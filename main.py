import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Housing = pd.read_csv("USA_Housing.csv")
Housing.rename(columns={'Avg. Area Income':'Ingresos_area', 'Avg. Area House Age':'Antiguedadcasa_area', 'Avg. Area Number of Rooms':'Habitaciones_area', 'Avg. Area Number of Bedrooms':'Dormitorios_area', 'Population':'Población', 'Price':'Precio', 'Address':'Dirección'}, inplace=True)
Housing.dropna()
print(Housing)
mediaingresos_area = Housing['Ingresos_area'].mean()
mediaprecio = Housing['Precio'].mean()
