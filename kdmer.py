"""
Para teste:
k= 3
d = 1
sequence = TAATGCCATGGGATGTT
Saída = 
"""
import io

k = int(input("k="))
d = int(input("d="))
sequence = input("Sequência de Nucleotídeos: ")

with open("k"+str(k)+"d"+str(d)+"mer.txt", "w") as file:
    tam =len(sequence)
    kdmers = [sequence[i:(i+k)]+"|"+sequence[(i+k+d):(i+d+k+k)] for i in range(0, tam-(k+d+(k-1)))]
    kdmers.sort()
    string = str(kdmers)
    file.write(string)
