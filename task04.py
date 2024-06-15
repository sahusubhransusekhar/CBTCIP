import sounddevice as sd
import numpy as np
import wavio

# Settings
sample_rate = 44100  # Sample rate in Hz [CD quality]
duration = int(input("How long you wanna record [in sec] "))  # Duration of recording in seconds
filename = "output.wav"  # Output filename

def record_audio(sample_rate, duration, filename):
    print(f"Recording for {duration} seconds at {sample_rate} Hz...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")
    wavio.write(filename, audio, sample_rate, sampwidth=2)
    print(f"Audio saved as '{filename}'.")

def play_audio(filename):
    """Play an audio file."""
    print(f"Playing audio from '{filename}'...")
    # Read the WAV file
    wave_obj = wavio.read(filename)
    data = wave_obj.data
    sample_rate = wave_obj.rate
    # Play the audio data
    sd.play(data, samplerate=sample_rate)
    sd.wait()  # Wait until the audio has finished playing
    print("Playback finished.")

# Main script
if __name__ == "__main__":
    # Record audio
    record_audio(sample_rate, duration, filename)
    ip = input("Do you wanna play the audio? ")
    if ip.lower() in ("yes","y","yea","1"):
        # Play the recorded audio
        play_audio(filename)