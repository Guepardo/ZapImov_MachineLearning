# ZapImov_MachineLearning
##Limpeza dos dados

```python
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
```


```python
df.tail(2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
      <th>sector</th>
      <th>street</th>
      <th>city</th>
      <th>type</th>
      <th>room</th>
      <th>suite</th>
      <th>park</th>
      <th>m2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12771</th>
      <td>R$ 177.000</td>
      <td>Vila Alpes</td>
      <td>Avenida Alpes,Dos</td>
      <td>Goiania GO</td>
      <td>Apartamento</td>
      <td>2 quartos |</td>
      <td>1 suíte |</td>
      <td>1 vaga |</td>
      <td>56m2</td>
    </tr>
    <tr>
      <th>12772</th>
      <td>R$ 190.000</td>
      <td>SETOR BUENO</td>
      <td>Avenida T 2</td>
      <td>Goiania GO</td>
      <td>Conjunto Comercial/Sala</td>
      <td>25m2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>




```python
df['sector'].tail(5)
```




    12768         Jardim América
    12769    ALPHAVILLE CRUZEIRO
    12770         Brisas da Mata
    12771             Vila Alpes
    12772            SETOR BUENO
    Name: sector, dtype: object




```python
df[df.sector == 'SETOR BUENO'].describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
      <th>sector</th>
      <th>street</th>
      <th>city</th>
      <th>type</th>
      <th>room</th>
      <th>suite</th>
      <th>park</th>
      <th>m2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2286</td>
      <td>2286</td>
      <td>2286</td>
      <td>2286</td>
      <td>2286</td>
      <td>2286</td>
      <td>2286</td>
      <td>2286</td>
      <td>2286</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>410</td>
      <td>1</td>
      <td>152</td>
      <td>1</td>
      <td>15</td>
      <td>40</td>
      <td>51</td>
      <td>71</td>
      <td>225</td>
    </tr>
    <tr>
      <th>top</th>
      <td>Sob consulta</td>
      <td>SETOR BUENO</td>
      <td></td>
      <td>Goiania GO</td>
      <td>Apartamento</td>
      <td>3 quartos |</td>
      <td>3 suítes |</td>
      <td>2 vagas |</td>
      <td></td>
    </tr>
    <tr>
      <th>freq</th>
      <td>690</td>
      <td>2286</td>
      <td>187</td>
      <td>2286</td>
      <td>1443</td>
      <td>860</td>
      <td>663</td>
      <td>823</td>
      <td>365</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['room'].head()
```




    0        4 quartos | 
    1    2 a 4 quartos | 
    2        2 quartos | 
    3           29 a 65m2
    4        4 quartos | 
    Name: room, dtype: object




```python
#Removendo os valores que faziam referência ao metro quadrado e não a quantidade de quartos. 
```


```python
df['room'] = df['room'].apply(lambda row: row.replace('quartos','').replace('|','').strip())

```


```python
df['room'] = df['room'].apply(lambda row: row if len(row) == 1 else '')
```


```python
df['room'].tail(10)
```




    12763    2
    12764    2
    12765     
    12766    3
    12767    4
    12768    2
    12769    4
    12770    2
    12771    2
    12772     
    Name: room, dtype: object




```python
#Removendo caracteres da coluna de suite
```


```python
df['suite'].tail(5)
```




    12768     1 suíte | 
    12769    4 suítes | 
    12770          100m2
    12771     1 suíte | 
    12772               
    Name: suite, dtype: object




```python
df['suite'] = df['suite'].apply(lambda row: row.replace('suítes','').replace('suíte','').replace('|','').replace('vagas','').strip())
```


```python
df['suite'] = df['suite'].apply(lambda row: row if len(str(row)) == 1 else '')
```


```python
df['suite'].tail(5)
```




    12768    1
    12769    4
    12770     
    12771    1
    12772     
    Name: suite, dtype: object




```python
#Normalizando os valores dos imóveis
```


```python
df['price'].tail(10)
```




    12763      R$ 142.770
    12764      R$ 170.000
    12765      R$ 210.195
    12766    R$ 1.800.000
    12767    R$ 2.900.000
    12768      R$ 230.000
    12769    R$ 2.950.000
    12770      R$ 170.000
    12771      R$ 177.000
    12772      R$ 190.000
    Name: price, dtype: object




```python
df['price'] = df['price'].apply(lambda row: row.replace('R$', '').strip())
```


```python
index = 0
while index < len(df['price']): 
    
    if not df['price'][index].replace('.','').isdigit():
        df['price'][index] = ''
    
    index += 1
