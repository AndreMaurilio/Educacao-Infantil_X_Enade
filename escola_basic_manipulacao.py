import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_rows = 80
pd.options.display.max_columns = 90




def flutuante(x):
    if (x == ''):
        return 0
    else:
        return float(x)


# ESCOLA
infantil = 0
primario = 0
transpF = 0
transpP = 0
transfT = 0
cidade = 0

codigo_cid = []
estado_list = []
cidades_list = []
creche_list = []
infantil_list = []
primario_list = []
transpCrec_list = []
transpF_list = []
transpP_list = []
transpTT_list = []
nao_achados = 0
nao_achados_list = []


wrt2018 = open(
    r"C:\\Users\\André\\CursoPyLadiesSP-master\\TRABALHO\\Educacao-Infantil_X_Enade\\escola-2018.txt")

saeb2017 = open(
    r"C:\\Users\\André\\CursoPyLadiesSP-master\\TRABALHO\\Educacao-Infantil_X_Enade\\saeb-2017.csv")


# RASPAGEM ESCOLA
for campos in wrt2018:
    campos = campos.split(";")
    codigo_cid.append(campos[0])
    cidades_list.append(campos[1])
    estado_list.append((campos[2]))
    creche_list.append((campos[3]))
    infantil_list.append(campos[4])
    primario_list.append(campos[5])
    transpCrec_list.append((campos[6]))
    transpF_list.append(campos[7])
    transpP_list.append(campos[8])
    transpTT_list.append(campos[9][:-1])
wrt2018.close()


# SAEB

escola_qtd = [0] * len(codigo_cid)
pes_port = [0] * len(codigo_cid)
pro_port = [0] * len(codigo_cid)
pro_port_saeb = [0] * len(codigo_cid)
pes_mat = [0] * len(codigo_cid)
pro_mat = [0] * len(codigo_cid)
pro_mat_saeb = [0] * len(codigo_cid)
escola_qtd = [0] * len(codigo_cid)
qtd_alunos = [0] * len(codigo_cid)
creche = [0] * len(codigo_cid)
primario = [0] * len(codigo_cid)
preescola = [0] * len(codigo_cid)
# RAPAGEM SAEB
divisor = 0
for notas in saeb2017:
    notas = notas.split(";")
    if notas[0] in codigo_cid:
        qtd_alunos[codigo_cid.index(notas[0])] += flutuante(notas[1])  
        pro_port_saeb[codigo_cid.index(notas[0])] += flutuante(notas[2])  
        pro_mat_saeb[codigo_cid.index(notas[0])] += flutuante(notas[3])
        creche [codigo_cid.index(notas[0])] += flutuante(notas[4])
        preescola[codigo_cid.index(notas[0])] += flutuante(notas[5])
        primario[codigo_cid.index(notas[0])] += flutuante(notas[6])
    else:
        nao_achados += 1
        nao_achados_list.append(notas[0])


saeb2017.close()

# DATAFRAME DE ESCOLA
df = pd.DataFrame({
    'Cidades': cidades_list,
    'Estado': estado_list,
    'Alunos Creeches': creche_list,
    'Alunos Infantil': infantil_list,
    'Alunos Primario': primario_list,
    'Transporte p/ creche': transpCrec_list,
    'Transporte p/ infantil': transpF_list,
    'Transporte p/ primario': transpP_list,
    'Transporte p/ total': transpTT_list,

})

# SAEB
dfs = pd.DataFrame({
    'Cidade:': cidades_list,
    'Estado': estado_list,
    'QTD/Alunos': qtd_alunos,
    'Proeficiencia Portugues/SAEB': pro_port_saeb ,
    'Proeficiencia Matematica/SAEB': pro_mat_saeb ,
    'Creche':creche,
    'Preescola':preescola,
    'Primario':primario
})


df.head(15)
dfs.head(15)
# print(df.loc[df['Cidades'] == 'SAO JOSE DOS CAMPOS'])
# print(df.sample(10))

print("----------------COMECA SAEB ----------------"+"\n")
# print(dfs.loc[dfs['Estado'] == 'MG'])
print(dfs.describe())




# plt.bar(cidades_list, pro_mat_saeb)
# plt.show()

if(nao_achados > 0):
    print(nao_achados)
