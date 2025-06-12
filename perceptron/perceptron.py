import numpy as np

#qtd_neuronios: está diretamente ligada com os valores de entrada (Está quente? e Está sol?)
qtd_neuronios = 2

#qtd_epocas: permite com que o programador possa definir a quantidade de repetições durante a etapa de treinamento
qtd_epocas = 10

#taxa_aprendizagem: realiza a calibragem dos pesos associadas a cada neurônio, o valor varia entre 0 e 1, determina o tamanho do passo (mudança no valor)
taxa_aprendizagem = 0.3

#TREINAMENTO
#N1: 0 N2: 0
#N1: 0 N2: 1
#N1: 1 N2: 0
#N1: 1 N2: 1
#X : vetor que representa a entrada dos dados
X = np.array([[0,0],[0,1],[1,0],[1,1]])
#y: representa as classes reais (base de dados)
y = np.array([0,0,0,1])
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
        if(soma >= 0):
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
X_teste = np.array([[0,0],[0,1],[1,0],[1,1]])
#y: representa as classes reais (base de dados de teste)
y_teste = np.array([0,0,0,1])

resultados=[]

for x_teste in X_teste:
    soma = np.dot(pesos[1:],x_teste)+pesos[0]
    if(soma >= 0.5):
        y_predita = 1 #1 - SIM
    else:
        y_predita = 0 #0 - NÃO
    resultados.append(y_predita)

res = np.array(resultados)

acuracia = np.mean(y_teste == res)
print(acuracia)

        


