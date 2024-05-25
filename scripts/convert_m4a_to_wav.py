from pydub import AudioSegment

# Load your audio file
audio = AudioSegment.from_file("Rua Professor Picarolo.m4a", format="m4a")

# Export as WAV
audio.export("Rua Professor Picarolo.wav", format="wav")