```


```python
df['price'].tail(10)
```




    12763      142.770
    12764      170.000
    12765      210.195
    12766    1.800.000
    12767    2.900.000
    12768      230.000
    12769    2.950.000
    12770      170.000
    12771      177.000
    12772      190.000
    Name: price, dtype: object




```python
#Normalizando o campo de metros quadrados
```


```python
df['m2'].tail(10)
```




    12763        
    12764        
    12765        
    12766        
    12767        
    12768    65m2
    12769        
    12770        
    12771    56m2
    12772        
    Name: m2, dtype: object




```python
df['m2'] = df['m2'].apply(lambda row: row.replace('m2', '').strip())
```


```python
index = 0
while index < len(df['m2']): 
    temp = df['m2'][index].split('a')
    
    if len(temp) > 1: 
        var1 = int(temp[0])
        var2 = int(temp[1])
        
        df['m2'][index] = str((var1 + var2) / 2)
        
        
    index += 1
```


```python
df['m2'].tail(10)
```




    12763      
    12764      
    12765      
    12766      
    12767      
    12768    65
    12769      
    12770      
    12771    56
    12772      
    Name: m2, dtype: object




```python
#limpando dados para as vagas
```


```python
df['park'].tail(10)
```




    12763          50m2
    12764          64m2
    12765              
    12766         320m2
    12767         451m2
    12768    2 vagas | 
    12769         466m2
    12770              
    12771     1 vaga | 
    12772              
    Name: park, dtype: object




```python
df['park'] = df['park'].apply(lambda row: row.replace('vagas', '').replace('vaga', '').replace('|','').strip())
```


```python
df['park'] = df['park'].apply(lambda row: row if len(str(row)) == 1 else '')
```


```python
df['park'].tail(10)
```




    12763     
    12764     
    12765     
    12766     
    12767     
    12768    2
    12769     
    12770     
    12771    1
    12772     
    Name: park, dtype: object




```python
#Tratando Strings
```


```python
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
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
      <th>sector</th>
      <th>street</th>
      <th>city</th>
      <th>type</th>
      <th>room</th>
      <th>suite</th>
      <th>park</th>
      <th>m2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>669.000</td>
      <td>JD GOIAS</td>
      <td>RUA 46</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>121</td>
    </tr>
    <tr>
      <th>4</th>
      <td>480.000</td>
      <td>JD GOIAS</td>
      <td>RUA 54</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>119</td>
    </tr>
    <tr>
      <th>8</th>
      <td>240.000</td>
      <td>SETOR BUENO</td>
      <td>RUA T 64</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>80</td>
    </tr>
    <tr>
      <th>9</th>
      <td>215.000</td>
      <td>JARDIM ATLÂNTICO</td>
      <td>RUA CHARITA,DA</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>58</td>
    </tr>
    <tr>
      <th>10</th>
      <td>600.000</td>
      <td>SETOR BUENO</td>
      <td>AVENIDA T 15</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>183</td>
    </tr>
    <tr>
      <th>11</th>
      <td>170.000</td>
      <td>RESID ELI FORTE</td>
      <td>RUA DIVA FORTES</td>
      <td>Goiania GO</td>
      <td>CASA</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>12</th>
      <td>350.000</td>
      <td>SETOR PEDRO LUDOVICO</td>
      <td>ALAMEDA COUTO MAGALHAES</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>80</td>
    </tr>
    <tr>
      <th>14</th>
      <td>445.000</td>
      <td>SETOR MARISTA</td>
      <td>AVENIDA 136</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>158</td>
    </tr>
    <tr>
      <th>17</th>
      <td>285.000</td>
      <td>JARDIM AMÉRICA</td>
      <td>RUA C 180</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>85</td>
    </tr>
    <tr>
      <th>19</th>
      <td>260.000</td>
      <td>JARDIM AMÉRICA</td>
      <td>RUA C 131</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>82</td>
    </tr>
    <tr>
      <th>20</th>
      <td>275.000</td>
      <td>VILA JARAGUÁ</td>
      <td>RUA 230</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>71</td>
    </tr>
    <tr>
      <th>22</th>
      <td>299.000</td>
      <td>JARDIM ATLÂNTICO</td>
      <td>RUA RAIA,DA</td>
      <td>Goiania GO</td>
      <td>CASA</td>
      <td>3</td>
      <td>2</td>
      <td>4</td>
      <td>150</td>
    </tr>
    <tr>
      <th>23</th>
      <td>250.000</td>
      <td>SETOR CENTRAL</td>
      <td>AVENIDA ARAGUAIA</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>141</td>
    </tr>
    <tr>
      <th>28</th>
      <td>310.000</td>
      <td>SETOR LESTE UNIVERSITARIO</td>
      <td>RUA 257</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>70</td>
    </tr>
    <tr>
      <th>29</th>
      <td>700.000</td>
      <td>SETOR SUL</td>
      <td>RUA 88 C</td>
      <td>Goiania GO</td>
      <td>CASA</td>
      <td>6</td>
      <td>1</td>
      <td>2</td>
      <td>365</td>
    </tr>
    <tr>
      <th>30</th>
      <td>159.900</td>
      <td>RESID ITAIPU</td>
      <td>RUA RI 10</td>
      <td>Goiania GO</td>
      <td>CASA</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>100</td>
    </tr>
    <tr>
      <th>31</th>
      <td>293.000</td>
      <td>JD GUANABARA II</td>
      <td>RUA GB 8</td>
      <td>Goiania GO</td>
      <td>CASA DE CONDOMÍNIO</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>75</td>
    </tr>
    <tr>
      <th>33</th>
      <td>750.000</td>
      <td>SETOR BUENO</td>
      <td>AV.T5</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>298</td>
    </tr>
    <tr>
      <th>34</th>
      <td>330.000</td>
      <td>SETOR SUL</td>
      <td>RUA 90</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>108</td>
    </tr>
    <tr>
      <th>37</th>
      <td>290.000</td>
      <td>SETOR PEDRO LUDOVICO</td>
      <td>ALAMEDA COUTO MAGALHAES</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>67</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.to_csv('C:\\Users\\bsine\\Desktop\\data.csv', sep='\t')
