import whisper

model = whisper.load_model("small")
result = model.transcribe("caminho do áudio", language="pt")

print(result["text"])