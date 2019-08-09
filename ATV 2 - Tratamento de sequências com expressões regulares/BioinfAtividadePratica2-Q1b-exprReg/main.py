# Instituto Federal de Brasília - Taguatinga
# Curso: Bacharelado em Ciência da Computação - 7° semestre
# Disciplina: Introdução à Bioinformática - 1/2019
# Professor: Me. João Victor Oliveira 
# Estudante: Carolina Ataíde

# Expressões Regulares em Bioinformática                                                      Atividade Prática 2: Questão 1 - letra B

import re

filename = 'toxins_3-5.fna'
file = open(filename,'r')

seqCompleta = [] #lista de sequencias completas do arquivo toxins_3-5.fna
mRNA = [] #lista de sequencia complementar da sequencia de toxins_3-5.fna
header = []
concatSeq = ''

for line in file:
  seqLine = line.rstrip() # seqLine recebe linha atual sem \n
  if seqLine.startswith('>lcl'):
    header.append(seqLine)  # se for header, armazena na lista header
    if not concatSeq == '':
      seqCompleta.append(concatSeq) # se concatSeq not null, armazena a seq concatenada na lista seqCompleta
    concatSeq = "" # reinicializa concatSeq
  else:
    concatSeq = concatSeq + seqLine # concatenação das linhas referantes a sequencia atual    
seqCompleta.append(concatSeq) # ao acabar o arquivo, salva a ultima seqCompleta concatenada

for seq in seqCompleta: #substs da fita original
  subst = re.sub('T','U',seq)
  subst = subst[::-1] #fita na direção 5' -> 3'
  mRNA.append(subst)

f = open('mRNA_toxins.fna', 'w')
for (a,b) in zip(header,mRNA):
  f.write(a+'\n')
  f.write(b+'\n')
f.close()
