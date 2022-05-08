from dis import dis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Housing = pd.read_csv("USA_Housing.csv")
Housing.rename(columns={'Avg. Area Income':'Ingresos_area', 'Avg. Area House Age':'Antiguedadcasa_area', 'Avg. Area Number of Rooms':'Habitaciones_area', 'Avg. Area Number of Bedrooms':'Dormitorios_area', 'Area Population':'Poblacion', 'Price':'Precio', 'Address':'Dirección'}, inplace=True)
Housing.dropna()
print(Housing)
mediaingresos_area = Housing['Ingresos_area'].mean()
mediahabitaciones_area = Housing['Habitaciones_area'].mean()
mediaantiguedadcasa = Housing['Antiguedadcasa_area'].mean()
mediapoblacion = Housing['Poblacion'].mean()
#mediadormitorios_area = Housing['Dormitorios_area'].mean()
dormitorios = list(Housing['Dormitorios_area'])
dormitorios_area = []
for i in dormitorios:
    dormitorios_area.append(int(i))
del dormitorios
dormitorios_area = sorted(dormitorios_area)
minimo_dor = min(dormitorios_area) ; maximo_dor = max(dormitorios_area)
conteo = []
habitaciones = []
for i in range(minimo_dor, maximo_dor+1):
    recuento = dormitorios_area.count(i)
    conteo.append(recuento)
    habitaciones.append(i)
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
    plt.hist(Housing['Precio'], color = 'yellow')
    plt.xlabel('Precio')
    plt.axvline(x=mediaprecio, color='black', linestyle='dotted', label='Media del precio')
    plt.title("Gráfico con el precio de los apartamentos(en millones aproximados)")
    plt.legend()
    plt.show()

def pie():
    plt.figure(figsize=(9,5))
    plt.pie(conteo, labels=conteo)
    plt.title("Gráfico con el numero aproximado de habitaciones por apartamento")
    plt.legend(habitaciones, bbox_to_anchor=(1.05, 1))
    plt.show()

def dispersion():
    plt.figure(figsize=(9,5))
    plt.scatter(Housing['Antiguedadcasa_area'], Housing['Poblacion'], s=2, color='orange')
    plt.xlabel('Antigüedad media los apartamentos de una zona(años)') ; plt.ylabel('Población media de una zona')
    plt.axvline(x=mediaantiguedadcasa, color='red', linestyle='dashdot', label='Media de la población')
    plt.axhline(y=mediapoblacion, color='red', linestyle='dashed', label='Media de la antiguedad de los apartamentos')
    plt.legend(bbox_to_anchor=(0.48, 0.85))
    plt.title("Gráfico con la población de una zona en función de la antigüedad media de sus apartamentos")
    plt.show()