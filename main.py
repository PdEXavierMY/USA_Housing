import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Housing = pd.read_csv("USA_Housing.csv")
Housing.rename(columns={'Avg. Area Income':'Ingresos_area', 'Avg. Area House Age':'Antiguedadcasa_area', 'Avg. Area Number of Rooms':'Habitaciones_area', 'Avg. Area Number of Bedrooms':'Dormitorios_area', 'Population':'Población', 'Price':'Precio', 'Address':'Dirección'}, inplace=True)
Housing.dropna()
print(Housing)
mediaingresos_area = Housing['Ingresos_area'].mean()
mediaprecio = Housing['Precio'].mean()
print("La información de el dataset analizado es la siguiente\n")
print(Housing.info())

#def graficos():
plt.figure(figsize=(9,5))
plt.bar(Housing['Habitaciones_area'], Housing['Ingresos_area'], color = 'blue')
plt.xlabel("Media de habitaciones por área") ; plt.ylabel('Media de ingresos por área')
plt.title("Gráfico con el número de habitaciones en función del ingreso por área")
plt.show()