```
## Rotulação de dados



```python
import pandas as pd

path = 'C:\\Users\\bsine\\Desktop\\'

df = pd.DataFrame.from_csv(path = path+'data.csv' , sep = '\t')
```


```python
df.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
      <th>sector</th>
      <th>street</th>
      <th>city</th>
      <th>type</th>
      <th>room</th>
      <th>suite</th>
      <th>park</th>
      <th>m2</th>
    </tr>
    <tr>
      <th>﻿</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>669.000</td>
      <td>JD GOIAS</td>
      <td>RUA 46</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>121</td>
    </tr>
    <tr>
      <th>4</th>
      <td>480.000</td>
      <td>JD GOIAS</td>
      <td>RUA 54</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>119</td>
    </tr>
    <tr>
      <th>8</th>
      <td>240.000</td>
      <td>SETOR BUENO</td>
      <td>RUA T 64</td>
      <td>Goiania GO</td>
      <td>APARTAMENTO</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Retirando a coluna 'city': 
df.columns
```




    Index(['price', 'sector', 'street', 'city', 'type', 'room', 'suite', 'park',
           'm2'],
          dtype='object')




```python
del df['city']
```


```python
df.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
      <th>sector</th>
      <th>street</th>
      <th>type</th>
      <th>room</th>
      <th>suite</th>
      <th>park</th>
      <th>m2</th>
    </tr>
    <tr>
      <th>﻿</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>669.000</td>
      <td>JD GOIAS</td>
      <td>RUA 46</td>
      <td>APARTAMENTO</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>121</td>
    </tr>
    <tr>
      <th>4</th>
      <td>480.000</td>
      <td>JD GOIAS</td>
      <td>RUA 54</td>
      <td>APARTAMENTO</td>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>119</td>
    </tr>
    <tr>
      <th>8</th>
      <td>240.000</td>
      <td>SETOR BUENO</td>
      <td>RUA T 64</td>
      <td>APARTAMENTO</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Selecionando todos os nomes de setores. 
#Tentativa com drop_duplicates()
uniques_drop = df.sector.drop_duplicates()
uniques_drop[0:10]
```




    ﻿
    0                      JD GOIAS
    8                   SETOR BUENO
    9              JARDIM ATLÂNTICO
    11              RESID ELI FORTE
    12         SETOR PEDRO LUDOVICO
    14                SETOR MARISTA
    17               JARDIM AMÉRICA
    20                 VILA JARAGUÁ
    23                SETOR CENTRAL
    28    SETOR LESTE UNIVERSITARIO
    Name: sector, dtype: object




```python
uniques_drop.count()
```




    298




```python
#Selecionando todos os nomes de setores. 
#Tentativa com unique
uniques_sector = df.sector.unique()
uniques_sector[0:10]
```




    array(['JD GOIAS', 'SETOR BUENO', 'JARDIM ATLÂNTICO', 'RESID ELI FORTE',
           'SETOR PEDRO LUDOVICO', 'SETOR MARISTA', 'JARDIM AMÉRICA',
           'VILA JARAGUÁ', 'SETOR CENTRAL', 'SETOR LESTE UNIVERSITARIO'], dtype=object)




```python
len(uniques_sector)
```




    298




```python
#Aparentemente os dois tem o mesmo resultado. 
```


```python
#Criando dicionário para setores: 
sector_dic = {}

