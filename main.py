# a simple script that a tkinter interface to load a file and use openai whisper to transcribe it
import tkinter as tk
from tkinter import filedialog, messagebox
import whisper




def write_transcription_to_file(transcription, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(transcription)

def transcribe_files(paths):
    model = whisper.load_model("turbo")
    for path in paths:
        print(f"Transcribing {path}...")
        result = model.transcribe(path)
        output_file = path.rsplit('.', 1)[0] + '_transcription.txt'
        write_transcription_to_file(result['text'], output_file)
    messagebox.showinfo("Succes !", "Transcription réussie! \n Les fichiers ont été enregistrés.")


# gui
def select_files():
    file_paths = filedialog.askopenfilenames(title="Selectionner les fichiers audio (avec shift+clic pour plusieurs)", 
                                             filetypes=[("Audio Files", "*.mp3 *.wav *.m4a *.flac *.mp4")])
    if file_paths:
        transcribe_files(file_paths)
    else:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        

root = tk.Tk()
root.title("Credits : Paul B")
root.geometry("300x150")
select_button = tk.Button(root, text="Selectionner les fichiers audio", command=select_files)
select_button.pack(expand=True)
root.mainloop()