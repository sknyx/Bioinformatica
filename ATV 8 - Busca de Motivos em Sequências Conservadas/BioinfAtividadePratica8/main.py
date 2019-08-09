# -*- coding: utf-8 -*-
import re
import numpy as np
import pandas as pd 

filename = "D.motif"
file = open(filename, "r")

order = ['C','T','G','A'] #ordem dos nucleotídeos

seq_list = [] # lista com todas as sequências
qtd_list = [] #lista com a quantidade de cada sequência

position = 0
id_nuc = -1

for line in file:
  line_data = line
  aux = re.split("\t", line_data) #retirando a tabulação entre a sequência e o número
  seq_list.append(aux[0])
  qtd_list.append(int(aux[1].rstrip()))

#configuração do modo como o numpy lida com números do tipo float -> senão sai uns números doidos do tipo 6.4757e+08
float_formatter = lambda x: "%f" % x
np.set_printoptions(formatter={'float_kind':float_formatter})

#inicialização da pssm -> colocada uma coluna a mais para guardar a overall freq. quando necessário
pssm = np.zeros((4, len(seq_list[0])+1), dtype=object) 

for n in order: #para cada nucleotideo
  id_nuc = id_nuc + 1
  for seq in seq_list: #para cada sequencia
    seq_position = seq_list.index(seq) #pega a posição dessa sequência na lista
    for position in range(0,len(seq)): #para cada posição dessa sequência
      if n == seq[position]:

        pssm[id_nuc,position] = pssm[id_nuc,position] + qtd_list[seq_position]
  # pssm[id_nuc,len(seq_list[0])] = sum(pssm[id_nuc:])

print("\n--------- Matriz de Quantidades Totais:")
# impressão com labels
df = pd.DataFrame(pssm[0:4,0:len(seq_list[0])], index=list(order), columns=range(1,len(seq_list[0])+1))
print("\n")
print(df)

pssm = pssm/sum(qtd_list)

print("\n\n--------- Matriz de Frequências Totais:")
# impressão com labels
df = pd.DataFrame(pssm[0:4,0:len(seq_list[0])], index=list(order), columns=range(1,len(seq_list[0])+1))
print("\n")
print(df)

for i in range(0,4):
  #somar os valores da linha e dividí-los pela quantidade de posições, para encontrar a Overall freq.
  pssm[i,len(seq_list[0])] = pssm[i,i:len(seq_list[0])].sum() / len(seq_list[0])

  #dividir cada valor da linha pela Overall freq. encontrada acima
  for j in range(0,len(seq_list[0])):
    pssm[i,j] = pssm[i,j]/pssm[i,len(seq_list[0])]

print("\n\n--------- Matriz de Frequências Totais Normalizadas:")
# impressão com labels
df = pd.DataFrame(pssm[0:4,0:len(seq_list[0])], index=list(order), columns=range(1,len(seq_list[0])+1))
print("\n")
print(df)

#Converte os scores normalizados para escala logarítmica na base 2

for i in range(0,4):
  for j in range(0,len(seq_list[0])):
    if pssm[i,j] != 0:
      pssm[i,j] = np.log2(pssm[i,j])
    else:
      pssm[i,j] = '--'

print("\n\n--------- PSSM Completa:")
# impressão com labels
df = pd.DataFrame(pssm[0:4,0:len(seq_list[0])], index=list(order), columns=range(1,len(seq_list[0])+1))
print("\n")
print(df)

df.to_csv('D_scores_totais.csv')

file.close()
