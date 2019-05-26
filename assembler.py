#Aluno: Luis Carlos da Silva Filho

from kdmer import kdMer, readFasta

def Assembler(filename):
    """
    Remonta uma sequência genética a partir de um arquivo texto contendo os 
    kdmers em ordem lexicográfica.

    :param k: tamanho da leitura
    :param d: distância entre as leituras

    """
    try:
        kdmers = None
        prefixs = list()
        sufixs = list()
        _f = filename.strip('kdmer.txt').split('d')
        k = int(_f[0])
        d = int(_f[1])

        with open(filename, "r") as file:
            kdmers  = file.readline()
            kdmers = kdmers.strip('[')
            kdmers = kdmers.strip(']')
            kdmers = kdmers.split(',')

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
        
        with open("output-k"+str(k)+"d"+str(d)+"mer.fasta", "w") as file:
            file.write(">k="+str(k)+"d="+str(d)+"\n")

            start = way1.index(None)
            tam = len(sufixs[start][0])-1
            file.write(prefixs[start][0])
            file.write(sufixs[start][0][tam])

            i = way2[start]
            while i != None:
                file.write(sufixs[i][0][tam])
                i = way2[i]

            h = 0
            while h <= d:
                i = way2.index(i)
                h += 1

            file.write(prefixs[i][1])
            while i != None:
                file.write(sufixs[i][1][tam])
                i = way2[i]
            print("Arquivo de saída "+"output-k"+str(k)+"d"+str(d)+"mer.fasta"+ " criado com sucesso!")
            return
    except Exception:
        print("Não foi possível criar o arquivo de saída!")
        print("Verifique se o nome do arquivo está correto.")
    
            
if __name__ == "__main__":
    filename = input("Digite o nome do arquivo de entrada: (Exemplo: k5d2mer.txt)\n")
    Assembler(filename)