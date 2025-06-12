import nltk
from nltk import tokenize

S="O rato roeu a roupa do rei de roma"
T=" O rei de roma foi romero"

tokensS = tokenize.word_tokenize(S,language="portuguese")
tokensT = tokenize.word_tokenize(T,language="portuguese")

print(tokensS)
print(tokensT)

interseccao = 0

for s in tokensS:
    for t in tokensT:
        if(s == t):
            interseccao = interseccao+1

print(interseccao)

tamS = tokensS.__len__()
tamT = tokensT.__len__()
uniao = (tamS+tamT)-interseccao

print(uniao)

jaccard = interseccao/uniao

print(jaccard)