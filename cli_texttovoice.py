#!/usr/bin/env python3
import os
import sys
import time
import fitz  # PyMuPDF
from gtts import gTTS
import pyttsx3
from pydub import AudioSegment
from datetime import datetime

LANGUAGES = {
    "Italiano": "it",
    "Inglese": "en",
    "Francese": "fr",
    "Spagnolo": "es",
    "Tedesco": "de",
    "Portoghese": "pt",
    "Olandese": "nl"
}

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

def leggi_pdf(percorso):
    try:
        with fitz.open(percorso) as doc:
            testo = ""
            for pagina in doc:
                testo += pagina.get_text()
        return testo
    except Exception as e:
        print(f"[✘] Errore nella lettura del PDF: {e}")
        sys.exit(1)

def scegli_modalita():
    print("Scegli il motore vocale:")
    print("1) gTTS (online)")
    print("2) pyttsx3 (offline)")
    scelta = input("Scelta [1-2]: ").strip()
    return "gTTS" if scelta == "1" else "pyttsx3"

def scegli_lingua():
    print("Lingue disponibili:")
    for i, (nome, codice) in enumerate(LANGUAGES.items(), 1):
        print(f"{i}) {nome} ({codice})")
    idx = input("Scegli la lingua [numero]: ").strip()
    chiave = list(LANGUAGES.keys())[int(idx) - 1]
    return LANGUAGES[chiave]

def salva_audio(nome, audio):
    nome_output = f"{nome}_{datetime.now().strftime('%Y%m%d-%H%M%S')}.mp3"
    audio.export(nome_output, format="mp3")
    print(f"[✔] File salvato come: {nome_output}")

def main_loop():
    while True:
        print("\n📄 TextToVoice CLI (PDF/Text to Audio)")
        scelta_input = input("File (PDF o TXT) o testo? (F - File, T - Testo): ").strip().lower()

        if scelta_input == "f":
            file_path = input("Percorso del file (PDF o TXT): ").strip()
            if not os.path.exists(file_path):
                print("[✘] File non trovato.")
                continue
            if file_path.lower().endswith(".pdf"):
                testo = leggi_pdf(file_path)
            else:
                with open(file_path, "r", encoding="utf-8") as f:
                    testo = f.read()
        elif scelta_input == "t":
            print("Inserisci il testo da convertire (termina con una riga vuota):")
            lines = []
            while True:
                riga = input()
                if riga.strip() == "":
                    break
                lines.append(riga)
            testo = "\n".join(lines)
        else:
            print("[✘] Scelta non valida.")
            continue

        if not testo.strip():
            print("[✘] Nessun testo trovato.")
            continue

        motore = scegli_modalita()

        if motore == "gTTS":
            lingua = scegli_lingua()
            blocchi = spezza_testo(testo)
            finale = AudioSegment.empty()
            for i, blocco in enumerate(blocchi):
                print(f"[gTTS] Converto blocco {i+1}/{len(blocchi)}...")
                tts = gTTS(text=blocco, lang=lingua)
                temp = f"temp_{i}.mp3"
                tts.save(temp)
                finale += AudioSegment.from_mp3(temp)
                os.remove(temp)
            salva_audio("audio_gtts", finale)
        else:
            print("[pyttsx3] Sintesi vocale offline in corso...")
            try:
                engine = pyttsx3.init()
                engine.setProperty('rate', 150)
                nome_output = f"audio_pyttsx3_{datetime.now().strftime('%Y%m%d-%H%M%S')}.mp3"
                engine.save_to_file(testo, nome_output)
                engine.runAndWait()
                print(f"[✔] File salvato come: {nome_output}")
            except Exception as e:
                print(f"[✘] Errore nella sintesi pyttsx3: {e}")
                continue

        altra_operazione = input("\nVuoi fare un'altra conversione? (S/N): ").strip().lower()
        if altra_operazione != "s":
            print("Uscita dal programma.")
            break

if __name__ == "__main__":
    main_loop()
