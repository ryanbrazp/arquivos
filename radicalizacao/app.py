import nltk
from nltk.stem import RSLPStemmer

stemmer = RSLPStemmer()

# Em uma frase única ===============================================================
texto = "O rato roeu as roupas do rei de roma"
texto_tokennizado = nltk.word_tokenize(texto)
palavras_radizalizadas = []
for palavra in texto_tokennizado:
    palavra_radicalizada = stemmer.stem(palavra)
    palavras_radizalizadas.append(palavra_radicalizada)
print(palavras_radizalizadas)
# ====================================================================================



# Em uma lista de frases ===========================================================
lista_textos = [
    "O rato roeu as roupas do rei de roma",
    "o rápido raposo marrom salta sobre o cachorro preguiçoso",
    "o sol brilha intensamente no céu azul"
]
for frase in lista_textos:
    palavras_radizalizadas = []
    frase_tokennizada = nltk.word_tokenize(frase)
    for palavra in frase_tokennizada:
        palavra_radicalizada = stemmer.stem(palavra)
        palavras_radizalizadas.append(palavra_radicalizada)
    print(palavras_radizalizadas)
# ====================================================================================



# A partir de uma base de dados =====================================================
import pandas as pd
import os
currentDirectory = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(currentDirectory, '../BASE_RYAN.xlsx')
data = pd.read_excel(filePath)
column = data['AVALIAÇÃO']

for i, frase in column.items():
    palavras_radizalizadas = []
    frase_tokenizada = nltk.word_tokenize(frase)
    for palavra in frase_tokenizada:
        palavra_radicalizada = stemmer.stem(palavra)
        palavras_radizalizadas.append(palavra_radicalizada)
    print(f"{i+1}: {palavras_radizalizadas}\n")
# ====================================================================================