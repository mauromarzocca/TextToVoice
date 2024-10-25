from gtts import gTTS
from playsound import playsound
from datetime import datetime

# Genera un nome file basato sulla data e sull'orario corrente
current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
audio = f'audio_{current_time}.mp3'

# Impostazione della lingua
language = 'it'

# Creazione dell'oggetto gTTS e generazione dell'audio
sp = gTTS(text="Ciao, io sono TextToVoice", lang=language, slow=False)
sp.save(audio)

# Riproduzione del file audio
try:
    playsound(audio)
except Exception as e:
    print(f"Errore nella riproduzione dell'audio: {e}")