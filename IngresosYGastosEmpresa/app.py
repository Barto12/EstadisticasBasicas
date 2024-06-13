import pandas as pd
import matplotlib.pyplot as plt


def plot_ingresos_gastos(dataframe):
    plt.figure(figsize=(10, 6))

    # Graficar los ingresos
    plt.plot(dataframe.index, dataframe['Ingresos'], label='Ingresos', marker='o')

    # Graficar los gastos
    plt.plot(dataframe.index, dataframe['Gastos'], label='Gastos', marker='o')

    # Añadir título y leyenda
    plt.title('Evolución de ingresos y gastos')
    plt.legend()

    # Configurar el eje y para que empiece en 0
    plt.ylim(bottom=0)

    # Etiquetas de los ejes
    plt.xlabel('Meses')
    plt.ylabel('Cantidad')

    # Mostrar el gráfico
    plt.grid(True)
    plt.show()


# Crear un dataframe de ejemplo
data = {
    'Ingresos': [1000, 1500, 2000, 2500, 3000, 3500],
    'Gastos': [500, 700, 800, 900, 1100, 1200]
}
df = pd.DataFrame(data, index=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'])

# Llamar a la función para mostrar el gráfico
plot_ingresos_gastos(df)
