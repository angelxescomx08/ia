# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 21:16:43 2022

@author: angel
"""

#Plantilla de preprocesado: datos categoricos
import numpy as np #numeros
import matplotlib.pyplot as plt #graficas
import pandas as pd #carga de datos

#importar el dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values #(filas,columnas)
y = dataset.iloc[:,3].values

#codificar datos categoricos (convertir las letras a numeros)
from sklearn import preprocessing
le_X = preprocessing.LabelEncoder()
X[:,0] = le_X.fit_transform(X[:,0])#transformar categorias a número y asignarlas a la matriz
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
 
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],   
    remainder='passthrough'                        
)
X = np.array(ct.fit_transform(X), dtype=np.float64)
le_y = preprocessing.LabelEncoder()
y = le_y.fit_transform(y)