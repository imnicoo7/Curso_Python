import pandas as pd

df = pd.read_csv('archivo.csv')

# Ordenar dataframe por edad
df = df.sort_values("edad")

# Ordenarlo de forma descendente
df_descendente = df.sort_values("edad", ascending=False)

# Concatenando dos df
df_concatenado = pd.concat([df, df_descendente])

# accediendo a la edad de la fila 2 con loc
elemento_especifico_loc = df.loc[3, 'edad']

# accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[3, 2]

# accediendo a todas las filas de una columna
apellido = df.loc[:,"apellido"]

apellido_iloc = df.iloc[:,1]

print(apellido_iloc)
