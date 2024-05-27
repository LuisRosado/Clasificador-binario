# Importar bibliotecas
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Leer el archivo
dataFilePath = 'breastCancer.csv'
dataFrame = pd.read_csv(dataFilePath)

# Un vistazo a los datos con los que trabajaremos
dataFrame.head()

# Revisar que no haya nulos
dataFrame.isnull().sum()

# Gráfico de barras para la columna 'diagnosis'
ax = dataFrame['diagnosis'].value_counts().plot(kind='bar')

# Preparar la entrada y la posible salida
y = dataFrame["diagnosis"].values
x = dataFrame.drop(["diagnosis"], axis=1)

# Dividir en conjuntos de entrenamiento y prueba
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3)

# Crear el modelo de un Perceptrón multicapa
model = MLPClassifier(alpha=1, max_iter=2000)

# Entrenar el modelo
model.fit(xtrain, ytrain)

# Revisar el score de los modelos en entrenamiento y en test
print('Train: ', model.score(xtrain, ytrain))
print('Test: ', model.score(xtest, ytest))

# Predecir en la parte de test
ytestpred = model.predict(xtest)
ytrainpred = model.predict(xtrain)

# Sacar el reporte de clasificación
print('Classification report: \n', classification_report(ytest, ytestpred))

# Definir nombres de las clases
class_names = ["no sano", "sano"]

# Matriz de confusión y visualización
cm = confusion_matrix(ytest, ytestpred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot()

# Mostrar la visualización
plt.show()
