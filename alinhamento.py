"""
    Algoritmo de Smith-Waterman(Alinhamento Local) e Needleman-Wunsch(Alinhamento Global)
    Aluno: Luis Carlos da Silva Filho
    Sequência 1: GLSDGEWQQVLNVWGKVEADIAGHGQEVLIRLFTGHPETLEKFDKFKHLKTEAEMKASEDLKKHGTVVLTALGGILKKKGHHEAELKPLAQDHATKHKIPIKYLEFISDAIIHVLHSKHPGDFGADAQGAMTKALELFRNDIAAKYKELGFQG
    Sequência 2: MGLSDGEWQQVLNVWGKVEADIAGHGQEVLIRLFTGHPETLEKFDKFKHLKTEAEMKASEDLKKHGTVVLTALGGILKKKGHHEAELKPLAQSHATKHKIPIKYLEFISDAIIHVLHSKHPGDFGADAQGAMTKALELFRNDIAAKYKELGFQG
    
    =========== ALINHAMENTO LOCAL ==========
    Score:  757
    Sequência 1:  GLSDGEWQQVLNVWGKVEADIAGHGQEVLIRLFTGHPETLEKFDKFKHLKTEAEMKASEDLKKHGTVVLTALGGILKKKGHHEAELKPLAQDHATKHKIPIKYLEFISDAIIHVLHSKHPGDFGADAQGAMTKALELFRNDIAAKYKELGFQG
    Sequência 2:  GLSDGEWQQVLNVWGKVEADIAGHGQEVLIRLFTGHPETLEKFDKFKHLKTEAEMKASEDLKKHGTVVLTALGGILKKKGHHEAELKPLAQSHATKHKIPIKYLEFISDAIIHVLHSKHPGDFGADAQGAMTKALELFRNDIAAKYKELGFQG
    ========================================

    ========== ALINHAMENTO GLOBAL ==========
    Score:  747
    Sequência 1:  -GLSDGEWQQVLNVWGKVEADIAGHGQEVLIRLFTGHPETLEKFDKFKHLKTEAEMKASEDLKKHGTVVLTALGGILKKKGHHEAELKPLAQDHATKHKIPIKYLEFISDAIIHVLHSKHPGDFGADAQGAMTKALELFRNDIAAKYKELGFQG
    Sequência 2:  MGLSDGEWQQVLNVWGKVEADIAGHGQEVLIRLFTGHPETLEKFDKFKHLKTEAEMKASEDLKKHGTVVLTALGGILKKKGHHEAELKPLAQSHATKHKIPIKYLEFISDAIIHVLHSKHPGDFGADAQGAMTKALELFRNDIAAKYKELGFQG
    ========================================
"""

import numpy as np
########################################################
#ENTRADAS
sequence1 = input("Sequência 1:") #'CTAACACCCA'
sequence2 = input("Sequência 2:") #'ACAC'
match = int(input("Digite o valor do Match:"))
mismatch = int(input("Digite o valor do Mismatch:"))
gap = int(input("Digite o valor do Gap:"))
local = int(input("Digite <1> para Alinhamento Local, <outro número> para Alinhamento Global:\n"))
#########################################################

flag = False #Verifica qual é a base
if len(sequence1) < len(sequence2):
   flag = True
   aux = sequence1
   sequence1 = sequence2
   sequence2 = aux

sequence1 = '-' + sequence1
sequence2 = '-' + sequence2

if local == 1:
    local = True #Se True - Alinhamento Local, senão Alinhamento Global
else:
    local = False

size_line = len(sequence1)
size_column = len(sequence2)

scores_matrix = np.zeros((size_line, size_column))

##########################################
#INICIALIZAÇÃO DOS GAPS
if local:
    scores_matrix[0:size_line, 0] = 0
    scores_matrix[size_line-1, 0:size_column] = 0
else:
    scores_matrix[0:size_line, 0] = gap * np.flip(np.arange(0, size_line), axis=0)
    scores_matrix[size_line-1, 0:size_column] = gap * np.arange(0, size_column)
ways_matrix= np.empty([size_line-1, size_column-1,3])

#############################################

##########################################
#PREENCHIMENTO DA MATRIZ
for i in np.flip(np.arange(0, size_line-1), axis=0):
    for j in np.arange(1, size_column):
        left = 0
        center = 0
        down = 0
        #Mis or Macth?
        if sequence1[(size_line-1)-i] == sequence2[j]:
            center = match
        else:
            center = mismatch
        #Cálculos
        center += scores_matrix[i+1, j-1]
        left = scores_matrix[i, j-1] + gap
        down = scores_matrix[i+1, j] + gap
        _max = max([left, center, down])
        #Indica posições de onde vieram
        ways_matrix[i, j-1] = [left==_max, center==_max, down==_max]
        #Atualiza o valor na matrix
        if local:
            if _max < 0:
                scores_matrix[i, j] = 0
            else:
                scores_matrix[i, j] = _max
        else:
            scores_matrix[i, j] = _max
print(scores_matrix)

############################################
#TRACEBACK

colunm = scores_matrix[0:size_line, size_column-1]
line = scores_matrix[size_line-1, 0:size_column]
indexs_colunm = np.where(colunm == colunm.max())
indexs_line = np.where(line == line.max())
score = 0
vertical = ''
horizontal = ''
score_set = list()
sequence_set = list()
for i in indexs_colunm:
    x = i[0]
    y = size_column-1
    score = scores_matrix[x, y]
    while True:
        if local and  scores_matrix[x, y]== 0:
            break
        aux = None
        if local:
            aux = scores_matrix[x, y]
        way = np.where(ways_matrix[x, y-1]==True) #Retorna o lado de origem

        #Verificando qual é o caminho que tem valor maior
        if len(way) != 1:
            lista = [[0,0]] * 2
            for i, value in enumarate(way): #Pega os scores dos caminos possíveis
                if value[0] == 0:
                    lista[i] = [scores_matrix[x, y-1], value[0]]
                elif value[0] == 1:
                    lista[i] = [ scores_matrix[x+1, y-1], value[0]]
                elif value[0] == 2:
                    lista[i] = [scores_matrix[x+1, y], value[0]]
            way = max(lista)[0] #Seleciona o caminho com maior score
        elif x == size_line-1 or y == 0:
            way = -1
        else:
            way = way[0][0]


        if way == 0:#left
            vertical += '-'
            horizontal += sequence2[y]
            y -= 1
        elif way == 1:#center
            #print("x=", x,"seq=", sequence1[(size_line-1)-x])
            #print("Y=", y,"seq=", sequence2[y])
            vertical += sequence1[(size_line-1)-x]
            horizontal += sequence2[y]
            x += 1
            y -= 1
        elif way == 2:#down
            vertical += sequence1[(size_line-1)-x]
            horizontal += '-'
            x += 1
        else:
            vertical += sequence1[(size_line-1)-x]
            horizontal += sequence2[y]
            #print("x=", x,"seq=", sequence1[(size_line-1)-x])
            #print("Y=", y,"seq=", sequence2[y])
            break


        if x == size_line or y == -1:
            break
if flag:
    sequence1 = horizontal[::-1]
    sequence2 = vertical[::-1]
else:
    sequence1 = vertical[::-1]
    sequence2 = horizontal[::-1]

if local:
    print("=========== ALINHAMENTO LOCAL ==========")
else:
    print("========== ALINHAMENTO GLOBAL ==========")
print("Score: ", int(score))
print("Sequência 1: ", sequence1)
print("Sequência 2: ", sequence2)
print("========================================")
print("\n")
