dna_string = input("DNA: ")
def dna2rna(input_string):
    return("\n"+ "RNA: "+dna_string.replace("T","U"))

print(dna2rna(dna_string))