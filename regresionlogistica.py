# -*- coding: utf-8 -*-
"""RegresionLogistica.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10xRaCiHohUpOVE-iZQ-g9Gf-8tSc_za7
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

from google.colab import files
uploaded = files.upload()

# Cargar los datos desde un archivo CSV
data = pd.read_csv('Prueba2.csv')

# Ver las primeras filas y la información básica de los datos
print(data.head())
print(data.info())
print(data.describe())

# Separar las características (X) y la variable objetivo (y)
X = data.drop('Target', axis=1)
y = data['Target']

# Separar los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crear y entrenar el modelo de Regresión Logística
logistic_model = LogisticRegression()
logistic_model.fit(X_train_scaled, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = logistic_model.predict(X_test_scaled)

# Calcular la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)

# Mostrar la matriz de confusión 
plt.figure(figsize=(8,6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Imprimir reporte de clasificación
print(classification_report(y_test, y_pred))

# Calcular y mostrar la exactitud del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Exactitud del modelo: {accuracy * 100:.2f}%')
