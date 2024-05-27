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

Figura 1: Prediccion de casos confirmados de COVID-19
Figura 2: Serie de tiempo de casos confirmados de COVID-19
Figura 3: Prediccion de casos confirmados de COVID-19
