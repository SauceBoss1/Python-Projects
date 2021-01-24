
givenDNA = "TTTGACCCAGGCCCGAGAGAGTCTGAGTCCAACACCCCTCATCCATTTAAATCGTATGTATAGATACCGCCGAGTCGGGCGCATGCACCATCGGCCCGAGTACTCGTGAATCACGAGGTAGCGAACGACTGTCTCAGACTGCGGGCCTATGTGTGTTACTAGATGGCGAGACTGCTCATCTACTCCTTAGAGATTTGCTATGTACACATTACAATCTCCAAGTGGAACCAATTAGCTCGGAAAGGATGAAATAAACACAGCCTACCAATGAAATGAACTCAAACCCCCGGCTGGGAAGAAGATTTTTTTCGTTCGTCCTCTGGGAAGATCTCGATCTGAAACACCGGAATGTTGACTGTGGTTGCAACGAATTTGTGCTGCGAGTGGATGGCCAATGCGTGTTACGGAATGAATCCCCGTAAGCGCTCAACGAAAAATGCGGCATTCTTCGGTTGATAATGGGGGAACTAGGAACACGGCTTGTATACCGGCAGCACGTTAATGTGGACTTCATTCTTCGAGCGTGTAAATGGGATCGCGGCGGCACGGTTAGGTAAAACCGTCGTAAGATTGGCCAATGCCGTCGAGGAAAATCACGCCCTGGTTGGCATTACGAAGCTCCTCTGAAGAGGTGGCGCGTGCACACAACTTTTCATAAACATGTGAGCGTTCTTCGATACCCATCCCGATTATCCTTAATTGGCGTAAAGTCTATCCGTCGTATGGTGCTTTAAGGTTCTGCAGACGGCGAGCTAGAGCTCGGGGTTCTTCTTCACCGGCATTTAAATGTGTAATTGTTTATAGTTTCCTCTCCAATATGACCAGCGCTTCGGTTATGGTCACGCCCGTATATACTGCAACTCAATAACCTGTCAATCACTAGGACGGGGCCGTTACAGATCTCATCACTATCATGTACTTATTCGAATACGTGGCCATTTTC"

nucleotides = {"A":0, "C":0, "G":0, "T":0} 

for nuc in givenDNA:
    nucleotides[nuc] += 1

#print(f'{nucleotides["A"]} {nucleotides["C"]} {nucleotides["T"]} {nucleotides["G"]}')
print(' '.join([str(val) for key, val in nucleotides.items()]))
