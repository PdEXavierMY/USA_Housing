import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Housing = pd.read_csv("USA_Housing.csv")
Housing.rename(columns={'Avg. Area Income':'Ingresos_area', 'Avg. Area House Age':'Antiguedadcasa_area', 'Avg. Area Number of Rooms':'Habitaciones_area', 'Avg. Area Number of Bedrooms':'Dormitorios_area', 'Population':'Población', 'Price':'Precio', 'Address':'Dirección'}, inplace=True)
Housing.dropna()
print(Housing)
mediaingresos_area = Housing['Ingresos_area'].mean()
mediahabitaciones_area = Housing['Habitaciones_area'].mean()
mediadormitorios_area = Housing['Dormitorios_area'].mean()
mediaprecio = Housing['Precio'].mean()
print("La información de el dataset analizado es la siguiente\n")
print(Housing.info())

def barras():
    plt.figure(figsize=(9,5))
    plt.bar(Housing['Habitaciones_area'], Housing['Ingresos_area'], color = 'blue')
    plt.xlabel("Habitaciones por área") ; plt.ylabel('Ingresos por área')
    plt.axvline(x=mediahabitaciones_area, color='black', linestyle='dashed', label='Media de habitaciones/area')
    plt.title("Gráfico con el número de habitaciones en función del ingreso por área")
    plt.legend()
    plt.show()

def histograma():
    plt.figure(figsize=(9,5))
    plt.hist(sorted(Housing['Dormitorios_area']), color = 'yellow')
    plt.xlabel('Dormitorios por área')
    plt.axvline(x=mediadormitorios_area, color='black', linestyle='dotted', label='Media de dormitorios/area')
    plt.title("Gráfico con el número de dormitorios/área")
    plt.legend()
    plt.show()

histograma()