import pandas as pd

df = pd.read_csv("./archivos/archivo.csv")

# Convertir a String los datos de una columna
df['edad'] = df['edad'].astype(str)

# remplazando los datos "dalto" por maestro
df['apellido'].replace("Dalto", 'Maestro', inplace=True)
print(df)
# elimando las filas con datos repetidos
df = df.dropna()

# eliminando las filas duplicadas
df = df.drop_duplicates()
# Creando un CSV con el dataframe resultante (limpio)
df.to_csv('./archivos/df_limpio.csv')
 