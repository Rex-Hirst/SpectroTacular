import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sounddevice as sd
import librosa
import librosa.display


# Parameters
duration = 5  # seconds
fs = 22050  # Sample rate
buffer_size = 22050  # Buffer size for real-time processing

# Initializes buffer
audio_buffer = np.zeros(buffer_size)

# Function to update the spectrogram in real-time
def update_spectrogram(frame):
    global audio_buffer
    n_fft = min(2048, len(audio_buffer))  # Adjust n_fft based on the length of the audio buffer
    S = librosa.feature.melspectrogram(y=audio_buffer, sr = fs, n_mels = 128, fmax=8000, n_fft=n_fft)
    S_dB = librosa.power_to_db(S, ref=np.max)
    plt.clf()
    librosa.display.specshow(S_dB, sr = fs, x_axis='time', y_axis='mel')
    plt.colorbar(format = '%+2.0f dB')
    plt.title('Real-Time Spectrogram')


# Callback function to update the audio buffer
def audio_callback(indata, frames, time, status):
    global audio_buffer
    if status:
        print(status)
    audio_buffer = np.roll(audio_buffer, -frames)
    audio_buffer[-frames:] = indata[:, 0]


# Stream audio and update spectrogram in real-time
fig = plt.figure(figsize=(10, 4))
ani = animation.FuncAnimation(fig, update_spectrogram, interval=50, cache_frame_data=False)

with sd.InputStream(callback=audio_callback, channels=1, samplerate=fs):
    plt.show(block=True)
    sd.sleep(duration * 1000)
