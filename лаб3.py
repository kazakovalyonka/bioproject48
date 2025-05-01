import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Шаг 1: Загрузка данных Iris
iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data['target'] = iris.target  # Добавляем столбец с классами

# Шаг 2: Выбор факторов для построения диаграммы
factor_x = 'sepal length (cm)'  # Первый столбец
factor_y = 'petal length (cm)'  # Второй столбец

x = data[factor_x]
y = data[factor_y]
classes = data['target']

# Шаг 3: Построение диаграммы рассеяния
plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, c=classes, cmap='viridis', edgecolor='k', s=100, alpha=0.8)

# Настройка графика
plt.title('Диаграмма рассеяния для данных Iris', fontsize=14)
plt.xlabel(factor_x, fontsize=12)
plt.ylabel(factor_y, fontsize=12)
plt.colorbar(scatter, label='Классы')
plt.grid(True)

# Легенда (для наглядности)
legend_labels = iris.target_names  # Названия классов
for i, label in enumerate(legend_labels):
    plt.scatter([], [], c=scatter.cmap(i / len(legend_labels)), label=label, edgecolor='k', s=100)
plt.legend(title="Классы", loc="upper left")

# Показ графика
plt.tight_layout()
plt.show()
