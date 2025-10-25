
# 📚 Proyecto de Análisis de Datos de Librería con Pandas

Este proyecto realiza la limpieza, el preprocesamiento, un análisis, visualizacion y genera reportes html exploratorio inicial de dos conjuntos de datos relacionados: **Libros** y **Clientes** de una librería, utilizando la biblioteca **Pandas y matplotlib** en Python.

## 🎯 Objetivo del Proyecto

El objetivo principal es transformar los datos crudos, que contienen inconsistencias y formatos variados, en una estructura limpia y estandarizada, para luego responder preguntas clave sobre el inventario y las ventas de la librería.

Al igual tener la capacidad de generar reporte html empapandose del analisis que se hizo en el anterior cambio y tambien graficar ya sean barras, puntos, tortas etc.. usando matplotlib

## ⚙️ Estructura de Archivos

El proyecto se divide en cuatro módulos principales:
1.  **`preprocesamiento.py`**: Contiene las funciones para la limpieza y preparación de los datos.
2.  **`analisis.py`**: Carga los datos, aplica las funciones de preprocesamiento y realiza el análisis exploratorio final.
3.  **`visualizacion.py`**: Define las funciones que generan los gráficos con Matplotlib.
4.  **`generar_reporte.py`**: Produce un reporte HTML que incluye tablas y resultados del análisis, generando una vista de ventas por categoría.



## 🧹 Fases de Preprocesamiento de Datos (Data Cleaning)

Se aplicaron las siguientes transformaciones al DataFrame de libros para asegurar la calidad de los datos:

### 1. Manejo de Valores Faltantes (`manejar_nulos`)
* Se reemplazaron las celdas vacías o con solo espacios en blanco por el valor estándar **`NaN`** (Not a Number).
* Se rellenaron los `NaN` en columnas clave con valores por defecto (ej. `"Sin nombre"`, `"Anónimo"`, o un precio promedio de `20.000`).

### 2. Estandarización de Formato de Texto (`estandarizar_texto`)
* Se estandarizaron las columnas de texto (`nombre_libro`, `categoria`, `autor`) a **minúsculas** y se eliminaron los **espacios en blanco** superfluos al inicio y final de las cadenas. Esto garantiza que las categorías y nombres se cuenten correctamente.

### 3. Normalización de la Columna de Precios (`eliminar_simbolos`)
* Se eliminaron símbolos y unidades de medida no numéricas (como `$`, `kg`, `g`, `ml`) de las columnas de precio y de nombre de libro para poder convertirlas al tipo de dato numérico.
* Posteriormente, la columna **`precio`** se convirtió al tipo **numérico** (`float`) para permitir cálculos.

### 4. Eliminación de Duplicados (`eliminar_duplicados`)
* Se identificaron y eliminaron filas duplicadas basadas únicamente en el `nombre_libro`, asumiendo que el mismo libro no debe tener múltiples registros idénticos.

## 📊 Análisis Exploratorio y Preguntas Respondidas

Una vez limpios y preparados, los datos se analizaron para obtener las siguientes ideas:

### 1. Análisis de Frecuencias
* **Libro más repetitivo:** Se identificó el título de libro con la mayor frecuencia en el inventario/ventas utilizando **`.value_counts().idxmax()`**.
* **Cliente con más libros:** Se determinó el `id_cliente` con la mayor cantidad de libros y se unió con la tabla de clientes para mostrar su nombre completo.

### 2. Agrupación (Group By)
* **Ventas totales por categoría:** Se utilizó **`.groupby("categoria")["precio"].sum()`** para calcular la suma de los precios de venta por cada categoría de libro (ej. Novela, Misterio, Teatro), lo que indica la categoría que genera más ingresos.

### 3. Filtrado
* **Libros más baratos:** Se filtraron los registros donde el `precio` fuera **menor a 15** unidades, y se contó y listó la cantidad de libros que cumplen con esta condición.

### 4. Unión de Datos (Merge)
* Se combinó el `DataFrame` de `df_libros` con el de `df_clientes` utilizando **`pd.merge(..., on='id_cliente', how='left')`**. Esta operación crea un conjunto de datos único que asocia la información de cada libro con el nombre y detalles del cliente que lo compró.

##  🎨 Fase de Visualización con Matplotlib

En esta etapa, se incorporan gráficos para visualizar los resultados del análisis y mejorar la interpretación de los datos.

### Funciones de Visualización
 Dentro del módulo visualizacion.py se definen dos funciones principales:

- **graficar_ventas_por_categoria(df_libros)**

Genera un gráfico de barras con el Top 5 de categorías con mayores ventas, basado en el total de precios sumados. Este gráfico permite identificar las categorías más rentables.

- **graficar_frecuencia_libroscategorias(df_libros)**

Crea un gráfico de puntos que muestra las categorías con máyor frecuencia de libros, reflejando la diversidad y presencia de cada tipo de libro.
 
 ## 📜 Generación del Reporte HTML

El módulo generar_reporte.py se encarga de producir un reporte HTML a partir de un DataFrame, convirtiendo los datos en una tabla visual mediante el método to_html() de Pandas.

**Este reporte incluye:**

- Una tabla principal con la información de los libros analizados.

- Un diseño con estilo básico para mejorar la legibilidad y presentación.

 
 ```
<script>
         
    document.addEventListener("DOMContentLoaded", function () {
      const filas = document.querySelectorAll("table tr");
      filas.forEach(fila => {
        fila.addEventListener("mouseenter", () => fila.style.backgroundColor = "#dfe6e9");
        fila.addEventListener("mouseleave", () => fila.style.backgroundColor = "");
      });
    });
  

        </script>


