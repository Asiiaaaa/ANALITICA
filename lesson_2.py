# -*- coding: utf-8 -*-
"""LESSON 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15TAJjE2K4UhXioUWPsgn-7v0JJvM_3Al

#**Условие 1: 1 задача**
Скачать файл в уроке

Считать данные с помощью pandas

Вывести на экран первые 5 строк

Посмотреть на описание признаков и на их содержание
"""

import pandas as pd
df = pd.read_csv('/content/kc_house_data.csv')
df.head ()

"""kc_house_data .csv

*  id - Уникальный ID для каждого дома
* date - Дата продажи дома
* price - Стоимость продажи дома
* bedrooms - Кол-во спален
* bathrooms - Кол-во ванных комнат (0.5 - туалет без душа)
* sqft_living - Кв. метры жилые
* sqft_lot - Кв. метры общие
* floors - Кол-во этажей
* waterfront - Есть набережная или нет
* view - Значение от 0 до 4 насколько хороший вид
* condition - Значение от 1 до 5 насколько хорошее состояние
* grade - Значение от 1 до 13, где 1-3 плохая конструкция здания и дизайн, 7 - средний уровень конструкции и дизайна, 11-13 - высокое качество конструкции и дизайна
* sqft_above - Кв. метры дома, которые находятся выше земли
* sqft_basement - Кв. метры дома, которые находятся ниже земли
* yr_built - Год постройки дома
* yr_renovated - Год ремонта дома
* zipcode - Индекс
* lat - Широта
* long - Долгота
* sqft_living15 - Кв. метры жилой площади у 15 соседей
* sqft_lot15 - Кв. метры общей площади у 15 соседей

#**Условие 2: 2 задача**
Проведите первичный анализ данных
Изучите типы данных
Найдите количество пропущенных ячеек в данных
Посчитайте основные статистики по всем признакам и поизучайте их
Пишите выводы
"""

# Изучите типы данных
df.info()

# Найдите количество пропущенных ячеек в данных
df.isnull().sum().sum()

# Посчитайте основные статистики по всем признакам
df.describe()

"""#**Условие 3:3 задача**
Ответьте на несколько вопросов

3.1 В каком диапазоне изменяются стоимости недвижимости?

3.2 Какую долю в среднем занимают жилая площадь от всей площади по всем домам?

3.3 Как много домов с разными этажами в данных?

3.4 Насколько хорошие состояния у домов в данных?

3.5 Найдите года, когда построили первый дом, когда построили последний дом в данных?
"""

# В каком диапазоне изменяются стоимости недвижимости
df['price'].min(), df['price'].max()

# Какую долю в среднем занимают жилая площадь от всей площади по всем домам
(df['sqft_living'] / df['sqft_lot']).mean()

# Как много домов с разными этажами в данных
df['floors'].value_counts()

# Насколько хорошие состояния у домов в данных
df['condition'].value_counts()

# Насколько хорошие состояния у домов в данных
df['condition'].mean()

# Найдите года, когда построили первый дом, когда построили последний дом в данных
df['yr_built'].min(), df['yr_built'].max()

"""#**Условие 4:4 задача**

Ответьте на несколько вопросов

4.1 Сколько в среднем стоят дома, у которых 2 спальни?

4.2 Какая в среднем общая площадь домов, у которых стоимость больше 600 000?

4.3 Как много домов коснулся ремонт?

4.4 Насколько в среднем стоимость домов с оценкой grade домов выше 10 отличается от стоимости домов с оценкой grade меньше 4?
"""

# Сколько в среднем стоят дома, у которых 2 спальни
df['price'][df['bedrooms'] == 2].mean()

# Какая в среднем общая площадь домов, у которых стоимость больше 600 000
df['sqft_lot'][df['price'] > 600000].mean()

# Как много домов коснулся ремонт
df['id'][df['yr_renovated'] > 0].count()

# Насколько в среднем стоимость домов с оценкой grade домов выше 10 отличается от стоимости домов с оценкой grade меньше 4?
df['price'][df['grade'] > 10].mean() - df['price'][df['grade'] < 4].mean()

"""#**Условие 5:5 задача**

Ответьте на несколько вопросов

5.1 Выберите дом клиенту
Клиент хочет дом с видом на набережную, как минимум с тремя ванными и с подвалом. Сколько вариантов есть у клиента?

5.2 Выберите дом клиенту
Клиент хочет дом либо с очень красивым видом из окна, либо с видом на набережную, в очень хорошем состоянии и год постройки не меньше 1980 года. В какой ценовом диапазоне будут дома?

5.3 Выберите дом клиенту
Клиент хочет дом без подвала, с двумя этажами, стоимостью до 150000. Какая оценка по состоянию у таких домов в среднем?
"""

# Клиент хочет дом с видом на набережную, как минимум с тремя ванными и с подвалом. Сколько вариантов есть у клиента
df['id'][(df['waterfront'] == 1) & (df['bathrooms'] >= 3) & (df['sqft_basement'] > 0)].count()

# Клиент хочет дом либо с очень красивым видом из окна, либо с видом на набережную, в очень хорошем состоянии и год постройки не меньше 1980 года. В какой ценовом диапазоне будут дома
df1 = df[((df['view'] > 3) | (df['waterfront'] == 1)) & (df['condition'] > 4) & (df['yr_built'] >= 1980)]
df1['price'].min(), df1['price'].max()

# Клиент хочет дом без подвала, с двумя этажами, стоимостью до 150000. Какая оценка по состоянию у таких домов в среднем
df['condition'][(df['sqft_basement'] == 0) & (df['floors'] == 2) & (df['price'] < 150000)].mean()