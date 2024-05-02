import os
import pandas as pd
from pathlib import Path
from pyod.models.mcd import MCD


raw_folder = Path(os.getcwd()) / 'data' / 'raw'
processed_folder = Path(os.getcwd()) / 'data' / 'processed'




#------------------------------------
#QUITAR OUTLIERS DE df_model.parquet

df = pd.read_parquet(raw_folder / 'df_model.parquet')

mcd_model = MCD(contamination  = 0.01) 

vars_outliers = ['velocidad',
                'potencia',
                'flujo_agua',
                'rendimiento',
                'presion_ewm']
                
mcd_model.fit(df[vars_outliers])

df['outlier'] = mcd_model.labels_

df_no = df[df.outlier == 0].drop(columns = ['outlier'])
df_no.to_parquet(processed_folder / 'df_model_no_outliers.parquet')


