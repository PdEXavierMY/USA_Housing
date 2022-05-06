import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv("USA_Housing.csv")
print(datos)
datos.rename(columns={'Avg. Area Income':'Ingresos/area', 'Avg. Area House Age':'Antiguedadcasa/area', 'Avg. Area Number of Rooms':'Habitaciones/area', 'Avg. Area Number of Bedrooms':'Dormitorios/area', 'Population':'Población', 'Price':'Precio', 'Address':'Dirección'})