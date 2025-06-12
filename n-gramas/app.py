import nltk

# Em uma frase única ===============================================================
frase = "O produto foi entregue corretamente porém a qualidade é péssima. Não voltarei a comprar com esse fornecedor."
tokens = nltk.word_tokenize(frase.lower())
# Gerar bigramas
bigramas = list(nltk.ngrams(tokens, 2))
trigramas = list(nltk.ngrams(tokens, 3))
pentagramas = list(nltk.ngrams(tokens, 5))
# ====================================================================================



# Em uma lista de frases ===========================================================
lista_frases = [
    "O produto foi entregue corretamente porém a qualidade é péssima. Não voltarei a comprar com esse fornecedor.",
    "A entrega foi rápida, mas o produto não atendeu às expectativas.",
    "O atendimento ao cliente foi excelente, mas o produto chegou danificado."
]
for frase in lista_frases:
    tokens = nltk.word_tokenize(frase.lower())
    bigramas = list(nltk.ngrams(tokens, 2))
    trigramas = list(nltk.ngrams(tokens, 3))
    pentagramas = list(nltk.ngrams(tokens, 5))
    print(f"Frase: {frase} \n")
    print("Bigramas:", bigramas, "\n")
    print("Trigramas:", trigramas, "\n")
    print("Pentagramas:", pentagramas, "\n")
    print("======================================================================================================\n")
# ====================================================================================




# A partir de uma base de dados =====================================================
import pandas as pd
import os
currentDirectory = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(currentDirectory, '../BASE_RYAN.xlsx')
data = pd.read_excel(filePath)
column = data['AVALIAÇÃO']
for i, frase in column.items():
    tokens = nltk.word_tokenize(frase.lower())
    bigramas = list(nltk.ngrams(tokens, 2))
    trigramas = list(nltk.ngrams(tokens, 3))
    pentagramas = list(nltk.ngrams(tokens, 5))
    print(f"{i+1}: {frase} \n")
    print("Bigramas:", bigramas, "\n")
    print("Trigramas:", trigramas, "\n")
    print("Pentagramas:", pentagramas, "\n")
    print("======================================================================================================\n")
# ====================================================================================