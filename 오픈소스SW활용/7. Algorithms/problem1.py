"""
A DNA sequence is a string made up of the letters A, T, G, and C.
To find the complement of a DNA sequence, As are replaced by Ts, Ts by As, Gs by Cs, and Cs by Gs.
For example, the complement of AATTGCCGT is TTAACGGCA.
"""

def complement(str):
    temp = []
    for i in range(len(str)):
        if str[i] == 'T':
            temp.append('A')
        elif str[i] == 'A':
            temp.append('T')
        elif str[i] == 'G':
            temp.append('C')
        elif str[i] == 'C':
            temp.append('G')

    return "".join(temp)

code = input('input DNA sequence : ')
print('complement is', complement(code))
