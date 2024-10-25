# TextToVoice

---

- [TextToVoice](#texttovoice)
  - [Descrizione](#descrizione)
  - [Requisiti](#requisiti)
  - [Descrizione delle Funzioni](#descrizione-delle-funzioni)
  - [Esecuzione](#esecuzione)

---

## Descrizione

Questo progetto consente di generare e riprodurre file audio in italiano utilizzando le librerie gTTS e playsound. Viene utilizzato Google Text-to-Speech (gTTS) per convertire un testo in un file audio, che successivamente viene riprodotto utilizzando playsound. Questo progetto è compatibile con sistemi macOS, Windows e Linux (con qualche accorgimento).

## Requisiti

Il progetto richiede le seguenti librerie:

- gTTS: per la sintesi vocale (Text-to-Speech).
- playsound: per riprodurre file audio.
- PyObjC: libreria necessaria solo su macOS per l’integrazione delle API di sistema.

Il file requirements.txt include tutte le librerie necessarie:

```sh

gTTS
playsound==1.2.2
PyObjC
```

Per installare le dipendenze, esegui il comando:

```sh

pip install -r requirements.txt

```

## Descrizione delle Funzioni

1. gTTS: Viene utilizzato per creare un file audio a partire da una stringa di testo.

   - text: testo da convertire in audio.
   - lang: codice della lingua (it per l’italiano).
   - slow: se impostato su True, rallenta la velocità dell’audio generato.

2. playsound: Riproduce il file audio generato. Gestisce anche eventuali eccezioni.

## Esecuzione

Per eseguire il codice:

1. Assicurati di aver installato tutte le dipendenze con pip install -r requirements.txt.
2. Avvia lo script Python:

```sh

python nome_script.py

```
