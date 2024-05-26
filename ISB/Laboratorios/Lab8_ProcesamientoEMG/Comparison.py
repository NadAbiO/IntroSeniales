import numpy as np
import pywt
import scipy.signal as signal
import matplotlib.pyplot as plt

# Read the EMG signal from the .txt file, skipping header lines
def read_emg_signal(file_path):
    with open(file_path, 'r') as file:
        # Skip lines until `# EndOfHeader` is found
        for line in file:
            if line.strip() == '# EndOfHeader':
                break
        # Read the signal data
        signal = [float(line.split()[-1]) for line in file if line.strip()]
    return np.array(signal)

# Replace the path with the actual file path using raw string
file_path = r'Bruno(1).txt'
emg_signal = read_emg_signal(file_path)

# Define the sampling frequency
fs = 1000  # Adjust if known, otherwise estimate based on your data

# Create a time vector based on the length of the signal and the sampling frequency
t = np.linspace(0, len(emg_signal) / fs, len(emg_signal))

# Wavelet filter
def wavelet_denoise(signal, wavelet='db4', level=1, threshold=6):
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    coeffs[1:] = [pywt.threshold(c, threshold, mode='soft') for c in coeffs[1:]]
    return pywt.waverec(coeffs, wavelet)

wavelet_filtered = wavelet_denoise(emg_signal)

# FIR filter
numtaps = 101  # Filter order
cutoff = 50  # Cutoff frequency in Hz
fir_coeff = signal.firwin(numtaps, cutoff, fs=fs)
fir_filtered = signal.lfilter(fir_coeff, [1.0], emg_signal)

# IIR filter
sos = signal.butter(10, cutoff, 'low', fs=fs, output='sos')
iir_filtered = signal.sosfilt(sos, emg_signal)

# Calculate RMS
def rms(signal):
    return np.sqrt(np.mean(signal**2))

rms_wavelet = rms(wavelet_filtered)
rms_fir = rms(fir_filtered)
rms_iir = rms(iir_filtered)

print(f'RMS of wavelet filtered signal: {rms_wavelet}')
print(f'RMS of FIR filtered signal: {rms_fir}')
print(f'RMS of IIR filtered signal: {rms_iir}')

# Plot the results
plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
plt.plot(t, emg_signal, label='Original EMG Signal')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(t, wavelet_filtered, label='Wavelet Filtered Signal')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(t, fir_filtered, label='FIR Filtered Signal')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(t, iir_filtered, label='IIR Filtered Signal')
plt.legend()

plt.tight_layout()
plt.show()
