
# Definição das bibliotecas a serem utilizadas

import numpy 

# Definição de constantes 

N = 8 # Tamanho da matriz a ser usado nas linhas e colunas

# este programa não funciona para N < 4 !!!!!

t_0 = 1 # valor da diagonal princial 

t_1 = 2 # valor da diagonal paralela a princial, chamaremos de espelho

t_2 = 3 # valor da diagonal paralela a diagonal espelho

# crianção de variáveis, vetores e matrizes


matriz = numpy.zeros((N,N)) 
#cria uma matriz quadrada
#de N linhas por N colunas preenchidas com zeros


# print(matriz) # exibe a matriz criada


# Aqui vamos inseir na matriz o valor da diagonal principal

for i in range(N):
    for j in range(N):
        if i==j:
            matriz[i,j] = t_0
            
# print(matriz) # exibe a matriz após inserção da diagonal principal


# Aqui vamos inseir na matriz o valor da diagonal espelho

for i in range(N):
    for j in range(-1,N):
# o valor -1 é para a condição de contorno periódica que coloca
# o valor de t_1 na quina, ou ponta, superior da matriz        
        if i==j+1:
            matriz[i,j] = t_1 # coloca valores no espelho inferior
        if i==j-1:
            matriz[i,j] = t_1 # coloca valores no espelo superior
        if j==N-1:
            matriz[N-1,0] = t_1 # condição de contorno periódica 
            # coloca o últmo valor na quina, ou ponta, infeior da matriz 


# print(matriz) # exibe a matriz após inserção da diagonal espelho


# Inserindo na na matriz o valor paralelo a diagonal espelho

for k in range(N):
    for l in range(-2,N):
# o valor -2 é para a condição de contorno periódica que coloca
# o valor de t_1 na quina, ou ponta, superior da matriz        
        if k==l+2:
            matriz[k,l] = t_2 # coloca valores no espelho inferior
        if k==l-2:
            matriz[k,l] = t_2 # coloca valores no espelo superior
        if k==N-2:
            matriz[N-2,0] = t_2 
            matriz[N-1,1] = t_2 
            # condição de contorno periódica 
            # coloca o últmo valor na quina, ou ponta, infeior da matriz 
        if N==4:
            matriz[N-2,0] = 2*t_2 
            matriz[N-1,1] = 2*t_2 
            matriz[0,N-2] = 2*t_2 
            matriz[1,N-1] = 2*t_2         
            # condição de contorno periódica no caso extremo inferior
            # coloca o últmo valor na quina, ou ponta, infeior da matriz 
            # contudo considera que esta operação é feita somando valores


# print(matriz) # exibe a matriz com o último valor posto 



