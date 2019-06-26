# https://www.tbi.univie.ac.at/RNA/ViennaRNA/doc/html/rna_structure_notations.html
import re

def dotbracket():
# sequence -> ACAGTATGAGCAGAGGAAATCCAGACGGGTTGTTTCCTGTTTGTCTTGGGACCTGTCTCTACACCTCTGCCACACTT
  db = "..(((.((.(((((((......(((((((((....((..........))))))))))).....))))))))).)))."

  hairpin_loop(db)

def hairpin_loop(db):
  regex = re.compile("\(+\.+\)")
  pos_info = regex.findall(db)
  print("Hairpin Loop: ", pos_info)

def stem(db):
  