from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
language = 'it'

# Genera il file audio con gTTS
sp = gTTS(text="Ciao, io sono TextToVoice", lang=language, slow=False)
sp.save(audio)

# Riproduci l'audio
try:
    playsound(audio)
except Exception as e:
    print(f"Errore nella riproduzione dell'audio: {e}")