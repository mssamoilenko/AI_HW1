# import pandas as pd
#
# df = pd.DataFrame({
#     'Name': [
#         'Canada',
#         'France',
#         'Germany',
#         'Italy',
#         'Japan',
#         'United Kingdom',
#         'United States',
#     ],
#     'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
#     'GDP': [
#         1785387,
#         2833687,
#         3874437,
#         2167744,
#         4602367,
#         2950039,
#         17348075
#     ],
#     'Surface Area': [
#         9984670,
#         640679,
#         357114,
#         301336,
#         377930,
#         242495,
#         9525067
#     ],
#     'HDI': [
#         0.913,
#         0.888,
#         0.916,
#         0.873,
#         0.891,
#         0.907,
#         0.915
#     ],
#     'Continent': [
#         'America',
#         'Europe',
#         'Europe',
#         'Europe',
#         'Asia',
#         'Europe',
#         'America'
#     ]
# })

# print(df)

# df.columns = df.columns.str.lower()
# # print(df)

# df.info()
# print(df.shape)

# print(df.dtypes)

# print(type(df['Population']))
# print(df[['Population','Name']])

# print(df.iloc[3,:])



# col_inds = [0,1,-1]
# print(df.iloc[:,col_inds])


# df[df['Continent'] == 'Europe']
# print(df[df['Continent'] == 'Europe'])

# df['Continent'] == 'Europe'
# df['HDI'] >= 0.9
#
# print(df[(df['Continent'] == 'Europe')&(df['HDI'] >= 0.9)]) #and
# print(df[(df['Continent'] == 'Europe')|(df['HDI'] >= 0.9)]) #or
# print(df[~(df['Continent'] == 'Europe')]) #no

# data = pd.DataFrame({
#     "Кіт": [0.50, 0.20, 0.05, 0.10, 0.15, 0.05],
#     "Автомобіль": [0.05, 0.05, 0.05, 0.60, 0.05, 0.10],
#     "Собака": [0.30, 0.40, 0.05, 0.10, 0.25, 0.05],
#     "Автомобіль": [0.05, 0.05, 0.05, 0.60, 0.05, 0.10],
#     "Дерево": [0.05, 0.05, 0.05, 0.10, 0.45, 0.75],
#     "Птах": [0.10, 0.30, 0.80, 0.10, 0.10, 0.05],
# })
#
#
# print(data.idxmax(axis=1))




#hw
#task1
import numpy as np
# a = np.arange(30,70)
# print(a)
#
# #task2
# b = a[a % 2 == 0]
# b
# print(b)

#task3
# g = np.linspace(0, 0.9,10)
# print(g)
#
# #task4
# def gener_new_matrix(matrix):
#     n = matrix.shape[0]
#     new_matrix = np.zeros((n+2, n+2), dtype=matrix.dtype)
#     new_matrix[1: n+1, 1: n+1] = matrix
#     return new_matrix
# matrix=np.array([[1,2],[3,4]])
#
# #task5
# n = gener_new_matrix(matrix)
# n
# print(n.dtype)
#
# n_float = n.astype('float32')
# n_float
# print(n_float.dtype)

#task6
#
# x = np.array([1, 5, 3, 8, 6, 5, 7, 4])
# var = 5
# x[x == var] = -1
#
# x[x > var] = -1
#
# x[x < var] = -1

#task7
# X = np.array([[1, 2, np.nan, 4],
#               [5, np.nan, np.nan, 4],
#               [np.nan, 10, 11, np.nan]])
# X[np.isnan(X)] = -1
# print(X)

# #task8
# arr = np.random.randint(1, 100,(4,6))
# arr.reshape(3,8)

#task9
# arr = np.random.randint(1, 100,(3,4))
# print(arr)
#
# x1 = arr[:, 0]
# resx1 = np.mean(x1)
# print(resx1)
# x2 = arr[:, 1]
# resx2 = np.mean(x2)
#
# x3 = arr[:, 2]
# resx3 = np.mean(x3)
#
# x4 = arr[:, 3]
# resx4 = np.mean(x4)

#task10
# x = np.array([[0.2 , 0.3 , 0.23, 0.07, 0.03, 0.17],
#               [0.15, 0.06, 0.21, 0.12, 0.24, 0.24],
#               [0.1 , 0.21, 0.03, 0.07, 0.31, 0.28],
#               [0.21, 0.24, 0.03, 0.18, 0.12, 0.21],
#               [0.19, 0.25, 0.25, 0.06, 0.12, 0.12]])
#
# max_indices = np.argmax(x, axis=1)
# max_indices





