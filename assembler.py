from kdmer import kdMer
"""
For test:
    k=999d=999 
    GTGGTCGTGAGATGTTGA
"""

def Assembler(k, d):
    """
    Remonta uma sequência genética a partir de um arquivo texto contendo os 
    kdmers em ordem lexicográfica.
    :param:
    :retn:
    """
    with open("k"+str(k)+"d"+str(d)+"mer.txt", "r") as file:
        kdmers  = file.readline()
        kdmers = kdmers.strip('[')
        kdmers = kdmers.strip(']')
        kdmers = kdmers.split(',')
        prefixs = list()
        sufixs = list()
        for i in kdmers: #Divide os kdmers [ABCD|EFGH] => prefixs = [ABC, EFG], sufixs = [BCD, FGH]
            vertice = i.split('|')
            prefixs.append([vertice[0][0:(k-1)], vertice[1][0:(k-1)]])
            sufixs.append([((vertice[0][::-1])[0:k-1])[::-1], ((vertice[1][::-1])[0:k-1])[::-1]])
        
        way1 = list() #Numera os prefixos para cada kdmers
        way2 = list() #Numera os sufixos para cada kdmers
        for i in prefixs:
            try:
                way1.append(sufixs.index(i))
            except ValueError:
                way1.append(None)
        for i in sufixs:
            try:
                way2.append(prefixs.index(i))
            except ValueError:
                way2.append(None)

        start = way1.index(None)
        tam = len(sufixs[start][0])-1

        print(prefixs[start][0])
        print(sufixs[start][0][tam])

        i = way2[start]
        while i != None:
            print(sufixs[i][0][tam])
            i = way2[i]
        h = 0
        while h <= d:
            print(i)
            i = way2.index(i)
            h += 1
        print(prefixs[i][1])
        while i != None:
            print(sufixs[i][1][tam])
            i = way2[i]

       
        



if __name__ == "__main__":
    k = int(input("k="))
    d = int(input("d="))
    sequence = input("Sequência de Nucleotídeos: ")
    kdMer(sequence, k, d)
    Assembler(k, d)