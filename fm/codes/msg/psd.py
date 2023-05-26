#plot for PSD of message signal

import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
sample_rate, audio_data = wav.read('/home/megha/signal-processing/fm/codes/msg/Sound_Noise.wav')
frequencies, psd = plt.psd(audio_data, Fs=sample_rate)
plt.figure(figsize=(10, 6))
plt.plot(frequencies, 10 * np.log10(psd))
plt.xlabel('Frequency (Hz)')
plt.ylabel('PSD (dB/Hz)')
plt.title('Power Spectral Density')
plt.grid(True)
plt.show()


