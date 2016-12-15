
# coding: utf-8

# In[2]:

#full path C:\Users\bsine\Desktop\ZapImov_DataScience\data\data_zap.txt
import ast
import pandas as pd

path = 'C:\\Users\\bsine\\Desktop\\data_zap.txt'

file = open(path, 'r', encoding='utf-8') 

array = []

for line in file.readlines(): 
	temp = ast.literal_eval(line); 
	
	temp_array = []

	temp_array.append(temp['price'])
	temp_array.append(temp['sector'])
	temp_array.append(temp['street'])
	temp_array.append(temp['city'])
	temp_array.append(temp['type'])
	temp_array.append(temp['room'])
	temp_array.append(temp['suite'])
	temp_array.append(temp['park'])
	temp_array.append(temp['m2'])

	array.append(temp_array)

names = ['price', 'sector', 'street', 'city', 'type', 'room', 'suite', 'park', 'm2']

df = pd.DataFrame(data= array, columns= names)


# In[3]:

df.tail(2)


# In[4]:

df['sector'].tail(5)


# In[5]:

df[df.sector == 'SETOR BUENO'].describe()


# In[6]:

df['room'].head()


# In[7]:

#Removendo os valores que faziam referência ao metro quadrado e não a quantidade de quartos. 


# In[8]:

df['room'] = df['room'].apply(lambda row: row.replace('quartos','').replace('|','').strip())


# In[9]:

df['room'] = df['room'].apply(lambda row: row if len(row) == 1 else '')


# In[10]:

df['room'].tail(10)


# In[11]:

#Removendo caracteres da coluna de suite


# In[12]:

df['suite'].tail(5)


# In[13]:

df['suite'] = df['suite'].apply(lambda row: row.replace('suítes','').replace('suíte','').replace('|','').replace('vagas','').strip())


# In[14]:

df['suite'] = df['suite'].apply(lambda row: row if len(str(row)) == 1 else '')


# In[15]:

df['suite'].tail(5)


# In[16]:

#Normalizando os valores dos imóveis


# In[17]:

df['price'].tail(10)


# In[18]:

df['price'] = df['price'].apply(lambda row: row.replace('R$', '').strip())


# In[19]:

index = 0
while index < len(df['price']): 
    
    if not df['price'][index].replace('.','').isdigit():
        df['price'][index] = ''
    
    index += 1


# In[20]:

df['price'].tail(10)


# In[21]:

#Normalizando o campo de metros quadrados


# In[22]:

df['m2'].tail(10)


# In[23]:

df['m2'] = df['m2'].apply(lambda row: row.replace('m2', '').strip())


# In[24]:

index = 0
while index < len(df['m2']): 
    temp = df['m2'][index].split('a')
    
    if len(temp) > 1: 
        var1 = int(temp[0])
        var2 = int(temp[1])
        
        df['m2'][index] = str((var1 + var2) / 2)
        
        
    index += 1


# In[25]:

df['m2'].tail(10)


# In[26]:

#limpando dados para as vagas


# In[27]:

df['park'].tail(10)


# In[28]:

df['park'] = df['park'].apply(lambda row: row.replace('vagas', '').replace('vaga', '').replace('|','').strip())


# In[29]:

df['park'] = df['park'].apply(lambda row: row if len(str(row)) == 1 else '')


# In[30]:

df['park'].tail(10)


# In[31]:

#Tratando Strings


# In[32]:

df['street'] = df['street'].apply(str.upper)
df['type']   = df['type'].apply(str.upper)
df['sector'] = df['sector'].apply(str.upper)

df['price']  = df['price'].apply(str.strip)
df['sector'] = df['sector'].apply(str.strip)
df['street'] = df['street'].apply(str.strip)
df['city']   = df['city'].apply(str.strip)
df['type']   = df['type'].apply(str.strip)
df['room']   = df['room'].apply(str.strip)
df['suite']  = df['suite'].apply(str.strip)
df['park']   = df['park'].apply(str.strip)
df['m2']     = df['m2'].apply(str.strip)

#['price', 'sector', 'street', 'city', 'type', 'room', 'suite', 'park', 'm2']


df = df[ df.price  != '']
df = df[ df.sector != '']
df = df[ df.street != '']
df = df[ df.city   != '']
df = df[ df.type   != '']
df = df[ df.room   != '']
df = df[ df.suite  != '']
df = df[ df.park   != '']
df = df[ df.m2     != '']

df.head(20)


# In[33]:

df.to_csv('C:\\Users\\bsine\\Desktop\\data.csv', sep='\t')

