from scipy.fftpack import fft,fftshift
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import scipy.signal as signal

# Load WAV file
sample_rate, audio = wavfile.read('Sound.wav')

# Perform FFT on signal
fft = np.fft.fft(audio)

# Calculate power spectral density
psd = np.abs(fft)**2

# Calculate frequency range
freqs = np.fft.fftfreq(len(psd), 1/sample_rate)

# Plotting input spectrum using power vs freq
plt.plot(freqs,psd)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('Input Signal')
plt.show()
