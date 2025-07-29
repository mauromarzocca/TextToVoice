# TextToVoice

Versione 2.1

---

- [TextToVoice](#texttovoice)
  - [Descrizione](#descrizione)
  - [Requisiti](#requisiti)
    - [macOS](#macos)
    - [Ubuntu/Debian](#ubuntudebian)
  - [Descrizione delle Funzioni](#descrizione-delle-funzioni)
  - [Esecuzione](#esecuzione)
  - [Note](#note)

---

![logo](logo.png)

## Descrizione

Questo progetto consente di generare file audio da testo scritto o da file PDF, utilizzando le librerie `gTTS` e `pydub`. Il testo può essere scritto manualmente o importato da un file PDF tramite l’interfaccia grafica.  
Il progetto è compatibile con sistemi macOS, Windows e Linux.

Le funzionalità principali includono:

- Estrazione del testo da file PDF
- Scelta della lingua di sintesi vocale
- Suddivisione automatica del testo in blocchi se troppo lungo
- Generazione e salvataggio del file audio `.mp3`
- Interfaccia utente con barra di avanzamento

## Requisiti

Il progetto richiede le seguenti librerie Python:

- **gTTS**: per la sintesi vocale (Text-to-Speech).
- **PyMuPDF**: per estrarre testo da file PDF.
- **pydub**: per unire blocchi vocali in un unico file audio.

Il file `requirements.txt` include tutte le dipendenze Python necessarie:

```sh
gTTS
pydub
PyMuPDF
pyttsx3
```

Per installare le dipendenze, esegui il comando:

```sh
pip install -r requirements.txt
```

Inoltre è necessario installare `ffmpeg`, richiesto da `pydub` per elaborare i file audio.

### macOS

```sh
brew install ffmpeg
```

### Ubuntu/Debian

```sh
sudo apt install ffmpeg
```

## Descrizione delle Funzioni

1. **gTTS**: Viene utilizzato per creare un file audio a partire da una stringa di testo.
   - `text`: testo da convertire in audio.
   - `lang`: codice della lingua (es. `it` per l’italiano).
   - `slow`: se impostato su `True`, rallenta la velocità dell’audio generato.
   - `pyttsx3`: Permette di impostare la velocità del linguaggio.

2. **pydub**: Unisce più file audio `.mp3` generati in un unico file finale.

3. **fitz (PyMuPDF)**: Permette di estrarre il testo dalle pagine di un file PDF.

4. **tkinter**: Crea l’interfaccia grafica per selezionare PDF, scrivere testo, scegliere la lingua e avviare la conversione.

5. **threading**: Permette la generazione dell’audio senza bloccare l’interfaccia.

## Esecuzione

Per eseguire il progetto:

1. Installa le dipendenze:

```sh
pip install -r requirements.txt
```

2. Avvia lo script principale:

  ```sh
  python texttovoice.py
  ```

3. Usa l’interfaccia per:
   - Caricare un file PDF oppure scrivere del testo
   - Scegliere la lingua
   - Salvare il file audio in una posizione a tua scelta

## Note

- `playsound` e `PyObjC` **non sono più necessari**.
- È possibile salvare il file audio con un nome e in una cartella a tua scelta.
- L'audio viene riprodotto automaticamente al termine se supportato dal sistema operativo.
