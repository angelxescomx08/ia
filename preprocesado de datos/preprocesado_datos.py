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

#Dividir el dataset en un conjunto de entrenamiento y un conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) #Entradas,salidas, tamaño del test, semilla para que salgan los mismos datos

#Escalado de variables
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""











