import numpy as np
import brainflow
from brainflow.data_filter import DataFilter, FilterTypes, DetrendOperations, AggOperations
import matplotlib.pyplot as plt
import pandas as pd
import mne
from mne.preprocessing import ICA, corrmap, create_ecg_epochs, create_eog_epochs
import time
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
import pywt
import scipy.stats
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Especifica el path de tu archivo de OpenBCI
file_path = 'Intro.py/OpenBCI_GUI-v5-meditation.txt'

# Leer el archivo de texto
data = pd.read_csv(file_path, comment='%', header=None)

# Extraer las columnas relevantes (suponiendo que las primeras 8 columnas después de la columna de índice son los datos de EEG) y todas las filas
eeg_data = data.iloc[1:30000, 1:9]
eeg_trans = pd.DataFrame(np.transpose(eeg_data))
eeg = eeg_trans.to_numpy()

# Verifica la estructura de los datos
print(eeg)

eeg_channels = [1, 2, 3, 4, 5, 6, 7, 8]
eeg_data = eeg / 1000000  # Convertir de microvoltios a voltios

eeg_trans = pd.DataFrame(np.transpose(eeg_data))
eeg_trans = np.ascontiguousarray(eeg_trans)
DataFilter.write_file(eeg_trans, 'test.csv', 'w')
restored_data = DataFilter.read_file('test.csv')
restored_df = pd.DataFrame(np.transpose(restored_data))
print('Data From the File')
print(restored_df.head(10))

# Crear un objeto Raw de MNE
ch_types = ['eeg'] * len(eeg_channels)
ch_names = [
    "FC3",
    "FCz",
    "FC4",
    "C3",
    "Cz",
    "C4",
    "CP3",
    "CPz"
]
sfreq = 250
info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)
raw = mne.io.RawArray(eeg_data, info)

# Aplicación de ICA
ica = mne.preprocessing.ICA(n_components=8, random_state=97, max_iter=800)
ica.fit(raw)
ica.exclude = [0]  # Índices para excluir basados en inspección manual o métodos automáticos
reconst_raw = raw.copy()
ica.apply(reconst_raw)

# Filtrado
reconst_raw.filter(l_freq=1., h_freq=40.)

# Normalización
reconst_raw.apply_function(lambda x: (x - np.mean(x)) / np.std(x), picks=['eeg'])

# Crear eventos sintéticos para demostración
events = mne.make_fixed_length_events(reconst_raw, start=0, stop=None, duration=2.0)
epochs = mne.Epochs(reconst_raw, events, event_id=1, tmin=-0.2, tmax=0.5, baseline=(None, 0), preload=True)
evoked = epochs.average()

# Graficar los datos evocados y GFP
evoked.plot(spatial_colors=True, gfp=True)

# Función para extraer características de los coeficientes wavelet
def extract_wavelet_features(data, wavelet='db2', level=4):
    features = []
    for channel_data in data:
        coeffs = pywt.wavedec(channel_data, wavelet, level=level)
        channel_features = []
        
        for coeff in coeffs:
            # Mediana
            median_val = np.median(coeff)
            
            channel_features.append(median_val)  # Solo la mediana
            
        features.append(channel_features)
    
    return np.array(features)

# Obtener los datos normalizados del objeto MNE
data_normalized = reconst_raw.get_data()

# Extraer características
features = extract_wavelet_features(data_normalized)

# Mostrar las características extraídas
print("Características extraídas:", features.shape)
print("Ejemplo de características extraídas para el primer canal:", features[0])

# Crear DataFrame para facilitar la visualización
df_features = pd.DataFrame(features, columns=['Delta (0.1-3 Hz)', 'Theta (4-7 Hz)', 'Alpha (8-12 Hz)', 'Beta (12-30 Hz)', 'Gamma (30-100 Hz)'])

# Graficar características por bandas de frecuencia (median values)
fig, axes = plt.subplots(1, 5, figsize=(25, 5))

for i, band in enumerate(df_features.columns):
    sns.boxplot(data=df_features[band], ax=axes[i])
    axes[i].set_title(f'Median values of {band}')
    axes[i].set_xlabel('Canales')
    axes[i].set_ylabel('Mediana')
    axes[i].set_xticklabels(['1'])

plt.tight_layout()
plt.show()

# Graficar los datos evocados y GFP, RMS
time = np.linspace(-0.2, 0.5, epochs.get_data().shape[-1])
channel_names = ["FC3", "FCz", "FC4", "C3", "Cz", "C4", "CP3", "CPz"]

fig, axs = plt.subplots(4, 1, figsize=(15, 20))
mean_data = np.mean(epochs.get_data(), axis=0).T
median_data = np.median(epochs.get_data(), axis=0).T
gfp = np.std(epochs.get_data(), axis=1).mean(axis=0)
rms = np.sqrt(np.mean(epochs.get_data() ** 2, axis=1)).mean(axis=0)

# Graficar la media
for ch, name in zip(mean_data.T, channel_names):
    axs[0].plot(time, ch, label=name)
axs[0].set_title('Evoked Responses Combined by mean (mean)')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('µV')
axs[0].legend()

# Graficar la mediana
for ch, name in zip(median_data.T, channel_names):
    axs[1].plot(time, ch, label=name)
axs[1].set_title('Evoked Responses Combined by median (median)')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('µV')
axs[1].legend()

# Graficar GFP
axs[2].plot(time, gfp, label='GFP')
axs[2].set_title('Evoked Responses Combined by gfp (GFP)')
axs[2].set_xlabel('Time (s)')
axs[2].set_ylabel('µV')
axs[2].legend()

# Graficar RMS
axs[3].plot(time, rms, label='RMS')
axs[3].set_title('Evoked Responses Combined by RMS (RMS)')
axs[3].set_xlabel('Time (s)')
axs[3].set_ylabel('µV')
axs[3].legend()

plt.tight_layout()
plt.show()
