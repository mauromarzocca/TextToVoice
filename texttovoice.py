import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
from gtts import gTTS
import fitz  # PyMuPDF
from pydub import AudioSegment
import os
import threading

# Lingue disponibili
LANGUAGES = {
    "Italiano": "it",
    "Inglese": "en",
    "Francese": "fr",
    "Spagnolo": "es",
    "Tedesco": "de",
    "Portoghese": "pt",
    "Olandese": "nl"
}

def carica_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("File PDF", "*.pdf")])
    if not file_path:
        return
    try:
        with fitz.open(file_path) as doc:
            testo = ""
            for pagina in doc:
                testo += pagina.get_text()
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, testo)
    except Exception as e:
        messagebox.showerror("Errore", f"Errore nell'aprire il PDF:\n{e}")

def spezza_testo(testo, lunghezza_massima=4500):
    parole = testo.split()
    blocchi = []
    blocco_corrente = ""
    for parola in parole:
        if len(blocco_corrente) + len(parola) + 1 < lunghezza_massima:
            blocco_corrente += " " + parola
        else:
            blocchi.append(blocco_corrente.strip())
            blocco_corrente = parola
    blocchi.append(blocco_corrente.strip())
    return blocchi

def avvia_conversione_thread():
    thread = threading.Thread(target=converti_audio)
    thread.start()

def converti_audio():
    testo = text_box.get("1.0", tk.END).strip()
    if not testo:
        messagebox.showwarning("Attenzione", "Inserisci del testo o carica un PDF.")
        return
    lingua = LANGUAGES.get(opzione_lingua.get())
    if not lingua:
        messagebox.showerror("Errore", "Seleziona una lingua.")
        return

    # Selezione file di destinazione
    file_path = filedialog.asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("File Audio MP3", "*.mp3")],
        title="Salva file audio",
        initialfile="output.mp3"
    )
    if not file_path:
        stato_var.set("Operazione annullata.")
        return

    try:
        blocchi = spezza_testo(testo)
        num_blocchi = len(blocchi)
        finale = AudioSegment.empty()

        progress_bar["value"] = 0
        progress_bar["maximum"] = num_blocchi
        stato_var.set("Inizio conversione...")

        for i, blocco in enumerate(blocchi):
            stato_var.set(f"Convertendo blocco {i+1} di {num_blocchi}...")
            tts = gTTS(text=blocco, lang=lingua)
            temp_file = f"temp_{i}.mp3"
            tts.save(temp_file)
            finale += AudioSegment.from_mp3(temp_file)
            os.remove(temp_file)
            progress_bar["value"] = i + 1
            root.update_idletasks()

        finale.export(file_path, format="mp3")
        stato_var.set("Conversione completata!")
        messagebox.showinfo("Successo", f"File audio salvato:\n{file_path}")
        os.system(f"open \"{file_path}\"" if os.name == "posix" else f"start \"{file_path}\"")

    except Exception as e:
        stato_var.set("Errore nella conversione.")
        messagebox.showerror("Errore", f"Errore nella sintesi vocale:\n{e}")

# UI
root = tk.Tk()
root.title("TextToVoice")
root.geometry("500x670")
root.resizable(False, False)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="TextToVoice", font=("Helvetica", 16, "bold")).pack(pady=5)

btn_pdf = tk.Button(frame, text="Carica un file PDF", command=carica_pdf)
btn_pdf.pack(pady=5)

tk.Label(frame, text="Oppure scrivi qui sotto").pack()
text_box = ScrolledText(frame, height=15)
text_box.pack(pady=5, fill="both", expand=True)

tk.Label(frame, text="Scegli la lingua:").pack(pady=5)
opzione_lingua = tk.StringVar(value="Italiano")
menu_lingua = tk.OptionMenu(frame, opzione_lingua, *LANGUAGES.keys())
menu_lingua.pack(pady=5)

btn_converti = tk.Button(frame, text="Genera Audio", command=avvia_conversione_thread)
btn_converti.pack(pady=10)

progress_bar = ttk.Progressbar(frame, orient="horizontal", mode="determinate", length=400)
progress_bar.pack(pady=5)

stato_var = tk.StringVar()
stato_label = tk.Label(frame, textvariable=stato_var)
stato_label.pack(pady=2)

root.mainloop()