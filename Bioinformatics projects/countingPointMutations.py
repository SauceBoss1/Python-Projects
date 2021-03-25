dna_string1= input("DNA seq 1: ")
dna_string2= input('DNA seq 2: ')

def pointMutCounter(string1, string2):
    MutCounter = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            MutCounter += 1
    return MutCounter

print("There are "+ str(pointMutCounter(dna_string1, dna_string2)) +" mutations")