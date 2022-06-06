# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 21:17:22 2022

@author: angel
"""

#Plantilla de preprocesado: datos faltantes
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