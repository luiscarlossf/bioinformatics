#Aluno: Luis Carlos da Silva Filho

def readFasta():
    """
    Ler um arquivo fasta e retorna um dicionário com as informações
    do arquivo lido.

    :return dic: dicionário com as informações do arquivo fasta:
                 tamanho da leitura(k), distância entre as leituras(d) e
                 a sequência(sequence).
    """

    arquivo = input("Digite o nome do arquivo: (Exemplo: 'nome_arquivo.fasta')  ")
    dic = {}
    with open(arquivo, 'r') as fasta:
        for linha in fasta:
            if not linha.startswith('>'):
                dic['sequence'] = linha
            else:
                linha = linha.strip('>k=')
                linha = linha.split('d=')
                dic['k'] = int(linha[0])
                dic['d'] = int(linha[1])
        return dic
    
def kdMer(sequence, k, d):
    """
    O programa gera, em ordem lexicográfica, os (k,d) mers, em um arquivo texto.

    :param sequence: sequência genômica
    :param k: tamanho da leitura
    :param d: distância entre as leituras
    :return:
    """

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
    info = readFasta()
    kdMer(info['sequence'], info['k'], info['d'])