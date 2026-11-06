import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Cargar los datos del nivel del mar
    df = pd.read_csv("epa-sea-level.csv")

    # Crear el diagrama de dispersión
    fig, ax = plt.subplots()
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Regresión lineal usando todos los datos disponibles
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )

    # Crear los valores de los años hasta 2050
    years = range(df["Year"].min(), 2051)

    # Calcular y dibujar la primera línea de mejor ajuste
    sea_levels = [slope * year + intercept for year in years]
    ax.plot(years, sea_levels, "r", label="Best fit line (all data)")

    # Filtrar los datos desde el año 2000 en adelante
    recent_df = df[df["Year"] >= 2000]

    # Regresión lineal usando únicamente los datos desde 2000
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        recent_df["Year"], recent_df["CSIRO Adjusted Sea Level"]
    )

    # Crear los años desde 2000 hasta 2050
    recent_years = range(2000, 2051)

    # Calcular y dibujar la segunda línea de mejor ajuste
    recent_sea_levels = [
        slope_recent * year + intercept_recent for year in recent_years
    ]
    ax.plot(
        recent_years,
        recent_sea_levels,
        "g",
        label="Best fit line (2000 onward)"
    )

    # Configurar títulos y etiquetas
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Mostrar la leyenda
    ax.legend()

    # Guardar el gráfico
    plt.savefig("sea_level_plot.png")

    # Devolver los ejes para las pruebas
    return ax
