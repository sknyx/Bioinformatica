# Instituto Federal de Brasília - Taguatinga
# Curso: Bacharelado em Ciência da Computação - 7° semestre
# Disciplina: Introdução à Bioinformática - 1/2019
# Professor: Me. João Victor Oliveira 
# Estudante: Carolina Ataíde

# Expressões Regulares em Bioinformática                                                      Atividade Prática 2: Questão 1 - letra C

import re

filename = 'mRNA_toxins.fna'
file = open(filename,'r')

mRNA = [] #lista de sequencias completas do arquivo toxins_3-5.fna
mRNA_split3 = [] # lista com sequências divididas 3 em 3
aminoSeq = [] # lista com sequência de aminoácidos
header = []
concatSeq = ''
concatAminoSeq = ''

AminoDict =	{ 'F': ['UUU','UUC'],
              'L': ['UUA','UUG','CUU','CUC','CUA','CUG'],
              'I': ['AUU','AUC','AUA'],
              'M': ['AUG'],
              'V': ['GUU','GUC','GUA','GUG'],
              'S': ['UCU','UCC','UCA','UCG','AGU','AGC'],
              'P': ['CCU','CCC','CCA','CCG'],
              'T': ['ACU','ACC','ACA','ACG'],
              'A': ['GCU','GCC','GCA','GCG'],
              'Y': ['UAU','UAC'],
              ' STOP(OCHRE) ': ['UAA'],
              ' STOP(AMBER) ': ['UAG'],
              'H': ['CAU','CAC'],
              'Q': ['CAA','CAG'],
              'N': ['AAU','AAC'],
              'K': ['AAA','AAG'],
              'D': ['GAU','GAC'],
              'E': ['GAA','GAG'],
              'C': ['UGU','UGC'],
              ' STOP(OPAL) ': ['UGA'],
              'W': ['UGG'],
              'R': ['CGU','CGC','CGA','CGG','AGA','AGG'],
              'G': ['GGU','GGC','GGA','GGG']
}

## ## ##

def findAmino(seq3): # função para percorrer o dicionário, encontrar o match e retornar o                          aminoácido correspondente
  for i in AminoDict: 
    if seq3 in AminoDict[i]:
      return i

## ## ##

for line in file:
  seqLine = line.rstrip() # seqLine recebe linha atual sem \n
  if seqLine.startswith('>lcl'):
    header.append(seqLine)  # se for header, armazena na lista header
    if not concatSeq == '':
      concatSeq = concatSeq[::-1]
      mRNA.append(concatSeq) # se concatSeq not null, armazena a seq concatenada na lista mRNA
      mRNA_split3.append(re.findall('...',concatSeq))
    concatSeq = "" # reinicializa concatSeq
  else:
    concatSeq = concatSeq + seqLine # concatenação das linhas referantes a sequencia atual    

mRNA.append(concatSeq) # ao acabar o arquivo, salva o ultimo mRNA concatenada
concatSeq = concatSeq[::-1]
mRNA_split3.append(re.findall('...',concatSeq))

## ## ##

for seq in mRNA_split3:
  for seq3 in seq:
    concatAminoSeq = concatAminoSeq + str(findAmino(seq3))
  aminoSeq.append(concatAminoSeq)
  concatAminoSeq = ''

## ## ##

f = open('toxins.faa', 'w')
for (a,b) in zip(header,aminoSeq):
  f.write(a+'\n')
  f.write(b+'\n')
f.close()