import nltk

lemma = nltk.stem.PorterStemmer()

# Em uma frase única ===============================================================
texto = "the mouse gnawed the clothes of the king of rome"
texto_tokennizado = nltk.word_tokenize(texto)
palavras_lematizadas = []
for palavra in texto_tokennizado:
    palavra_lematizada = lemma.stem(palavra)
    palavras_lematizadas.append(palavra_lematizada)
print(palavras_lematizadas)
# ====================================================================================



# Em uma lista de frases ===========================================================
lista_textos = [
    "the mouse gnawed the clothes of the king of rome",
    "the quick brown fox jumps over the lazy dog",
    "the sun shines brightly in the blue sky"
]
for frase in lista_textos:
    palavras_lematizadas = []
    frase_tokennizada = nltk.word_tokenize(frase)
    for palavra in frase_tokennizada:
        palavra_lematizada = lemma.stem(palavra)
        palavras_lematizadas.append(palavra_lematizada)
    print(palavras_lematizadas)
# ====================================================================================



# A partir de uma base de dados =====================================================
import pandas as pd
import os
currentDirectory = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(currentDirectory, '../BASE_RYAN.xlsx')
data = pd.read_excel(filePath)
column = data['AVALIAÇÃO']

for i, frase in column.items():
    palavras_lematizadas = []
    frase_tokenizada = nltk.word_tokenize(frase)
    for palavra in frase_tokenizada:
        palavra_lematizada = lemma.stem(palavra)
        palavras_lematizadas.append(palavra_lematizada)
    print(f"{i+1}: {palavras_lematizadas}\n")
# ====================================================================================