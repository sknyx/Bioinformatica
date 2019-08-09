# Instituto Federal de Brasília - Taguatinga
# Curso: Bacharelado em Ciência da Computação - 7° semestre
# Disciplina: Introdução à Bioinformática - 1/2019
# Professor: Me. João Victor Oliveira 
# Estudante: Carolina Ataíde

# Expressões Regulares em Bioinformática                                                      Atividade Prática 2: Questão 1 - letra A

import re

filename = 'toxins.fna'
file = open(filename,'r')

seqCompleta = [] #lista de sequencias completas do arquivo original
seqMolde = [] #lista de sequencia complementar da sequencia original
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

for seq in seqCompleta: #complementos da fita original
  complemento = re.sub('T','X',seq)
  complemento = re.sub('A', 'T', complemento)
  complemento = re.sub('X', 'A', complemento)
  complemento = re.sub('C', 'Y', complemento)
  complemento = re.sub('G', 'C', complemento)
  complemento = re.sub('Y', 'G', complemento)

  complemento = complemento[::-1] #fita na direção 3' -> 5'
  seqMolde.append(complemento)

f = open('toxins_3-5.fna', 'w')
for (a,b) in zip(header,seqMolde):
  f.write(a+'\n')
  f.write(b+'\n')
f.close()

#print(len(seqMolde))
#print('\n---\n'.join(map(str,seqMolde)))

def split(word): 
    return [char for char in word]