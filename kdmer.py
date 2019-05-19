"""
Para teste:
k= 3
d = 1
sequence = TAATGCCATGGGATGTT
Saída = 
"""

def kdMer(sequence, k, d):

    with open("k"+str(k)+"d"+str(d)+"mer.txt", "w") as file:
        tam =len(sequence)
        kdmers = [sequence[i:(i+k)]+"|"+sequence[(i+k+d):(i+d+k+k)] for i in range(0, tam-(k+d+(k-1)))]
        kdmers.sort()
        file.write('[')
        for i, kdmer in enumerate(kdmers):
            if i != 0:
                file.write(',')
            file.write(kdmer)
        file.write(']')
        return kdmers

if __name__ == "__main__":
    k = int(input("k="))
    d = int(input("d="))
    sequence = input("Sequência de Nucleotídeos: ")
    kdMer(sequence, k, d)