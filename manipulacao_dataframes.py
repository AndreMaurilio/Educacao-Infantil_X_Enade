import pandas as pd

df = pd.read_csv(r"C:\\Users\\André\\CursoPyLadiesSP-master\\TRABALHO\\micro_censo_escolar_2016\\DADOS\\MATRICULA_SUDESTE.CSV", delimiter='|',
                 encoding='iso-8859-1', usecols=['CO_MUNICIPIO', 'NU_IDADE_REFERENCIA'])
idades =[]
cidades_total=[]
creche=[]
infantil=[]
primario=[]
cidades=[]

idades = df['NU_IDADE_REFERENCIA']
cidades_total = df['CO_MUNICIPIO']
cont = 0

for i in cidades_total:
    if i not in cidades:
        cidades.append(i)
        infantil.append(0)
        primario.append(0)
        creche.append(0)

    if idades[cont] == '5':
         infantil[cidades.index(i)] += 1
    elif idades[cont] == '7':
            primario[cidades.index(i)] += 1
    elif idades[cont] =='2':
            creche[cidades.index(i)] += 1
    cont+=1
    
df2 = pd.DataFrame({
    'Cidade':cidades,
    'Creche':creche,
    'Infantil':infantil,
    'Primario': primario,

})


df2.sample(10)
