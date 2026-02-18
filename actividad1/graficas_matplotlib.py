import pandas as pd
import matplotlib.pylab as plt

df = pd.read_csv("titanic.csv")
# print(df.describe())

count = df["Sex"].value_counts()
# print(count)
# plt.bar(count.index, count.values)
# plt.title('Cantidad de pasajeros por genero.')
# plt.xlabel("Sexo")
# plt.ylabel("Cantidad")
# plt.show()

# plt.pie(count.values)
# plt.show()

# plt.hist(df["Age"], bins=20)
# plt.show()

# plt.hist(df.groupby("Survived")["Age"].value_counts(), bins=20)
# plt.show()



# # Quienes murieron mas hombres o mujeres

# print('-' * 40)
# print('Quienes murieron mas hombres o mujeres?\n',df.groupby('Sex')['Survived'].value_counts())
# print('-' * 40 + '\n')



# Ejemplo de un gradico en disperción

# plt.scatter(df['Age'], df["Fare"])
# plt.title('Grafica de dispeción de la edad vs la tarifa')
# plt.xlabel('Edad')
# plt.ylabel('Tarifa')
# print(df[['Age', 'Fare']].corr())
# plt.show()



# Ejemplo de cajas o boxplot

# plt.boxplot(df['Fare'].dropna())
# plt.title('Diagrama de caja de la edad')
# plt.show()



# Ejemplo grafico de lineas

promedio = df.groupby('Pclasse')['Fare'].mean()
plt.plot(promedio.index, promedio.values)
plt.xlabel('Clase')
plt.ylabel('Edad')
plt.grid(True)
plt.title('Precio promedio por clase')
plt.show()



