import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "1.imagens": [".png", ".jpg", ".jpeg"],
    "2.pdfs": [".pdf"],
    "3.compactados": [".rar", ".zip"],
    "4.instaladores": {".exe"},
    "5.programas": {".msi"},
    "6.Midia": {".mp3", ".mp4", ".gif", ".MKV", ".MPEG", ".WAV"},
    "7.Planilhas": {".xml", ".xlsx", ".csv", ".ods", ".tsv"},
    "8.Words": {".docx", ".doc", ".docx", ".XLS"},
    "9.Slides": {".pptx"},
}

for arquivo in lista_arquivos:
    # 01. Arquivo.pdf
    nome, exstensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if exstensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.makedirs(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
