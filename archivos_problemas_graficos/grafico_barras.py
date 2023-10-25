import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cofla_ingresos.csv')

# Gráfico de barras
sns.barplot(x="fuentes", y="ingresos", data=df)
total_ingresos = df['ingresos'].sum()
# Mostrar el total
print(f'El total de ingresos de Cofla es: {total_ingresos}')
plt.show()
