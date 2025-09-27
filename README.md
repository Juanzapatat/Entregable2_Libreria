# 📚 Proyecto de Análisis de Datos de Librería con Pandas

Este proyecto realiza la limpieza, el preprocesamiento y un análisis exploratorio inicial de dos conjuntos de datos relacionados: **Libros** y **Clientes** de una librería, utilizando la biblioteca **Pandas** en Python.

## 🎯 Objetivo del Proyecto

El objetivo principal es transformar los datos crudos, que contienen inconsistencias y formatos variados, en una estructura limpia y estandarizada, para luego responder preguntas clave sobre el inventario y las ventas de la librería.

## ⚙️ Estructura de Archivos

El proyecto se divide en dos módulos principales:
1.  **`preprocesamiento.py`**: Contiene las funciones para la limpieza y preparación de los datos.
2.  **`analisis.py`**: Carga los datos, aplica las funciones de preprocesamiento y realiza el análisis exploratorio final.

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
