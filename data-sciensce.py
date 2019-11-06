f = open(r"C:\Users\André\CursoPyLadiesSP-master\microdados_ed_superior_2018\dados\DM_CURSO.CSV")
curso = []
vagas = []
inscritos = []
cont = 0

for campos in f:
    campos = campos.split("|")
    if campos[9] not in curso:
        curso.append(campos[9])
        vagas.append(campos[110])
        inscritos.append(campos[111])


wrt = open(
    "C:\\Users\\André\\CursoPyLadiesSP-master\\TRABALHO\\CURSOS.txt", "w")
for s in curso:
    wrt.writelines(
        s+" vagas= " + str(vagas[cont]) + " incritos = " + str(inscritos[cont]) + "\n")
    cont += 1
wrt.close()
