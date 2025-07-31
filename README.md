# TextToVoice

Versione 2.1 – Modalità Duale (Online + Offline)

---

- [TextToVoice](#texttovoice)
  - [Descrizione](#descrizione)
  - [Requisiti](#requisiti)
    - [macOS](#macos)
    - [Ubuntu/Debian](#ubuntudebian)
  - [Descrizione delle Funzioni](#descrizione-delle-funzioni)
    - [Motori vocali](#motori-vocali)
    - [Altre funzioni](#altre-funzioni)
  - [Esecuzione](#esecuzione)
  - [Note](#note)

---

![logo](logo.png)

## Descrizione

TextToVoice è un'applicazione con interfaccia grafica che consente di convertire testo o file PDF in file audio `.mp3`, con la possibilità di scegliere tra:

- ✅ **gTTS (Google Text-to-Speech)**: qualità migliore, richiede Internet
- ✅ **pyttsx3**: completamente offline

Il progetto è compatibile con macOS, Windows e Linux, e include:

- Estrazione testo da PDF
- Scelta lingua (per gTTS)
- Barra di avanzamento
- Salvataggio del file audio dove preferisci

## Requisiti

Il progetto richiede le seguenti librerie Python:

- **gTTS**: per la sintesi vocale online
- **pyttsx3**: per la sintesi vocale offline
- **PyMuPDF**: per leggere file PDF
- **pydub**: per unire e gestire file audio `.mp3`

Contenuto del `requirements.txt`:

```sh
gTTS
pyttsx3
pydub
PyMuPDF
```

Installa tutte le dipendenze con:

```sh
pip install -r requirements.txt
```

Inoltre, per il corretto funzionamento di `pydub`, è necessario installare `ffmpeg`:

### macOS

```sh
brew install ffmpeg
```

### Ubuntu/Debian

```sh
sudo apt install ffmpeg
```

## Descrizione delle Funzioni

### Motori vocali

1. **gTTS (online)**:
   - Richiede Internet
   - Voce robotica ma accettabile
   - Supporta molte lingue
   - Suddivide automaticamente il testo in blocchi se troppo lungo

2. **pyttsx3 (offline)**:
   - Funziona anche senza Internet
   - Voce dipende dal sistema operativo (su Windows è migliore)
   - Nessun limite di caratteri

### Altre funzioni

- `fitz` (PyMuPDF): estrae testo da PDF caricati
- `tkinter`: gestisce la UI
- `threading`: conversione senza bloccare la UI
- `filedialog`: permette di scegliere dove salvare l'audio

## Esecuzione

1. Installa le dipendenze:

  ```sh
  pip install -r requirements.txt
  ```

2. Avvia lo script:

```sh
python texttovoice_dualmode.py
```

3. Usa l'interfaccia per:
   - Caricare un PDF o scrivere testo
   - Selezionare la lingua (per gTTS)
   - Scegliere il motore vocale (online o offline)
   - Salvare l'audio dove preferisci

## Note

- Il motore `gTTS` richiede connessione Internet.
- Il motore `pyttsx3` è utile per lettura offline (es. in viaggio).
- Puoi usare questo strumento per creare audioguide, ascoltare documenti o semplificare letture lunghe.
