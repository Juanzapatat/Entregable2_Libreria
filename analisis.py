import pandas as pd

#Carga de funciones del archivo preprocesamiento.py

from preprocesamiento import cargar_datos ,manejar_nulos, estandarizar_texto, eliminar_duplicados, eliminar_simbolos
from visualizacion import graficar_ventas_por_categoria, graficar_frecuencia_libroscategorias
from generar_reporte import generar_reporte_html

df_libros, df_clientes = cargar_datos("data/libros.csv" , "data/usuarios.csv")

df_libros = manejar_nulos(df_libros)
df_libros = estandarizar_texto(df_libros)
df_libros = eliminar_duplicados(df_libros, ["nombre_libro"])
df_libros = eliminar_simbolos(df_libros, ["nombre_libro" , "precio"])


print(df_libros.head(10))

print(f"\n{df_clientes.head(10)}")

 


print("\nAnalisis Frecuencias")


libro_mas_repetitivo = df_libros["nombre_libro"].value_counts().idxmax()
print(f"\nEl libro repetido es: {libro_mas_repetitivo}")

cliente_libros = df_libros["id_cliente"].value_counts().idxmax()
cliente_nombre = df_clientes[df_clientes["id_cliente"] == cliente_libros][["id_cliente","nombre","apellido"]].values[0]
print(f"Cliente con mas libros: ID: {cliente_nombre[0]} {cliente_nombre[1]} {cliente_nombre[2]}")



print("\nAnalisis Agrupacion")

df_libros["precio"] = pd.to_numeric(df_libros["precio"], errors="coerce")
ventas_por_categoria = df_libros.groupby("categoria")["precio"].sum()
print("\nVentas totales por categoria:")
print(ventas_por_categoria)

generar_reporte_html(ventas_por_categoria)



print("\nAnalisis Filtrado")

df_libros["precio"] = pd.to_numeric(df_libros["precio"], errors="coerce")

libros_mas_baratos = df_libros[df_libros["precio"] < 15]

print(f"Libros con precio más bajo a 15$: {libros_mas_baratos.shape[0]} libros")


print("\nLista de libros más baratos:")
print(libros_mas_baratos[["nombre_libro", "precio"]].to_string(index=False))

graficar_ventas_por_categoria(df_libros)
graficar_frecuencia_libroscategorias(df_libros)



print("\nMerge(Union de usuario y clientes)")

df_completo = pd.merge(df_libros, df_clientes, on = 'id_cliente', how='left')


print(f"\n{df_completo}" )





