dna_string = input("DNA: ")
'''
note: enumerate returns two values:
    1) count of current iteration
    2) value at that current location
'''

def complement(input_string):
    tempString = list(input_string)

    char = { 'A' : 'T', 'T': 'A', 'C' : 'G', 'G' : 'C'}

    for index, item in enumerate(tempString):
        for key, value in char.items():
            if item == key:
                tempString[index]=value
    
    return "".join(tempString)

def stringReverser(input_string):
    return input_string[::-1]
print('\n'+'RNA: '+stringReverser(complement(dna_string)))

'''
AAAACCCGGT
 -> tempStirng=[A, A, A, A, C, C, C, G, G, T]
 ->  0(index) = A(item)
    -> iterate over dictionary
        -> if A == A
            replace A with T

'''