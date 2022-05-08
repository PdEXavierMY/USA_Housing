from dis import dis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

from introducir.numero import solicitar_introducir_numero_extremo

Housing = pd.read_csv("USA_Housing.csv")
Housing.rename(columns={'Avg. Area Income':'Ingresos_area', 'Avg. Area House Age':'Antiguedadcasa_area', 'Avg. Area Number of Rooms':'Habitaciones_area', 'Avg. Area Number of Bedrooms':'Dormitorios_area', 'Area Population':'Poblacion', 'Price':'Precio', 'Address':'Dirección'}, inplace=True)
Housing.dropna()
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

def eleccion():
    print("Este repositorio contiene un análisis del dataset USA_Housing. ¿Que parte del análisis deseas visualizar?")
    print("1: Análisis inicial\n2: Grafico de Barras\n3: Histogramas\n4: Grafico de secciones\n5: Grafico de Dispersión\n6: Todos los gráficos\n7: Finalizar\n")
    n = solicitar_introducir_numero_extremo("Debes elegir", 1, 7)
    if n ==1:
        print("El dataset analizado es el siguiente:\n")
        print(Housing)
        print("La información relativa al dataset analizado es la siguiente:\n")
        print(Housing.info())
        print("")
        sleep(2)
        eleccion()
    elif n == 2:
        print("Este grafico analiza la relación que existe entre la media del número de habitaciones de un apartamento en una zona concreta con los ingresos medios en esa zona, con el objetivo de confirmar o desmentir la hipótesis de que a más habitaciones mayor el sueldo medio en la zona.")
        barras()
        eleccion()
    elif n == 3:
        print("Este gráfico muestra la agrupación del precio medio de los apartamentos por zona. Este gráfico nos permite hacernos una idea aproximada de la media y cantidad de apartamentos con un precio concreto.")
        histograma()
        eleccion()
    elif n == 4:
        print("Este gráfico nos muestra la cantidad del número de dormitorios(leyenda). En este caso sirve para comprobar cuantas habitaciones de media tiene la gente en su domicilio.")
        pie()
        eleccion()
    elif n == 5:
        print("Este gráfico nos enseña la distribución de la población en una zona en función de la antigüedad de sus apartamentos, casas... Podemos ver que las mayores y menores poblaciones se encuentran los que más dispersos. En cambio, en la media de la antigüedad de los domicilios y de la población se concentran la mayoría de puntos, como era de esperar.")
        dispersion()
        eleccion()
    elif n == 6:
        print("Ahora se visualizarán todos los gráficos 1 a 1. Si quiere un minianálisis de los resultados ejecute cada gráfico independientemente.")
        barras()
        histograma()
        pie()
        dispersion()
        eleccion()
    elif n == 7:
        exit()