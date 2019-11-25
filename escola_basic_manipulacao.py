import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_rows = 80
pd.options.display.max_columns = 90

plt.locator_params(axis='y', nbins=6)
plt.locator_params(axis='x', nbins=10)


def flutuante(x):
    if (x == ''):
        return 0
    else:
        return float(x)


def porcentagem_trans(df):
    df2 = df.copy()
    for Group in ['Transporte p/ creche', 'Transporte p/ infantil', 'Transporte p/ primario']:
        df2[Group] = round(df[Group]/df['Transporte p/ total']*100,0)
    return df2


# ------------------------------------------------- ESCOLA-----------------------------
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
porc_creche = []
porc_infantil=[]


wrt2016 = open(
    r"C:\\Users\\André\\CursoPyLadiesSP-master\\TRABALHO\\Educacao-Infantil_X_Enade\\escola-2016.txt")

saeb2017 = open(
    r"C:\\Users\\André\\CursoPyLadiesSP-master\\TRABALHO\\Educacao-Infantil_X_Enade\\saeb-2017.csv")


# ---------------------------------------------RASPAGEM ESCOLA-----------------------------------
for campos in wrt2016:
    campos = campos.split(";")
    codigo_cid.append(campos[0])
    cidades_list.append(campos[1])
    estado_list.append((campos[2]))
    creche_list.append((campos[3]))
    infantil_list.append(campos[4])
    primario_list.append(campos[5])
    porc_creche.append(100 if int(campos[3])/int(campos[5])*100 > 100 else int(campos[3])/int(campos[5])*100)
    porc_infantil.append(100 if int(
        campos[4])/int(campos[5])*100 > 100 else int(campos[4])/int(campos[5])*100)
    transpCrec_list.append(int(campos[6]))
    transpF_list.append(int(campos[7]))
    transpP_list.append(int(campos[8]))
    transpTT_list.append(int(campos[9][:-1]))
wrt2016.close()


# ---------------------------------- SAEB----------------------

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


# --------------------------------RAPAGEM SAEB----------------------
divisor = 0
for notas in saeb2017:
    notas = notas.split(";")
    if notas[0] in codigo_cid:
        qtd_alunos[codigo_cid.index(notas[0])] += flutuante(notas[1])
        pro_port_saeb[codigo_cid.index(notas[0])] += flutuante(notas[2])
        pro_mat_saeb[codigo_cid.index(notas[0])] += flutuante(notas[3])
        creche[codigo_cid.index(notas[0])] += flutuante(notas[4])
        preescola[codigo_cid.index(notas[0])] += flutuante(notas[5])
        primario[codigo_cid.index(notas[0])] += flutuante(notas[6])
    else:
        nao_achados += 1
        nao_achados_list.append(notas[0])


saeb2017.close()

# ------------CRIAÇÃO DATAFRAME DE ESCOLA
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

# -----------CRIAÇÃO DATAFRAME SAEB
dfs = pd.DataFrame({
    'Cidade:': cidades_list,
    'Estado': estado_list,
    'QTD/Alunos': qtd_alunos,
    'Proeficiencia Portugues/SAEB': pro_port_saeb,
    'Proeficiencia Matematica/SAEB': pro_mat_saeb,
    'Creche': creche,
    'Preescola': preescola,
    'Primario': primario
})


dfF = pd.DataFrame({
    'Cidades': cidades_list,
    'Estado': estado_list,
    'Alunos na Creeches': creche_list,
    'Alunos no Infantil': infantil_list,
    'Alunos no Primario': primario_list,
    'Proef. Portugues/SAEB': pro_port_saeb,
    'Proef. Matematica/SAEB': pro_mat_saeb,
    'Porcentagem Creche x Inf': porc_infantil,
    'Porcentagem Creche x Prim': porc_creche
   
})





# --------------PRINT DATAFRAMES ESCOLA------------
df.head(15)
d = porcentagem_trans(df)
# print(df.loc[df['Cidades'] == 'SAO PAULO'])
# print(dfF.groupby(pd.cut(dfF['Alunos no Primario'],np.range()) TENTATIVA DE GROUP BY


# ---------------PRINT DATAFRAMES SAEB--------------------

print("----------------COMECA SAEB ----------------"+"\n")

dfF.head(15)
print(dfF.loc[dfF['Cidade:'] == 'SAO PAULO'])
# print(dfs.loc[dfs['Cidade:'] == 'SAO CAETANO DO SUL'])


# print(dfs.sample(10))


# ------- CRIAÇÃO DE GRAFICOS-------------------
array_1 = np.array(cidades_list)
array_2 = np.array(pro_mat_saeb)
plt.bar(array_1[:30], array_2[:30]) # delimito tamanho dos arrays para os 30 primeiros
plt.show()                          # exibe grafico

if(nao_achados > 0):
    print('nao achados = '+str(nao_achados))
