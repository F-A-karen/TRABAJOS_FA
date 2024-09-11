
import matplotlib.pyplot as plt
import numpy as np

xpoints =  np.array([1, 2, 5, 6, 7])
ypoints= np.array([2, 6, 3, 6, 3])


# Crear un gráfico de dispersión

plt.plot(xpoints, ypoints, marker ='o')

# Crear una línea de ajuste para la visualización
plt.xlabel('tiempo')
plt.ylabel('valor')
plt.title('grafico de valores subiendo y bajando ')

plt.grid(True)
plt.show()