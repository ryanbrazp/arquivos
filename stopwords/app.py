import nltk

stopwords = nltk.corpus.stopwords.words('portuguese')

# Em uma frase única ===============================================================
texto = "O rato roeu a roupa do rei de Roma"
texto_tokennizado = nltk.word_tokenize(texto)
palavras_relevantes = []
for palavra in texto_tokennizado:
    if palavra not in stopwords:
        palavras_relevantes.append(palavra)

print(palavras_relevantes)
# ====================================================================================




# Em uma lista de frases ===========================================================
lista_textos = [
    "O rato roeu a roupa do rei de Roma",
    "A rápida raposa marrom pula sobre o cachorro preguiçoso",
    "O sol brilha intensamente no céu azul"
]
for frase in lista_textos:
    palavras_relevantes = []
    frase_tokennizada = nltk.word_tokenize(frase)
    for palavra in frase_tokennizada:
        if palavra not in stopwords:
            palavras_relevantes.append(palavra)
    print(palavras_relevantes)
# ====================================================================================




# A partir de uma base de dados =====================================================
import pandas as pd
import os

currentDirectory = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(currentDirectory, '../BASE_RYAN.xlsx')
data = pd.read_excel(filePath)
column = data['AVALIAÇÃO']

for i, frase in column.items():
    palavras_relevantes = []
    frase_tokenizada = nltk.word_tokenize(frase)
    for palavra in frase_tokenizada:
        if palavra not in stopwords:
            palavras_relevantes.append(palavra)
    print(f"{i+1}: {palavras_relevantes}\n")