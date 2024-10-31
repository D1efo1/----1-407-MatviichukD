# -*- coding: utf-8 -*-
"""LR_1_task_4.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CbCBX0vWHUlfY2conQm2gy3GUE-FsQI4
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB




# Вхідний файл, який містить дані
input_file = 'data_multivar_nb.txt'

# Завантаження даних із вхідного файлу
data = pd.read_csv(input_file, delimiter=',').values
X, y = data[:, :-1], data[:, -1]

# Створимо екземпляр наївного Байєсовського класифікатора
classifier = GaussianNB()

# Навчимо класифікатор, використовуючи тренувальні дані
classifier.fit(X, y)

# Запустимо класифікатор на тренувальних даних та спрогнозуємо результати
y_pred = classifier.predict(X)

# Обчислимо якість (accuracy) класифікатора
accuracy = 100.0 * (y == y_pred).sum() / X.shape[0]
print("Accuracy of Naive Bayes classifier =", round(accuracy, 2), "%")

# Візуалізувати результати роботи класифікатора
visualize_classifier(classifier, X, y)

# Разбивка данных на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)
classifier_new = GaussianNB()
classifier_new.fit(X_train, y_train)
y_test_pred = classifier_new.predict(X_test)

# Вычисляем точность классификатора и визуализируем результаты
accuracy = 100.0 * (y_test == y_test_pred).sum() / y_test.shape[0]
print("Accuracy of the new classifier =", round(accuracy, 2), "%")

# Визуализация работы классификатора
visualize_classifier(classifier_new, X_test, y_test)

# Используем встроенные функции для вычисления точности (accuracy), прецизионности (precision) и полноты (recall) классификатора на основе перекрестной проверки (cross-validation)
num_folds = 3
accuracy_values = cross_val_score(classifier_new, X, y, scoring="accuracy", cv=num_folds)
print("Accuracy =", str(round(100 * accuracy_values.mean(), 2)) + "%")

precision_values = cross_val_score(classifier_new, X, y, scoring="precision_weighted", cv=num_folds)
print("Precision =", str(round(100 * precision_values.mean(), 2)) + "%")

recall_values = cross_val_score(classifier_new, X, y, scoring="recall_weighted", cv=num_folds)
print("Recall =", str(round(100 * recall_values.mean(), 2)) + "%")

f1_values = cross_val_score(classifier_new, X, y, scoring="f1_weighted", cv=num_folds)
print("F1 =", str(round(100 * f1_values.mean(), 2)) + "%")

"""!pip"""