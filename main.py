from scipy.io import wavfile
import noisereduce as nr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style

style.use('ggplot')

def plot_audio_signal(time, data, title):
    plt.plot(time, data, label=title)
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()

# Load data from original WAV file
rate_original, data_original = wavfile.read("input_audio.wav")

# Perform noise reduction
reduced_noise = nr.reduce_noise(y=data_original, sr=rate_original)

# Write the denoised audio to a new WAV file
wavfile.write("denoised_audio.wav", rate_original, reduced_noise)

# Calculate the time axis for plotting
time_original = np.arange(len(data_original)) / rate_original
time_denoised = np.arange(len(reduced_noise)) / rate_original  # Using the denoised data length

# Plot the original and denoised signals
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plot_audio_signal(time_original, data_original, 'Original WAV File')

plt.subplot(2, 1, 2)
plot_audio_signal(time_denoised, reduced_noise, 'Denoised WAV File')

plt.tight_layout()
plt.show()
