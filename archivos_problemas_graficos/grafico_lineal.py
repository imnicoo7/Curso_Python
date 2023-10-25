import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('pedos.csv')

sns.lineplot(x="fecha", y=" pedos", data=df)
# Creando un punto en el momento de más pedis
plt.plot("01-07", 22, "o")
plt.show()
