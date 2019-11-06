
cidade_cod = []
escola_cod = []
pes_port = []
pro_port = []
pro_port_saeb = []
pes_mat = []
pro_mat = []
pro_mat_saeb = []
creches = []
preescola = []
primario = []
qt_aluno=[]
cont = 0
p = 0


def flutuante(x):
    if (x == ''):
        return 0
    else:
        return float(x)


f = open(r"C:\Users\André\CursoPyLadiesSP-master\TRABALHO\microdados_saeb_2017\DADOS\TS_ALUNO_9EF.csv")

for campos in f:
    campos = campos.split(',')
    if campos[2] == '35' or campos[2] == '33' or campos[2] == '32' or campos[2] == '31':
        if campos[3] not in cidade_cod:
            cidade_cod.append(campos[3])
            qt_aluno.append(0) 
            qt_aluno[cidade_cod.index(campos[3])] +=1
            pro_port_saeb.append(0)
            pro_port_saeb[cidade_cod.index(campos[3])] += flutuante(campos[29])
            pro_mat_saeb.append(0)
            pro_mat_saeb[cidade_cod.index(campos[3])] += flutuante(campos[33])
            creches.append(0)
            preescola.append(0)
            primario.append(0)
            if campos[82]=='A':
                creches[cidade_cod.index(campos[3])] += 1
            elif campos[82]=='B':
                preescola[cidade_cod.index(campos[3])] += 1
            elif campos[82]=='C':
                primario[cidade_cod.index(campos[3])] += 1

        elif campos[3] in cidade_cod:
            qt_aluno[cidade_cod.index(campos[3])] += 1    
            pro_port_saeb[cidade_cod.index(campos[3])] += flutuante(campos[29])    
            pro_mat_saeb[cidade_cod.index(campos[3])] += flutuante(campos[33])
            if campos[82]=='A':
                creches[cidade_cod.index(campos[3])] += 1
            elif campos[82]=='B':
                preescola[cidade_cod.index(campos[3])] += 1
            elif campos[82]=='C':
                primario[cidade_cod.index(campos[3])] += 1

print(len(cidade_cod))
saeb2017 = open(
    "C:\\Users\\André\\CursoPyLadiesSP-master\\TRABALHO\\Educacao-Infantil_X_Enade\\saeb-2017.csv", "w")
cont = 0
for s in cidade_cod: 
    saeb2017.writelines(s+';'+str(qt_aluno[cont])+';'
    +str(round((pro_port_saeb[cont]/qt_aluno[cont]), 2)) + ';'+str(round((pro_mat_saeb[cont]/qt_aluno[cont]), 2)) 
    + ';'+str(creches[cont])+';'+ str(preescola[cont])+';'+str(primario[cont])+"\n")
    cont +=1

saeb2017.close()
