# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Plantilla de preprocesado
import numpy as np #numeros
import matplotlib.pyplot as plt #graficas
import pandas as pd #carga de datos

#importar el dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values #(filas,columnas)
y = dataset.iloc[:,3].values

#Tratamiento de Na's
from sklearn.impute import SimpleImputer
#Objeto para reemplazar valores indefinidos(Valores a reemplazar,forma de remplazarlos(media), filas o columnas(columnas))
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean", verbose = 0) 
imputer.fit(X[:,1:3])#aplica los cambios al imputer
X[:,1:3] = imputer.transform(X[:,1:3])#sustituye los cambios

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

#Dividir el dataset en un conjunto de entrenamiento y un conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) #Entradas,salidas, tamaño del test, semilla para que salgan los mismos datos