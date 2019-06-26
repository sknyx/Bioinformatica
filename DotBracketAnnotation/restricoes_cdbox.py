# https://regex101.com/
import re

def restricoes_cdbox():

  #pegando as primeiras 50 sequências do arquivo
  with open("CD_dataset.fa", "r") as input:
      with open("filter_CD_dataset.fa", "w") as output: 
          sequences = [next(input) for line in range(50)]
          for i in sequences:
            output.write(i)

  #pegando as posições do C/D box de cada sequência
  with open("filter_CD_dataset.fa", "r") as sequences_file: 
    with open("restricted_CD_dataset.fa", "w") as output: 
      for line in sequences_file:

        #separando as infomações sobre as posições C, C', D' e D
        if line.startswith(">CD"):

          # escreve a linha original do header no novo file
          line = '\n' + line
          output.write(line)

          regex = re.compile("[ATGCU]+_[0-9]+")
          pos_info = regex.findall(line)
          #pegando apenas as posições do Cbox e Dbox
          pos_Cbox,pos_Dbox = pos_info[0].strip(r'[ATGCU]+_'),pos_info[-1].strip(r'[ATGCU]+_')
          # print(pos_Cbox, " ", pos_Dbox)
        
        else:

          #criando as restrições de acordo com as posições
          restriction = ''

          for position in range(1,len(line)):
            if position in range(int(pos_Cbox),int(pos_Dbox)+4):
              restriction = restriction + 'x'
            else:
              restriction = restriction + '.'
          restriction = restriction

          #caso tenha +10 nucleotídos tanto para antes do Cbox e depois do Dbox
          if int(pos_Cbox)>10 and len(line) >= (int(pos_Dbox) + 13):
            seq10 = line[int(pos_Cbox)-11:int(pos_Dbox)+13] + '\n'
            res10 = restriction[int(pos_Cbox)-11:int(pos_Dbox)+13]
            output.write(seq10)
            output.write(res10)

          #caso tenha +10 nucleotídos apenas para antes do Cbox
          elif int(pos_Cbox)>10 and len(line) < (int(pos_Dbox) + 13):
            seq10 = line[int(pos_Cbox)-11:]
            res10 = restriction[int(pos_Cbox)-11:]
            output.write(seq10)
            output.write(res10)

          #caso tenha +10 nucleotídos apenas para depois do Dbox
          elif int(pos_Cbox)<11 and len(line) >= (int(pos_Dbox) + 13):
            seq10 = line[:int(pos_Dbox)+13]
            res10 = restriction[:int(pos_Dbox)+13]
            output.write(seq10)
            output.write(res10)

          #caso não tenha +10 nucleotídos tanto para antes do Cbox e depois do Dbox
          else:
            seq10 = line
            res10 = restriction
            output.write(line)
            output.write(res10)

