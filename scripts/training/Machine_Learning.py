
# coding: utf-8

# In[27]:

import pandas as pd
from sklearn                  import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn                  import linear_model
from sklearn                  import metrics

path = 'C:\\Users\\bsine\\Desktop\\'

df = pd.DataFrame.from_csv(path = path+'data_to_learn.csv' , sep = '\t')


# In[28]:

#Coluna resultado
#df = df[df.sector == 8]

df['price'] = df['price'].apply(lambda x : x.replace('.', ''))
y = df['price'].apply(lambda x : x.replace('.', ''))
#Removendo coluna resultado do conjunto de treinamento
del df['price']


# In[29]:

X = df
X.tail(3)


# In[30]:

#Gerando conjuntos de treino e teste: 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0, random_state=33)


# In[31]:

#reduzindo escalas dos dados: 
scaler  = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)


# In[32]:

#Iniciando classificador linear: 
clf = linear_model.SGDClassifier(n_jobs=5)
clf.fit(X_train, y_train)


# In[33]:

#Valor idêntico
y_pred_train = clf.predict(X_train)
metrics.accuracy_score(y_train, y_pred_train) * 100


# In[41]:

#Isso significa que há apenas 1,4% de acerto de valores usando o próprio conjunto de treino.


# In[49]:

#Testando uma predição: 
#Ensaio do indice 12768
clf.predict(scaler.transform([[33, 428, 0, 2, 1, 1, 56]]))


# In[52]:

#valor real do ensaio
y[12768]


# In[53]:

def my_accuracy_score(amount=0, y_pred_train=[], y_train=[]):
    count = 0
    for x in range(len(y_pred_train)-1): 
        pred = float(y_pred_train[x].replace('.',''))
        test = float(y_train[x].replace('.',''))
        
        #print("Pred: %f Real: %f" % (pred, test) )
        if (test + amount) >= pred and (test - amount) <= pred:
            count += 1
    return count / len(y_pred_train)
        
    


# In[54]:

#valores com 1000 reais a mais ou a menos do real
my_accuracy_score(amount=1000, y_pred_train=y_pred_train, y_train=y_train.as_matrix()) * 100


# In[55]:

#valores com 10000 reais a mais ou a manos do real


# In[56]:

my_accuracy_score(amount=10000, y_pred_train=y_pred_train, y_train=y_train.as_matrix()) * 100


# In[61]:

#Veredito: 
#Com base nos testes acima, constatou-se que os dados são insuficientes para generalizar o modelo. 
#Em termos técnicos, há um underfitting no modelo e seria necessário mais dados para o treino.
#Conjunto total para treino: 
len(X)


# In[ ]:



