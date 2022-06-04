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