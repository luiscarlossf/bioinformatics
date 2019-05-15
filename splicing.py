"""
Splicing
Alunos: Luis Carlos da Silva Filho e Rodolfo Rodrigo Oliveira de Abreu
"""
#Entradas
DNA_string = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG'

#Removendo os introns da entrada
for intron in introns:
    DNA_string = DNA_string.replace(intron, '')
#Exibindo a saída
print("Saída: ", DNA_string)
