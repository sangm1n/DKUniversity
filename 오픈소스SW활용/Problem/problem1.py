"""
A DNA sequence is a string made up of the letters A, T, G, and C.
To find the complement of a DNA sequence, As are replaced by Ts, Ts by As, Gs by Cs, and Cs by Gs.
For example, the complement of AATTGCCGT is TTAACGGCA.
"""


def complement(str):
    answer = []
    for i in range(len(str)):
        if str[i] == 'a':
            answer.append('t')
        elif str[i] == 't':
            answer.append('a')
        elif str[i] == 'c':
            answer.append('g')
        elif str[i] == 'g':
            answer.append('c')
        else:
            answer.append(' ')

    return "".join(answer)


DNA = input('DNA sequence : ')
print('The complement is :', complement(DNA))
