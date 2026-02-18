import pandas as pd

df = pd.read_csv('titanic.csv')

# # Empleando funcion HEAD()
# print('-' * 150)
# print(df.head())  # Head() Me muestra los primeros datos de mi csv
# print('-' * 150 + '\n')

# # Empleando funcion INFO()
# print('-' * 150)
# print(df.info())  # Info() Me trae informacion general de mi csv
# print('-' * 150 + '\n')

# # Empleando funcion DESCRIBE()
# print('-' * 150)
# print(df.describe())   # Describe() resumen estadístico automático de una columna o de todo un DataFrame.
# print('-' * 150 + '\n')

# # Calculamos el promedio de las edades MEAN()
# print('-' * 18)
# print(df['Age'].mean())  # Mean() Es el medio o el promedio, 
# print('-' * 18 + '\n')

# # Calculamos el promedio de edades usando la mediana MEDIAN()
# print('-' * 4)
# print(df['Age'].median()) # Median() Valor que se queda en la mitad cuando se ordenan de mayor a menor
# print('-' * 4 + '\n')

# # Calculamos el promedio de edaes usando la moda MODE()
# print('-' * 25)
# print(df['Age'].mode()) # Mode() La moda es el valor que más se repite en una columna.
# print('-' * 25 + '\n')

# # Calculamos el total de las columnas iniciando en 0.
# print('-' * 4)
# print(df.shape[0]) # posicion 0 y shape se usa para devolver una tupla
# print('-' * 4 + '\n') 

# # Calculamos el total de los registros usando len
# print('-' * 4)
# print(len(df)) 
# print('-' * 4 + '\n')

# # Tipo de datos de las varibles volemos a usar INFO() como ya lo implemente antes usare df.dtypes
# print('-' * 22)
# print(df.dtypes) 
# print('-' * 22 + '\n')

# # Columnas que podrian ser irrelevantes
# print('-' * 73)
# print(df.columns)
# print('-' * 73 + '\n')

# # Se puede determinar si es niño o adulto
# print('-' * 40)
# print(df['Age'].describe())
# print('-' * 40 + '\n')

# print('-' * 40)
# print(df['Age'].value_counts()) # Value_counts Cuenta cuántas veces aparece cada valor único en una columna.
# print('-' * 40 + '\n')

# # Rango de edad predominante de fallecidos/sobrevivientes
# print('-' * 70)
# print(df.groupby('Survived')['Age'].describe()) 
# print('-' * 70 + '\n')

# print('-' * 40)
# print(df.groupby('Survived')['Age'].value_counts())
# print('-' * 40 + '\n')

# # Quienes murieron mas hombres o mujeres
# print('-' * 40)
# print('Quienes murieron mas hombres o mujeres?\n',df.groupby('Sex')['Survived'].value_counts())
# print('-' * 40 + '\n')

# # Edades negativas o mayores a 110
# print('-' * 40)
# print('El total de edades negativas:', (df['Age'] < 0).sum())
# print('-' * 40 + '\n')


# print('El total de edades superior o igual a 110:', (df['Age'] >= 110).sum())
# print('-' * 40 + '\n')

# # Calcular por que unos sobrevivieron y otros no
# print('-' * 40)
# print(df.groupby('Pclass')['Survived'].mean())
# print('\nEs posible calcular segun sexo o edad, pero en genereal es complicado saberlo.')
# print('-' * 40 + '\n')
