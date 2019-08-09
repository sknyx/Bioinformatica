import pandas
import re

filename = "TEXT_Uniprot_Data.txt"
file = open(filename, "r") 

AC_data = []
DE_data = []
concatData = ""
count = 0

for line in file:
  line_data = line

  if line_data.startswith('AC   '):
    AC_data.append( ((line_data.rstrip()).replace("AC   ","")).replace(";","") )
    count = 0

  elif line_data.startswith('DE   SubName:'):
    if count == 0:

      if concatData:
        concatData = re.sub(("{ECO:(.*)"),"",concatData)
        DE_data.append(concatData)

      concatData = (line_data.rstrip()).replace("DE   SubName: Full=","")
      count = count + 1 
    else:
      concatData = concatData + "\n" + (line_data.rstrip()).replace("DE   SubName: Full=","")
      count = count + 1

#end of file: crescenta última linha recuperada
concatData = re.sub(("{ECO:(.*)"),"",concatData)
DE_data.append(concatData)

#file.close()

#print(AC_data)
#print(DE_data)
#print('\n---\n'.join(map(str,DE_data)))

df = pandas.DataFrame(data={"AC": AC_data, "DE": DE_data})
df.to_csv("./Tabela_2_e.csv", sep=',',index=False)

Table = pandas.read_csv('Tabela_2_e.csv')
print("Tabela / Arquivo .csv criado!\n\n",Table)