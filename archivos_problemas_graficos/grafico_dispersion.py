import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dispersion.csv')

# Gráfico de barras
sns.scatterplot(x="tiempo", y="dinero", data=df)

plt.show()
