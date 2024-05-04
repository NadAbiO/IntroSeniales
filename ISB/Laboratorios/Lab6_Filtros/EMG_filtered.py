import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re
import pywt
from scipy import signal
from scipy.signal import firwin, lfilter

arrayemg = np.genfromtxt(r"C:\Users\Kimberly\OneDrive\Escritorio\INTRO SEÑALES\IntroSeniales\ISB\Laboratorios\Lab3_EMG\Señales_EMG\Kim.txt", delimiter="\t", skip_header=3, missing_values=0)

#Extraemos la columna de la señal
signalemg = arrayemg[:, 5]
signalemg = signalemg[0:300]
Fs_emg = 100
Ts_emg = 1/Fs_emg
n_emg= 300
t_emg = np.arange(0,n_emg*Ts_emg,Ts_emg)
t_emg

niveles_emg = 4
coeficientes_emg = pywt.wavedec(signalemg, 'db6', level=niveles_emg)

plt.figure(figsize=(10, 10))
plt.subplot(niveles_emg + 2, 1, 1)
plt.plot(t_emg,signalemg)
plt.ylabel('Voltaje (mV)')
plt.xlabel('Tiempo (s)')
plt.title('Señal Original')

for i, detalle in enumerate(coeficientes_emg[1:]):  # Empezar desde el segundo nivel
    plt.subplot(niveles_emg + 2, 1, i + 2)
    plt.plot(detalle)
    plt.title(f'Detalle Nivel {i+1}')

plt.subplot(niveles_emg + 2, 1, niveles_emg + 2)
plt.plot(coeficientes_emg[0])
plt.title(f'Aproximación ')
plt.tight_layout()
plt.figure()

umbral = 0.022

coeficientes_umbral_emg = [pywt.threshold(c, umbral, mode='soft') for c in coeficientes_emg]

senal_filtrada_emg = pywt.waverec(coeficientes_umbral_emg, 'db6')

plt.figure(figsize=(10, 8))


plt.subplot(2, 1, 2)
plt.plot(t_emg, senal_filtrada_emg)
plt.xlim(1,3)
plt.title('Señal EMG Sujeto Femenino - Filtro Wavelet (db6)')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.tight_layout()
plt.figure()
plt.show()


#Filtro de banda de paso Butterwort
frequencies = [20, 500]  # Rango de frecuencia después del filtrado en Hz
Fs_emg = 100
w1 = 2 * np.pi * frequencies[0] / Fs_emg
w2 = 2 * np.pi * frequencies[1] / Fs_emg
butterworth_bandpass_emg = signal.butter(2, [w1, w2], btype='band', analog=False,fs=Fs_emg, output='ba')
emg_filtered = lfilter(butterworth_bandpass_emg[0], butterworth_bandpass_emg[1], signalemg)




#Filtro FIR
fc1 = 35  # Frecuencia de corte inferior en Hz
fc2 = 49  # Frecuencia de corte superior en Hz
fs = 1000  # Frecuencia de muestreo en Hz
orden = 1000  # Orden del filtro
filtro_fir_emg = firwin(orden + 1, [fc1, fc2], pass_zero=False, fs=Fs_emg, window='hamming')
emg_filtered = lfilter(filtro_fir_emg, 1, signalemg)



plt.figure(figsize=(10, 8))  # Increase the figure size for better visibility

# Plot the first graph
plt.subplot(3, 1, 1)  # (rows, columns, panel number)
plt.plot(t_emg, signalemg, label="señal")     
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.title("Señal EMG - Kim - Sin Filtrar")

# Plot the second graph
plt.subplot(3, 1, 2)
plt.plot(t_emg, emg_filtered, 'r', label='Señal de EMG Sujeto Femenino filtrada')
plt.title('Señal EMG - Kim - Filtro IIR Butterworth Bandpass')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Plot the third graph
plt.subplot(3, 1, 3)
plt.plot(t_emg, emg_filtered, 'r', label='Señal EEG filtrada')
plt.title('Señal EMG - Kim - Filtro FIR con ventana Hamming')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()