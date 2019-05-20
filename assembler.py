from kdmer import kdMer
def Assembler(k, d):
    with open("k"+str(k)+"d"+str(d)+"mer.txt", "r") as file:
        kdmers  = file.readline()
        kdmers = kdmers.strip('[')
        kdmers = kdmers.strip(']')
        kdmers = kdmers.split(',')
        prefixs = list()
        sufixs = list()
        for i in kdmers:
            vertice = i.split('|')
            prefixs.append([vertice[0][0:(k-1)], vertice[1][0:(k-1)]])
            sufixs.append([((vertice[0][::-1])[0:k-1])[::-1], ((vertice[1][::-1])[0:k-1])[::-1]])
        
        way1 = list()
        way2 = list()
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
        print(kdmers)
        print(prefixs)
        print(sufixs)
        print(way1)
        print(way2)
        start = way1.index(None)
        end = way2.index(None)
        tam = len(sufixs[start][0])-1
        print(prefixs[start][0])
        print(sufixs[start][0][tam])
        i = way2[start]
        print(tam)
        print(sufixs[i][0][tam])
        while True:
            i = way2[i]
            if i != None:
                print(sufixs[i][0][tam])
            else:
                break
        h = 0
        while h < d-1:
            i = way1.index(i)
            h += 1
        print(i)
        i = h
        print(prefixs[i][1])
        print(sufixs[i][1][tam])
        while True:
            if i != None:
                print(sufixs[i][1][tam])
            else:
                break
            i = way2[i]

       
        



if __name__ == "__main__":
    k = int(input("k="))
    d = int(input("d="))
    sequence = input("Sequência de Nucleotídeos: ")
    kdMer(sequence, k, d)
    Assembler(k, d)