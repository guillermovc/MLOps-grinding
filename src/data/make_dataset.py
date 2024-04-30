import os
import pandas as pd
from pathlib import Path

print(f"Folder actual: {os.getcwd()}")

main_folder = Path(os.getcwd()) / 'data' / 'raw'

df = pd.read_parquet(main_folder / 'datos_molienda.parquet')

print(f"Guardando archivo procesado en {main_folder.parent/ 'processed'}")

df.to_parquet( main_folder.parent/ "processed" /'datos_molienda_prueba.parquet')
