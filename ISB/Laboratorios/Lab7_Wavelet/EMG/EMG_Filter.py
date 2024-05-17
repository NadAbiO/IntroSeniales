import numpy as np
import pywt
import matplotlib.pyplot as plt

data = np.loadtxt('Bruno.txt', skiprows=22, usecols=5)

# Define wavelet parameters
wavelet_db2 = 'db2'
wavelet_db6 = 'db6'
wavelet_db8 = 'db8'
level = 4

def denoise_signal(noisy_signal, wavelet, level):
    coeffs = pywt.wavedec(noisy_signal, wavelet, level=level)
    sigma = np.median(np.abs(coeffs[-level])) / 0.6745
    uthresh = sigma * np.sqrt(2 * np.log(len(noisy_signal)))
    denoised_coeffs = list(map(lambda x: pywt.threshold(x, value=uthresh, mode='soft'), coeffs))
    denoised_signal = pywt.waverec(denoised_coeffs, wavelet)
    return denoised_signal


denoised_signal_db2 = denoise_signal(data, wavelet_db2, level)

denoised_signal_db6 = denoise_signal(data, wavelet_db6, level)

denoised_signal_db8 = denoise_signal(data, wavelet_db8, level)

# Plot 
fig, axs = plt.subplots(4, 1, figsize=(14, 10))
fig.suptitle('EMG Signal Denoising using Wavelet Transform')

# Original signal
axs[0].plot(data)
axs[0].set_title('Señal Original')
axs[0].set_xlim([0, len(data)])

# Denoised signal (db2)
axs[1].plot(denoised_signal_db2)
axs[1].set_title('Señal filtrada (db2)')
axs[1].set_xlim([0, len(data)])

# Denoised signal (db6)
axs[2].plot(denoised_signal_db6)
axs[2].set_title('Señal filtrada (db6)')
axs[2].set_xlim([0, len(data)])

# Denoised signal (db8)
axs[3].plot(denoised_signal_db8)
axs[3].set_title('Señal filtrada (db8)')
axs[3].set_xlim([0, len(data)])

for ax in axs:
    ax.set_xlabel('Muestras')
    ax.set_ylabel('Amplitud')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
