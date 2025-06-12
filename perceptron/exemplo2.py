import numpy as np

qtd_neuronios = 5

#qtd_epocas: permite com que o programador possa definir a quantidade de repetições durante a etapa de treinamento
qtd_epocas = 10

taxa_aprendizagem = 0.6

#TREINAMENTO

#X : vetor que representa a entrada dos dados
X = np.array([[40,4.0,3.5,2.0,2],[78,6.5,6.0,5.5,9],[67,5.0,5.0,4.5,6],[80,7.0,6.5,7.0,12],
[55,4.5,4.0,3.0,3],[90,9.5,9.0,8.5,22],[84,7.5,7.5,7.0,14],[65,5.5,5.0,4.5,7],
[70,6.5,6.0,5.5,10],[50,4.0,4.0,3.5,2],[93,8.5,8.0,8.0,17],[58,5.5,4.5,4.0,5],
[76,7.0,6.5,6.0,11],[82,8.0,7.5,7.5,13],[92,8.5,9.0,7.5,15],
[85,7.5,6.0,6.0,10]])
X = X/X.max(axis=0) #normalização

#print(X)
#y: representa as classes reais (base de dados)
y = np.array([0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,0])
#pesos: vetor responsável por armazenar os valores dos pesos de cada neurônio
pesos = np.zeros(qtd_neuronios+1)
#funcionamento da rede neural
#quantidade de repetições
for epoca in range(qtd_epocas):
    #analise de cada combinação de entrada
    #x_entrada: combinação dos valores de cada neurônio
    #y_entrada: classe real
    for x_entrada,y_entrada in zip(X,y): 
        #função de somatório que multiplica o peso pelo valor de cada neurônio
        soma = np.dot(pesos[1:],x_entrada)+pesos[0]
        #função de ativação (degrau): classe predita é determinada por meio do valor obtido na função de somatório
        if(soma >= 0.65):
            y_predita = 1 #1 - SIM
        else:
            y_predita = 0 #0 - NÃO
        #se a rede ACERTOU o valor da variável erro será 0
        #se a rede ERROU o valor da variável erro será diferente de 0
        erro = y_entrada - y_predita
        #ajuste
        #se a rede ACERTOU então não deve ser realizado o ajuste nos pesos
        #se a rede ERROU então o ajuste é calculado com base na taxa de aprendizagem e erro
        ajuste = taxa_aprendizagem * erro * x_entrada
        pesos[1:] = pesos[1:] + ajuste
        ajusteBIAS = taxa_aprendizagem*erro
        pesos[0] = pesos[0] + ajusteBIAS

#PREDIÇÃO OU VALIDAÇÃO OU TESTE
#X : vetor que representa a base de teste
X_teste = np.array([
[73,5.0,4.5,4.0,6],
[60,6.0,5.5,5.0,5],
[95,9.0,9.5,9.0,20],
[88,8.0,8.0,6.5,18],[12,5.0,5.0,3.0,5]])

X_teste = X_teste/X_teste.max(axis=0)

#y: representa as classes reais (base de dados de teste)
y_teste = np.array([0,0,1,1,0])
print(y_teste)
resultados=[]

for x_teste in X_teste:
    soma = np.dot(pesos[1:],x_teste)+pesos[0]
    if(soma >= 0.65):
        y_predita = 1 #1 - SIM
    else:
        y_predita = 0 #0 - NÃO
    resultados.append(y_predita)

res = np.array(resultados)
print(res)

acuracia = np.mean(y_teste == res)
print(acuracia)