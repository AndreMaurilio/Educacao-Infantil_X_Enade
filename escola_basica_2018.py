import pandas as pd
import matplotlib.pyplot as plt


dados = open(
    r"C:\Users\André\CursoPyLadiesSP-master\TRABALHO\\Educacao-Infantil_X_Enade\\city.CSV")
situacao_de_funcionamento = {'Em Atividade': 0, 'Paralisada': 0,
                             'Extinta no Ano do Censo': 0, 'Extinta em Anos Anteriores': 0}
cidade = []
creche = []
infantil = []
primario = []
transportInf = []
transportPrim = []
transpotCrec = []

with open(r"C:\\Users\\André\\CursoPyLadiesSP-master\\TRABALHO\\microdados_ed_basica_2018\\DADOS\\MATRICULA_SUDESTE.CSV") as f:
    next(f)
    for campos in f:
        campos = campos.split("|")
        if campos[77] not in cidade:
            cidade.append(campos[77])
            creche.append(0)
            infantil.append(0)
            primario.append(0)
            transportInf.append(0)
            transportPrim.append(0)
            transpotCrec.append(0)
        if campos[6] == '5':
            infantil[cidade.index(campos[77])] += 1
            if campos[24] == '1':
                transportInf[cidade.index(campos[77])] += 1
        elif campos[6] == '7':
            primario[cidade.index(campos[77])] += 1
            if campos[24] == '1':
                transportPrim[cidade.index(campos[77])] += 1
        elif campos[6] == '2':
            creche[cidade.index(campos[77])] += 1
            if campos[24] == '1':
                transpotCrec[cidade.index(campos[77])] += 1

cidade_n = ["N/D"] * len(cidade)
estado_n = ["N/D"] * len(cidade)
for nome in dados:
    nome = nome.split(";")
    if(nome[0] in cidade):
        cidade_n[cidade.index(nome[0])] = nome[1]
        estado_n[cidade.index(nome[0])] = nome[2]


wrt2018 = open(
    "C:\\Users\\André\\CursoPyLadiesSP-master\\TRABALHO\\Educacao-Infantil_X_Enade\\escola-2018.txt", "w")
cont = 0
for s in cidade:
    linha = s + ";" + cidade_n[cont] + ";" + estado_n[cont][:2] + ";" + str(creche[cont])+";" + str(infantil[cont]) + ";" + str(primario[cont]) + ";"+str(
        transpotCrec[cont])+";"+str(transportInf[cont])+";" + str(transportPrim[cont]) + ";" + str(transpotCrec[cont]+transportInf[cont]+transportPrim[cont]) + "\n"
    wrt2018.writelines(linha)
    cont += 1
wrt2018.close()
