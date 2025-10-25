import matplotlib.pyplot as plt





def graficar_ventas_por_categoria(df_libros):
    top5 = (
        df_libros.groupby("categoria")["precio"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    plt.figure(figsize=(8, 5))
    plt.bar(top5.index, top5.values, color="skyblue")
    plt.title("Top 5 Categorías con Más Ventas")
    plt.xlabel("Categoría")
    plt.ylabel("Ventas Totales ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



def graficar_frecuencia_libroscategorias(df_libros):
    frecuencia = df_libros["categoria"].value_counts()

    plt.figure(figsize=(10, 6))
    plt.scatter(frecuencia.index, frecuencia.values, s=100, color="teal")

    plt.title("Frecuencia de Libros por Categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Número de Libros")
   

    plt.tight_layout()
    plt.show()
