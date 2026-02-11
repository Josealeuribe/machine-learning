import pandas as pd

df = pd.read_csv('titanic.csv')

# Empleando funcion HEAD()
print('-' * 150)
print(df.head())
print('-' * 150 + '\n')

# Empleando funcion INFO()
print('-' * 150)
print(df.info())
print('-' * 150 + '\n')

# Empleando funcion DESCRIBE()
print('-' * 150)
print(df.describe())
print('-' * 150 + '\n')

# Calculamos el promedio de las edades MEAN()
print('-' * 18)
print(df['Age'].mean())
print('-' * 18 + '\n')

# Calculamos el promedio de edades usando la mediana MEDIAN()
print('-' * 4)
print(df['Age'].median())
print('-' * 4 + '\n')

# Calculamos el promedio de edaes usando la moda MODE()
print('-' * 25)
print(df['Age'].mode())
print('-' * 25 + '\n')

# Calculamos el total de las columnas iniciando en 0.
print('-' * 4)
print(df.shape[0])
print('-' * 4 + '\n') 

# Calculamos el total de los registros usando len
print('-' * 4)
print(len(df))
print('-' * 4 + '\n')

# Tipo de datos de las varibles volemos a usar INFO() como ya lo implemente antes usare df.dtypes
print('-' * 22)
print(df.dtypes)
print('-' * 22 + '\n')

# Columnas que podrian ser irrelevantes
print('-' * 73)
print(df.columns)
print('-' * 73 + '\n')

# Se puede determinar si es niño o adulto
print('-' * 40)
print(df['Age'].describe())
print('-' * 40 + '\n')

print('-' * 40)
print(df['Age'].value_counts())
print('-' * 40 + '\n')

# Rango de edad predominante de fallecidos/sobrevivientes
print('-' * 70)
print(df.groupby('Survived')['Age'].describe())
print('-' * 70 + '\n')

print('-' * 40)
print(df.groupby('Survived')['Age'].value_counts())
print('-' * 40 + '\n')

# Quienes murieron mas hombres o mujeres
print('-' * 40)
print(df.groupby('Sex')['Survived'].value_counts())
print('-' * 40 + '\n')

# Edades negativas o mayores a 110
print('-' * 40)
print('El total de edades negativas:', (df['Age'] < 0).sum())
print('-' * 40 + '\n')


print('El total de edades superior o igual a 110:', (df['Age'] >= 110).sum())
print('-' * 40 + '\n')

# Calcular por que unos sobrevivieron y otros no
print('-' * 40)
print(df.groupby('Pclass')['Survived'].mean())
print('\nEs posible calcular segun sexo o edad, pero en genereal es complicado saberlo.')
print('-' * 40 + '\n')
