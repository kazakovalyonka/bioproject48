import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.datasets import co2

# Загрузка данных из statsmodels
dataset = co2.load_pandas()
data = dataset.data

# Просмотр данных
print(data.head())

# Заполнение пропусков
data = data.fillna(method='ffill')

# Выбор временного интервала
start_date = '1990-01-01'
end_date = '1995-12-31'
filtered_data = data.loc[start_date:end_date]

# Построение графика динамики
plt.figure(figsize=(12, 6))
plt.plot(filtered_data.index, filtered_data['co2'], label='CO2 уровень', color='blue')

# Настройка графика
plt.title('График динамики CO2 за указанный промежуток времени', fontsize=16)
plt.xlabel('Дата', fontsize=14)
plt.ylabel('Уровень CO2', fontsize=14)
plt.legend(loc='upper left')
plt.grid(True)

# Показ графика
plt.tight_layout()
plt.show()


