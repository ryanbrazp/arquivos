from nltk import tokenize
import os
import pandas as pd

currentDirectory = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(currentDirectory, 'BASE_RYAN.xlsx')
data = pd.read_excel(filePath)
fullColumn = data['AVALIAÇÃO']

mainLine = str(data['AVALIAÇÃO'][0]).lower()

tokensMainLine = tokenize.word_tokenize(mainLine, language="portuguese")

for row in fullColumn:
    row = str(row).lower()  
    tokens = tokenize.word_tokenize(row, language="portuguese")  

    intersection = 0  

    for mainToken in tokensMainLine:
        if mainToken in tokens:  
            intersection += 1  

    union = len(set(tokensMainLine)) + len(set(tokens)) - intersection

    jaccard = intersection / union
    print(f"Jaccard: {jaccard}")
    print(f"Jaccard: {jaccard * 100:.2f}%")
    print("=================================")