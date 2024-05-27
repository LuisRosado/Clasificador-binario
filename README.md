# Clasificador-binario
Se implemento un clasificador binario utilizando el conjunto de datos de cáncer de mama (breastCancer). El objetivo fue entrenar un modelo de Perceptrón Multicapa (MLP) para clasificar muestras de tejido mamario como benignas o malignas basadas en una serie de características clínicas y de laboratorio.

# Metodologıa

Se dividio el conjunto de datos en conjuntos de entrenamiento y prueba utilizando la funcion ”train test split” de la biblioteca ”scikit learn”. Luego, se entreno un modelo de Perceptron Multicapa (MLP) utilizando la implementacion proporcionada por ”sklearn neural network MLPClassifier”.

Se ajustaron los hiperparametros .alpha 2 ”max iter” para mejorar el rendimiento del modelo. Finalmente, se evaluo el modelo utilizando metricas de rendimiento como precision, recall y F1 score, ası como una matriz de
confusion.
Figura 1: Codigo de la practica.

# Resultados

El modelo de MLPClassifier logro una precision del 36.18 en el conjunto de entrenamiento y del 39.77 en el conjunto de prueba. Se observaron advertencias de precision indefinida en la matriz de confusion, lo que indica la
presencia de clases desbalanceadas en los datos.


![Resultados](https://github.com/LuisRosado/Clasificador-binario/assets/140114139/45a19f61-030e-4e2d-b8d7-a5124c4cf0b5)

Figura 1: Prediccion de casos confirmados de COVID-19

![Grafica_1](https://github.com/LuisRosado/Clasificador-binario/assets/140114139/575de775-1147-44c3-9519-8cad41183fb0)


Figura 2: Serie de tiempo de casos confirmados de COVID-19

![Grafica_2](https://github.com/LuisRosado/Clasificador-binario/assets/140114139/b97b8a94-07c9-4559-b613-e1da884c5e6c)

Figura 3: Prediccion de casos confirmados de COVID-19
