import nltk

# Em uma frase única ===============================================================
texto = "O rato roeu a roupa do rei de Roma"
print(nltk.word_tokenize(texto))
# ====================================================================================




# Em uma lista de frases ===========================================================
lista_textos = [
    "O rato roeu a roupa do rei de Roma",
    "A rápida raposa marrom pula sobre o cachorro preguiçoso",
    "O sol brilha intensamente no céu azul"
]
for frase in lista_textos:
    print(nltk.word_tokenize(frase))
# ====================================================================================




# A partir de uma base de dados =====================================================
import pandas as pd
import os

currentDirectory = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(currentDirectory, '../BASE_RYAN.xlsx')
data = pd.read_excel(filePath)
column = data['AVALIAÇÃO']

for i, assessment in column.items():
    print(f"{i+1}: {nltk.word_tokenize(assessment)}\n")
# ====================================================================================