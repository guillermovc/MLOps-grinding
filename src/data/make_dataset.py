# Manejo de archivos
import os
from pathlib import Path

# Manejo de datos
import pandas as pd
import numpy as np

# Visualización de datos
import matplotlib.pyplot as plt
import seaborn as sns

#outliers 
from pyod.models.mcd import MCD

from datetime import datetime, timedelta, time, date

# Establecer los folders de donde leeremos y guardaremos nuestros datasets
raw_folder = Path(os.getcwd()) / 'data' / 'raw'
processed_folder = Path(os.getcwd()) / 'data' / 'processed'

# Crear el directorio si no existe...
processed_folder.mkdir(parents=True, exist_ok=True)

nombre_no_outliers = "df_model_no_outliers.parquet"
nombre_transformado = "df_model_tidy.parquet"


# ==========================================================================
# 1. Quitar outliers
# ==========================================================================
df = pd.read_parquet(raw_folder / 'df_model.parquet')

print("Removiendo outliers ...")

mcd_model = MCD(contamination  = 0.01) 
vars_outliers = ['velocidad',
                'potencia',
                'flujo_agua',
                'rendimiento',
                'presion_ewm']
mcd_model.fit(df[vars_outliers])

df['outlier'] = mcd_model.labels_
df_no = df[df.outlier == 0].drop(columns = ['outlier'])

df_no.to_parquet(processed_folder / nombre_no_outliers)
print(f"Almacenando en la ruta {processed_folder / nombre_no_outliers}")

# ==========================================================================
# 2. Transformar los datos a intervalo
# ==========================================================================
df = df_no.copy() # Copiamos el df sin outliers

print("Transformando los datos ...")

# Los datos con separación de 20 y 30 segundos se llenenan con un forward fill
df = df.asfreq('10s')
df = df.ffill(limit = 3) #rellenar a lo máximo 30 segundos

window_len = 8 * 6 #cada 1 equivale a 10 segundos
vel_column = df.velocidad.rolling(window = window_len).mean().values
pot_column = df.potencia.values
rendimiento_column = df.rendimiento.rolling(window = window_len).mean().values
ruido_column = df.ruido.values
p80_column = df.p80.rolling(window = window_len).mean().values
# in10_column = df.in10.rolling(window = window_len).mean().values
# in1_column = df.in1.rolling(window = window_len).mean().values
f80_column = df.f80.rolling(window = window_len).mean().values
per_solidos_column = df.per_solidos.rolling(window = window_len).mean().values
wi_column = df.wi.rolling(window = window_len).mean().values
spi_column = df.spi.rolling(window = window_len).mean().values
imp_criticos_column = df.imp_criticos.rolling(window = window_len).mean().values
imp_estandares_column = df.imp_estandares.rolling(window = window_len).mean().values
jb_column = df.jb.values
presion = df.presion_ewm.values

df_model = pd.DataFrame({ 'velocidad':vel_column, # promedio
                       'potencia':pot_column, # de instante
                       'rendimiento':rendimiento_column,#promedio
                       'ruido':ruido_column,  #de instante
                       'p80':p80_column, #promedio
                       # 'in10':in10_column, #promedio
                       #  'in1':in1_column, #promedio
                       'f80':f80_column, #promedio
                       'per_solidos':per_solidos_column, #promedio
                       'wi':wi_column, #promedio
                       'spi':spi_column, #promedio
                       'imp_criticos':imp_criticos_column, #instante
                       'imp_estandares':imp_estandares_column, #instante
                       'jb':jb_column, #instante
                       'presion':presion, # de instante
                                 }, index = df.index)

df_model = df_model.dropna().reset_index(drop=True)

print("Se procesó el archivo raw con los datos transformados")
print(f"Shape resultante: {df_model.shape}")
print(f"Almacenando en la ruta {processed_folder / nombre_transformado}")

df_model.to_parquet(processed_folder / nombre_transformado)