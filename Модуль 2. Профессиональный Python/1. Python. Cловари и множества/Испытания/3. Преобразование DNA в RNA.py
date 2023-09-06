'''ДНК и РНК это последовательности нуклеотидов.

Четыре нуклеотида в ДНК:

Аденин (A)
Цитозин (C)
Гуанин (G)
Тимин (T)
Четыре нуклеотида в РНК:

Аденин (A)
Цитозин (C)
Гуанин (G)
Урацил (U)
Цепь РНК составляется на основе цепи ДНК последовательной заменой каждого
нуклеотида:

G -> C
C -> G
T -> A
A -> U
dna.py
Напишите функцию to_rna, которая принимает на вход цепь ДНК и возвращает
соответствующую цепь РНК (совершает транскрипцию РНК).'''

# import dna

# dna.to_rna('ACGTGGTCTTAA')
# # 'UGCACCAGAAUU'

# def to_rna(chain):
#     dna = ['G', 'C', 'T', 'A']
#     rna = ['C', 'G', 'A', 'U']
#     dictionary = dict(zip(dna, rna))
#     str = ''
#     # print(dictionary)
#     for k in chain:
#         for v, _ in dictionary.items():
#             if k == v:
#                 str = str + dictionary[v]
#     return str


def to_rna(chain):
    dna_to_rna = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    str = ''
    for letter in chain:
        str += dna_to_rna[letter]
    return str

# SOLUTION
# MAPPING = {
#     "G": "C",
#     "C": "G",
#     "T": "A",
#     "A": "U",
# }


# def to_rna(dna):

#     rna = []
#     for nucliotide in dna:
#         rna.append(MAPPING[nucliotide])

#     return ''.join(rna)


# Альтернативный вариант с использованием map
# def to_rna(dna):
#     return ''.join(map(MAPPING.get, dna))

print(to_rna('ACGTGGTCTTAA'))  # 'UGCACCAGAAUU'
