import nltk

# Em uma frase única ===============================================================
texto = "O rato roeu a roupa do rei de Roma"
texto_tokenizado = nltk.word_tokenize(texto.lower())

palavras_relevantes = []
for palavra in texto_tokenizado:
    if palavra not in nltk.corpus.stopwords.words('portuguese'):
        palavras_relevantes.append(palavra)

frequencia_palavras = nltk.FreqDist(palavras_relevantes)
print(frequencia_palavras.most_common())
# ====================================================================================




# Em uma lista de frases ===========================================================
lista_textos = [
    "O rato roeu a roupa do rei de Roma",
    "A rápida raposa marrom pula sobre o cachorro preguiçoso",
    "O sol brilha intensamente no céu azul"
]
for frase in lista_textos:
    frase_tokenizada = nltk.word_tokenize(frase.lower())
    palavras_relevantes = []
    for palavra in frase_tokenizada:
        if palavra not in nltk.corpus.stopwords.words('portuguese'):
            palavras_relevantes.append(palavra)
    
    frequencia_palavras = nltk.FreqDist(palavras_relevantes)
    print(f"{frase}: {frequencia_palavras.most_common()}")  
# ====================================================================================




# A partir de uma base de dados =====================================================
import pandas as pd
import os
currentDirectory = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(currentDirectory, '../BASE_RYAN.xlsx')
data = pd.read_excel(filePath)
column = data['AVALIAÇÃO']

for i, texto in column.items():
    frase_tokenizada = nltk.word_tokenize(texto.lower())
    palavras_relevantes = []
    for palavra in frase_tokenizada:
        if palavra not in nltk.corpus.stopwords.words('portuguese'):
            palavras_relevantes.append(palavra)
    
    frequencia_palavras = nltk.FreqDist(palavras_relevantes)
    print(f"{i+1}: {frequencia_palavras.most_common()}\n")
# ====================================================================================