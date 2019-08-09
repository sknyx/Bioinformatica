# Instituto Federal de Brasília - Taguatinga
# Curso: Bacharelado em Ciência da Computação - 7° semestre
# Disciplina: Introdução à Bioinformática - 1/2019
# Professor: Me. João Victor Oliveira 
# Estudante: Carolina Ataíde

# Alinhamento de Sequências Pairwise - Atividade Prática 3

import numpy as np
import pandas as pd
from copy import deepcopy
import sys

if len(sys.argv) > 1: # caso nao seja passado um arquivo por argumento, utiliza o arquivo padrão sequencias.fasta
  file = open(sys.argv[1],'r')
else:
  file = open('sequencias.fasta','r')

seq1 = ""
seq2 = ""
match_score = 3
mismatche_score = -3
gap_score = -2

# Função para dar split na sequência
def split(word): 
    return [char for char in word]

# Pegando as sequências
for line in file:
  seq = line.rstrip()
  if not seq.startswith('>id') and seq1 == "":
    seq1 = seq
  elif not seq.startswith('>id') and seq2 == "":
    seq2 = seq

# Inicialização da Matriz -> seq2 (linhas) seq1 (colunas)
matrix = np.zeros((len(seq2)+1, len(seq1)+1), dtype=int)

#listas com sequências separadas por nucleotídeos
seq1_Split = split(seq1)
seq2_Split = split(seq2)

# Preenchimento da matriz de pontuação
for i in range(1, len(seq2) +1 ):
  for j in range(1, len(seq1) +1 ):

    if seq2[i-1] == seq1[j-1]:
      match = matrix[i-1,j-1] + match_score
      gap_top = matrix[i-1,j] + gap_score
      gap_left = matrix[i,j-1] + gap_score
      mismatche = 0
      matrix[i,j] = max(match,gap_top,gap_left,mismatche)
    else:
      mismatche = matrix[i-1,j-1] + mismatche_score
      gap_top = matrix[i-1,j] + gap_score
      gap_left = matrix[i,j-1] + gap_score
      match = 0
      matrix[i,j] = max(match,gap_top,gap_left,mismatche)

# Impressão da matriz
print("\n*** Matriz de Pontuação ***\n")
ind = '-' + seq2
col = '-' + seq1
df = pd.DataFrame(matrix, index=list(ind), columns=list(col))
print(df)

# Calculando os 5 melhores alinhamentos
matrix_copy = deepcopy(matrix)
alinhamento = []
corresp = []

for i in range(5): #posições dos 5 maiores scores na matriz
  line,col = np.unravel_index(np.argmax(matrix_copy), matrix_copy.shape) #identifica a posição da matriz de pontução com o maior score
  print("\n----- caminho percorrido -------")
  print("\nLINHA: ",line,"  COL: ",col,"  SCORE: ", matrix[line,col])

  matrix_copy[line,col] = 0 #zera esse valor, de modo que na próxima iteração o maior score seja o i-ésimo maior score da matriz de pontuação
  parada = 1

  while parada > 0:

    parada = matrix[line-1,col-1]

    if matrix[line-1,col-1] >= matrix[line-1,col] and matrix[line-1,col-1] >= matrix[line,col-1]: #se o score da diagonal for maior que o score da linha acima e da linha ao lado
      
      # armazena os nucleotídeos que deram match
      if seq1[col-1] == seq2[line-1]:
        alinhamento.append(seq1[col-1])
        corresp.append(seq2[line-1])
      else:
        alinhamento.append('-')
        corresp.append(seq2[line-1])      

      print("LINHA: ", line-1,"  COL: ", col-1,"  SCORE: ", matrix[line-1,col-1])

      # percorrendo pela diagonal
      col = col - 1
      line = line - 1
      
    elif parada == 0: # fim do aliinhamento
      alinhamento.append(seq1[col-1])
      corresp.append(seq2[line-1])
      print("\nSeq1: ", alinhamento[::-1])
      print("Seq2: ", corresp[::-1])
      alinhamento = []
      corresp = []

    elif matrix[line-1,col-1] <= matrix[line,col-1] and matrix[line,col-1] >= matrix[line-1,col]: #se o score da esquerda for maior que o score da diagonal e da linha acima
      alinhamento.append('-') # considera um gap
      corresp.append(seq2[line])

      print("LINHA: ", line,"  COL: ", col-1,"  SCORE: ", matrix[line,col-1])

      col = col - 1 # nova diagonal

    else: # o score acima é maior que o score da diagonal e da esquerda
      alinhamento.append('-') # considera um gap
      corresp.append(seq2[line-1]) 

      print("LINHA: ", line-1,"  COL: ", col,"  SCORE: ", matrix[line-1,col])

      line = line - 1 # nova diagonal