#Cada label de setor deve representar um número inteiro neste momento: 
index = 0
for label_sector in uniques_sector: 
    sector_dic[label_sector] = index
    index += 1
    

```


```python
#Substituir labels no data set pelo index
df['sector'] = df['sector'].apply(lambda x : sector_dic[str(x)])
df.tail(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
      <th>sector</th>
      <th>street</th>
      <th>type</th>
      <th>room</th>
      <th>suite</th>
      <th>park</th>
      <th>m2</th>
    </tr>
    <tr>
      <th>﻿</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12761</th>
      <td>1.580.000</td>
      <td>1</td>
      <td>RUA T 34</td>
      <td>APARTAMENTO</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
      <td>236</td>
    </tr>
    <tr>
      <th>12768</th>
      <td>230.000</td>
      <td>6</td>
      <td>AVENIDA C 4</td>
      <td>APARTAMENTO</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>65</td>
    </tr>
    <tr>
      <th>12771</th>
      <td>177.000</td>
      <td>33</td>
      <td>AVENIDA ALPES,DOS</td>
      <td>APARTAMENTO</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>56</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Selecionando os tipos únicos 
uniques_street = df.street.unique()
uniques_street[0:10]
```




    array(['RUA 46', 'RUA 54', 'RUA T 64', 'RUA CHARITA,DA', 'AVENIDA T 15',
           'RUA DIVA FORTES', 'ALAMEDA COUTO MAGALHAES', 'AVENIDA 136',
           'RUA C 180', 'RUA C 131'], dtype=object)




```python
len(uniques_street)
```




    1477




```python
#Criando dicionário para streets: 
street_dic = {}

#Cada label de setor deve representar um número inteiro neste momento: 
index = 0
for label_street in uniques_street: 
    street_dic[label_street] = index
    index += 1
    
```


```python
#Substituir labels no data set pelo index
df['street'] = df['street'].apply(lambda x : street_dic[str(x)])
df.tail(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
      <th>sector</th>
      <th>street</th>
      <th>type</th>
      <th>room</th>
      <th>suite</th>
      <th>park</th>
      <th>m2</th>
    </tr>
    <tr>
      <th>﻿</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12761</th>
      <td>1.580.000</td>
      <td>1</td>
      <td>75</td>
      <td>APARTAMENTO</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
      <td>236</td>
    </tr>
    <tr>
      <th>12768</th>
      <td>230.000</td>
      <td>6</td>
      <td>137</td>
      <td>APARTAMENTO</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>65</td>
    </tr>
    <tr>
      <th>12771</th>
      <td>177.000</td>
      <td>33</td>
      <td>428</td>
      <td>APARTAMENTO</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>56</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Selecionando todos os nomes de type. 
uniques_type = df.type.unique()
uniques_type[0:10]
```




    array(['APARTAMENTO', 'CASA', 'CASA DE CONDOMÍNIO', 'QUITINETE',
           'CASA COMERCIAL', 'FLAT', 'CASA DE VILA', 'CHÁCARA', 'LOFT',
           'TERRENO PADRÃO'], dtype=object)




```python
len(uniques_type)
```




    13




```python
#Criando dicionário para types: 
type_dic = {}

#Cada label de setor deve representar um número inteiro neste momento: 
index = 0
for label_type in uniques_type: 
    type_dic[label_type] = index
    index += 1
    
```


```python
#Substituir labels no data set pelo index
df['type'] = df['type'].apply(lambda x : type_dic[str(x)])
df.tail(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
      <th>sector</th>
      <th>street</th>
      <th>type</th>
      <th>room</th>
      <th>suite</th>
      <th>park</th>
      <th>m2</th>
    </tr>
    <tr>
      <th>﻿</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12761</th>
      <td>1.580.000</td>
      <td>1</td>
      <td>75</td>
      <td>0</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
      <td>236</td>
    </tr>
    <tr>
      <th>12768</th>
      <td>230.000</td>
      <td>6</td>
      <td>137</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>65</td>
    </tr>
    <tr>
      <th>12771</th>
      <td>177.000</td>
      <td>33</td>
      <td>428</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>56</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Convertendo dicionários para dataframe: 
#sector_dic
#street_dic
#type_dic
```


```python
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
```


```python
#Armazenando dados em disco para consulta posterior: 
df_sector.to_csv(path+'sector_reference.csv', sep='\t')
df_street.to_csv(path+'street_reference.csv', sep='\t')
df_type.to_csv(path+'type_reference.csv', sep='\t')

df.to_csv(path+'data_to_learn.csv', sep='\t')
```


```python

```
