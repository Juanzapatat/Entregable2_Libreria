# pythonConGitFlow

Proyecto en Python que permite realizar preprocesamiento y análisis de datos de una librería a partir de archivos CSV de clientes y libros.

📖 Descripción

El proyecto se desarrolla en dos etapas principales:

Preprocesamiento (preprocesamiento.py)

Limpieza de datos.
Estandarización de campos.
Eliminación de registros duplicados.

Análisis (analisis.py)

Frecuencia:
¿Cuál es el libro más repetido?
¿Cuál es el cliente que más libros pidió?
Agrupación:
Total del precio por categoría.
Filtrado y conteo:
¿Cuántos libros tienen un precio menor a 15 USD?
Listado de libros disponibles.
Merge (unión):
Unión de información entre clientes y libros según un ID compartido.
📂 Estructura del proyecto
├── data/                 # Archivos CSV de clientes y libros
├── analisis.py           # Script de análisis de datos
├── preprocesamiento.py   # Script de preprocesamiento
├── README.md             # Documentación del proyecto
└── .gitignore

⚙️ Instalación

Clonar el repositorio:

git clone https://github.com/tuusuario/Entregable2_Libreria.git
cd Entregable2_Libreria


Instalar dependencias (ejemplo con pandas):

pip install pandas

▶️ Uso

Ejecutar el preprocesamiento:

python preprocesamiento.py


Ejecutar el análisis:

python analisis.py

✨ Tecnologías utilizadas
Python 3
Pandas
📌 Notas

Este proyecto corresponde a un entregable académico en el que se aplican conceptos básicos de preprocesamiento y análisis de datos con Python.