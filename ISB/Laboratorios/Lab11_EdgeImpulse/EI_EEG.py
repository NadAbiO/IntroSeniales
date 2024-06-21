import time
import hmac
import hashlib
import json
import requests
import random

def upload_ei(_name_label, _values, hmac_key, api_key):
    HMAC_KEY = hmac_key
    API_KEY = api_key
    emptySignature = ''.join(['0'] * 64)

    # Assuming Fs is your sampling frequency in Hz
    Fs = 360
    Ts = (1 / Fs) * 1000

    data = {
        "protected": {
            "ver": "v1",
            "alg": "HS256",
            "iat": time.time()  # epoch time, seconds since 1970
        },
        "signature": emptySignature,
        "payload": {
            "device_name": "ac:87:a3:0a:2d:1b",
            "device_type": "NANO33BLE",
            "interval_ms": Ts,
            "sensors": [
                { "name": "Volts", "units": "adu/mv" }
            ],
            "values": _values
        }
    }

    # Encode in JSON
    encoded = json.dumps(data)

    # Sign message
    signature = hmac.new(bytes(HMAC_KEY, 'utf-8'), msg=encoded.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()

    # Set the signature again in the message, and encode again
    data['signature'] = signature
    encoded = json.dumps(data)

    # Upload the file
    res = requests.post(
        url='https://ingestion.edgeimpulse.com/api/training/data',
        data=encoded,
        headers={
            'Content-Type': 'application/json',
            'x-file-name': _name_label,
            'x-api-key': API_KEY
        }
    )

    if res.status_code == 200:
        print('Uploaded file to Edge Impulse', res.status_code, res.content)
    else:
        print('Failed to upload file to Edge Impulse', res.status_code, res.content)

# Reemplaza estos valores con los tuyos
HMAC_KEY = "a5397fbbee5402cb004a390b528264c7"
API_KEY = "ei_394d6e18a9c95986048d940c2624a58d78e3ff639a7644fb73e8225430ec1391"
NAME_LABEL = "Kim_signal_EEG"
FILE_PATH = "Kim_EEG.txt"


# Función para verificar si una línea puede convertirse a un float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Leer los valores del archivo TXT, ignorando líneas no numéricas
with open(FILE_PATH, 'r') as file:
    values = [list(map(float, line.strip().split())) for line in file if is_float(line.strip().split()[0])]

# Dividir los datos en fragmentos de 1000 muestras cada uno
chunk_size = 1000
chunks = [values[i:i + chunk_size] for i in range(0, len(values), chunk_size)]

# Subir cada fragmento como un archivo separado
for i, chunk in enumerate(chunks):
    if len(chunk) == chunk_size:  # Asegurarse de que solo suba fragmentos completos de 1000 muestras
        file_name = f"EEG_signal{i+1}.json"
        upload_ei(file_name, chunk, HMAC_KEY, API_KEY)