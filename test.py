import whisper
import sounddevice
import wavio
import spicy
import sys

model = whisper.load_model("base")

freq = 44100
duration = 10

print("Recording starts...")

recording = sounddevice.rec(int(duration * freq),
                            samplerate=freq, channels=2)
    
sounddevice.wait()

wavio.write("recording.wav", recording, freq, sampwidth=2)

result = model.transcribe("recording.wav")

print(result["text"])

