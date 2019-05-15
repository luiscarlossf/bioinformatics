#Tradução do DNA
#Alunos: Luis Carlos da Silva Filho e Rodolfo Rodrigo Oliveira de Abreu

def translation(entrada, codigo):
    aminoacido = ""
    #codons = entrada.split('.') #Forma as trincas de códons
    codons = [ entrada[i:i+3] for i in range(0, len(entrada), 3)]
    flag = False
    for codon in codons:
        if flag == False:
            if codon == 'AUG':
                aminoacido += codigo[codon]
                flag = True
        elif (codon != 'UAA') and (codon != 'UAG') and (codon != 'UGA'):
            aminoacido += codigo[codon]
        else:
            #aminoacido += codigo[codon]
            break
    return aminoacido

geneticCode = {
'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
'UCU':'S', 'UCC':'S', 'UCA':'L', 'UCG':'L',
'UAU':'Y', 'UAC':'Y', 'UAA':'ST', 'UAG':'ST',
'UGU':'C', 'UGC':'C', 'UGA':'ST', 'UGG':'W',
'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
}

test = "AUG.GUC.UAC.AUA.GCU.GAC.AAA.CAG.CAC.GUA.GCA.UCU.CGA.GAG.GCA.UAU.GGU.CAC.AUG.UUC.AAA.GUU.UGC.GCC.UAG"
entrada = input("Digite o RNAm:(Formato - CODON.CODON.CODON)")
print("RNAm: ", entrada)
print("Cadeia de Aminoacido:", translation(entrada, geneticCode))
