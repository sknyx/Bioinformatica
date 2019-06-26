# https://regex101.com/
import re

def restricoes_hacabox():

  #pegando as primeiras 50 sequências do arquivo
  with open("HACA_dataset.fa", "r") as input:
      with open("filter_HACA_dataset.fa", "w") as output: 
          sequences = [next(input) for line in range(50)]
          for i in sequences:
            output.write(i)

  #pegando as posições do H/ACA box de cada sequência
  with open("filter_HACA_dataset.fa", "r") as sequences_file: 
    with open("restricted_HACA_dataset.fa", "w") as output: 
      for line in sequences_file:

        #separando as infomações sobre as posições H e ACA
        if line.startswith(">HACA"):

          # escreve a linha original do header no novo file
          line = '\n' + line
          output.write(line)

          #espressão regular para encontrar as posições do Hbox e ACAbox no header
          regex = re.compile("_[ATGCU]+_[0-9]+")
          pos_info = regex.findall(line)

          #pegando apenas as posições do Hbox e ACAbox
          pos_Hbox,pos_ACAbox = pos_info[0].strip(r'_[ATGCU]+_'),pos_info[-1].strip(r'_[ATGCU]+_')
          # print(pos_Hbox, " ", pos_ACAbox)
        
        else:

          # restrição -> Hbox como inicio e ACAbox + 3nts como fim
          seq_restricted = line[int(pos_Hbox)-1:int(pos_ACAbox)+6]
          output.write(seq_restricted)

          #sequencia original
          # output.write(line)
