import pandas
import re

filename = "TEXT_Uniprot_Data_Reviewed.txt"
file = open(filename, "r") 

AC_data = []
DE_data = []
concatData = ""
count = 0

for line in file:
  line_data = line

  if line_data.startswith("AC   "):
    AC_data.append( (line_data.rstrip()).replace("AC   ","") )

  elif line_data.startswith('DE   RecName: Full='):
    protein_full_name = ((line_data.rstrip()).replace("DE   RecName: Full=","")).replace(";","")
    protein_full_name = re.sub(("{ECO:(.*)"),"",protein_full_name)

    DE_data.append(protein_full_name)

file.close()

# print(len(AC_data))
# print(len(DE_data))
#print('\n---\n'.join(map(str,DE_data)))

df = pandas.DataFrame(data={"AC": AC_data, "DE - RecName: Full": DE_data})
df.to_csv("./Tabela_3.csv", sep=',',index=False)

Table = pandas.read_csv('Tabela_3.csv')
print("Tabela / Arquivo .csv criado!\n\n",Table)