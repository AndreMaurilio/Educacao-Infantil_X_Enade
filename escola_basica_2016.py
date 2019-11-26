import pandas as pd
import matplotlib.pyplot as plt

# -----------ABRE E LE ARQUIVO COM NOMES DAS CIDADES E ESTADOS----------
dados = open(
    r"C:\Users\André\CursoPyLadiesSP-master\TRABALHO\\Educacao-Infantil_X_Enade\\city.CSV")

cidade = []
creche = []
infantil = []
primario = []
transportInf = []
transportPrim = []
transpotCrec = []

with open(r"C:\\Users\\André\\CursoPyLadiesSP-master\\TRABALHO\\micro_censo_escolar_2016\\DADOS\\MATRICULA_SUDESTE.CSV") as f:
    next(f)
    for campos in f:
        campos = campos.split("|")
        # SE A CIDADE AINDA NÃO FOI ADICIONADA A LISTA, ADICIONO ELA E INICIALIZO OS CAMPOS QUE ESTÃO NA MESMA LINHA
        if campos[77] not in cidade:
            cidade.append(campos[77])
            creche.append(0)
            infantil.append(0)
            primario.append(0)
            transportInf.append(0)
            transportPrim.append(0)
            transpotCrec.append(0)
        # ----- VERIFICA QUAL A IDADE DO ALUNO E INCREMENTA O CAMPO CORRETO
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

# INICIALIZO OS ARRAYS COM O TAMANHO DO ARRAY DO CODIGO DE CIDADE, ELE FUNCIONARA COMO UM 'PK', ASSIM SUA POSIÇÃO NO INDICE 
# VINCULARÁ ELE AO NOME DA CIDADE E DO ESTADO.
cidade_n = ["N/D"] * len(cidade)
estado_n = ["N/D"] * len(cidade)
for nome in dados:
    nome = nome.split(";")
    if(nome[0] in cidade):
        cidade_n[cidade.index(nome[0])] = nome[1]
        estado_n[cidade.index(nome[0])] = nome[2]


wrt2016 = open(
    "C:\\Users\\André\\CursoPyLadiesSP-master\\TRABALHO\\Educacao-Infantil_X_Enade\\escola_2016.txt", "w")
cont = 0
for s in cidade:
    # ESCREVE: CODIGO DA CIDADE,NOME DA CIDADE,ESTADO,ALUNOS NA CRECHE,AL NO INFANTIL, AL NO PRIMARIO, TRANSPORTE P CRECHE,T. P INFANTI, T. P PRIMARIO,T TOTAL
    linha = s + ";" + cidade_n[cont] + ";" + estado_n[cont][:2] + ";" + str(creche[cont])+";" + str(infantil[cont]) + ";" + str(primario[cont]) + ";"+str(
        transpotCrec[cont])+";"+str(transportInf[cont])+";" + str(transportPrim[cont]) + ";" + str(transpotCrec[cont]+transportInf[cont]+transportPrim[cont]) + "\n"
    wrt2016.writelines(linha)
    cont += 1
wrt2016.close()
