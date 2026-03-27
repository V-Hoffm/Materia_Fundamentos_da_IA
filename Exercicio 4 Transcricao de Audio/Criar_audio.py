from gtts import gTTS

tts = gTTS("Olá, este é um teste de transcrição de áudio", lang="pt")
tts.save("voz_teste.mp3")