def bytes(lista):
    for i in range(0, 6):
        lista[i] = lista[i]/1048576
        lista[i] = round(lista[i], 2)
        #print(lista[i])

def percentual(lista, lista2, total):
    for i in range(0, 6):
        lista2[i] = (lista[i]*100)/total
        lista2[i] = round(lista2[i], 2)
        
def main():    
    arquivo = open('usuarios.txt','r')
    leitura = ['s', 's', 's', 's', 's', 's']

    for i in range(0,6):
        leitura[i] = arquivo.readline()

    linhas = ['s', 's', 's', 's', 's', 's']
    num = [0, 0, 0, 0, 0, 0]

    for i in range(0, 6):
        linhas[i] = leitura[i][0:14]

    for i in range(0, 6):
        num[i] = int(leitura[i][15:])

    bytes(num)
    total = 0
    for i in range(0, 6):
        total = total + num[i]
    per = [0, 0, 0, 0, 0, 0]
    media = round(total/6, 2)
    percentual(num, per, total)

    arquivo2 = open('relatório.txt', 'w')
    arquivo2.write("ACME Inc.            Uso do espaço em disco pelos usuários\n")
    arquivo2.write("----------------------------------------------------------\n")
    arquivo2.write("Nr.     Usuário       Espaço utilizado    % do uso\n")
    for i in range(0, 6):
        arquivo2.write(str(i))
        arquivo2.write("\t")
        for a in range(0, 6):
            if(a==i):
                arquivo2.write(linhas[a])
                arquivo2.write("\t")
            for b in range(0,6):
                if(b==i and b==a):
                    arquivo2.write(str(num[b]))
                    arquivo2.write("MB   \t")
                for c in range(0,6):
                    if(c==i and c==b and c ==a):
                        arquivo2.write(str(per[c]))
                        arquivo2.write("%\t\n")
        arquivo2.write("\n")
        
    arquivo2.write("Espaço total ocupado:" + str(total))
    arquivo2.write("\nEspaço médio ocupado:"+ str(media))

main()
