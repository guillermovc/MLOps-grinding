import pandas as pd
from pathlib import Path

raw_folder = Path.cwd(). / 'data' / 'raw'

df = pd.read_parquet(main_folder / 'datos_molienda.parquet')

df.to_parquet( main_folder.parent/'processed'/'datos_molienda_prueba.parquet')
