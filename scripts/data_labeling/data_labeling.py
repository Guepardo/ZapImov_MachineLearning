
# coding: utf-8

# In[214]:

import pandas as pd

path = 'C:\\Users\\bsine\\Desktop\\'

df = pd.DataFrame.from_csv(path = path+'data.csv' , sep = '\t')


# In[215]:

df.head(3)


# In[216]:

#Retirando a coluna 'city': 
df.columns


# In[217]:

del df['city']


# In[218]:

df.head(3)


# In[219]:

#Selecionando todos os nomes de setores. 
#Tentativa com drop_duplicates()
uniques_drop = df.sector.drop_duplicates()
uniques_drop[0:10]


# In[220]:

uniques_drop.count()


# In[221]:

#Selecionando todos os nomes de setores. 
#Tentativa com unique
uniques_sector = df.sector.unique()
uniques_sector[0:10]


# In[222]:

len(uniques_sector)


# In[223]:

#Aparentemente os dois tem o mesmo resultado. 


# In[224]:

#Criando dicionário para setores: 
sector_dic = {}

#Cada label de setor deve representar um número inteiro neste momento: 
index = 0
for label_sector in uniques_sector: 
    sector_dic[label_sector] = index
    index += 1
    


# In[225]:

#Substituir labels no data set pelo index
df['sector'] = df['sector'].apply(lambda x : sector_dic[str(x)])
df.tail(3)


# In[226]:

#Selecionando os tipos únicos 
uniques_street = df.street.unique()
uniques_street[0:10]


# In[227]:

len(uniques_street)


# In[228]:

#Criando dicionário para streets: 
street_dic = {}

#Cada label de setor deve representar um número inteiro neste momento: 
index = 0
for label_street in uniques_street: 
    street_dic[label_street] = index
    index += 1
    


# In[229]:

#Substituir labels no data set pelo index
df['street'] = df['street'].apply(lambda x : street_dic[str(x)])
df.tail(3)


# In[230]:

#Selecionando todos os nomes de type. 
uniques_type = df.type.unique()
uniques_type[0:10]


# In[231]:

len(uniques_type)


# In[232]:

#Criando dicionário para types: 
type_dic = {}

#Cada label de setor deve representar um número inteiro neste momento: 
index = 0
for label_type in uniques_type: 
    type_dic[label_type] = index
    index += 1
    


# In[233]:

#Substituir labels no data set pelo index
df['type'] = df['type'].apply(lambda x : type_dic[str(x)])
df.tail(3)


# In[234]:

#Convertendo dicionários para dataframe: 
#sector_dic
#street_dic
#type_dic


# In[235]:

sector_array = []
for key in sector_dic: 
    sector_array.append([sector_dic[key], key])

df_sector = pd.DataFrame(data= sector_array, columns= ['id','label'])

street_array = []
for key in street_dic: 
    street_array.append([street_dic[key], key])

df_street = pd.DataFrame(data= street_array, columns= ['id','label'])

type_array = []
for key in type_dic: 
    type_array.append([type_dic[key], key])
    
df_type =  pd.DataFrame(data= type_array, columns= ['id','label'])


# In[236]:

#Armazenando dados em disco para consulta posterior: 
df_sector.to_csv(path+'sector_reference.csv', sep='\t')
df_street.to_csv(path+'street_reference.csv', sep='\t')
df_type.to_csv(path+'type_reference.csv', sep='\t')

df.to_csv(path+'data_to_learn.csv', sep='\t')


# In[ ]:



