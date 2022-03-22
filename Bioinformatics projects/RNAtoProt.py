codon_table = {
  'UUU':'F','UUC':'F',
  'UUA':'L','UUG':'L',
  'UCU':'S','UCC':'S','UCA':'S','UCG':'S',
  'UAU':'Y','UAC':'Y',
  'UAA':'Stop','UAG':'Stop',
  'UGU':'C','UGC':'C',
  'UGA':'Stop',
  'UGG':'W',
  'CUU':'L','CUC':'L','CUA':'L','CUG':'L',
  'CCU':'P','CCC':'P','CCA':'P','CCG':'P',
  'CAU':'H','CAC':'H',
  'CAA':'Q','CAG':'Q',
  'CGU':'R','CGC':'R','CGA':'R','CGG':'R',
  'AUU':'I','AUC':'I','AUA':'I',
  'AUG':'M',
  'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
  'AAU':'N','AAC':'N',
  'AAA':'K','AAG':'K',
  'AGU':'S','AGC':'S',
  'AGA':'R','AGG':'R',
  'GUU':'V','GUC':'V','GUA':'V','GUG':'V',
  'GCU':'A','GCC':'A','GCA':'A','GCG':'A',
  'GAU':'D','GAC':'D',
  'GAA':'E','GAG':'E',
  'GGU':'G','GGC':'G','GGA':'G','GGG':'G'
}


rna = input('RNA: ')

def rna_to_prot(rna, cod_tab):
  final_prot = ''
  for codon in range(0,len(rna),3):
    string_codon = cod_tab[rna[codon:codon+3]]
    if len(string_codon) != 1:
      return final_prot
    final_prot += string_codon
  return final_prot

print(rna_to_prot(rna, codon_table))
