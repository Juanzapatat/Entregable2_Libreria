import pandas as pd
import numpy as np

def cargar_datos(ruta_libros, ruta_clientes):
	df_libros = pd.read_csv(ruta_libros, on_bad_lines='skip')
	df_clientes = pd.read_csv(ruta_clientes, on_bad_lines='skip')
	return df_libros, df_clientes


def manejar_nulos(df_libros):
    
    df_libros = df_libros.replace(r'^\s*$', np.nan, regex=True)
    
    df_libros = df_libros.fillna({
        "nombre_libro": "Sin nombre",
        "precio": 20.000, 
        "categoria": "Desconocida",
        "autor": "Anónimo"
    })
    return df_libros



def estandarizar_texto(df_libros):
    
    columnas = ["nombre_libro", "categoria", "autor"]
    for col in columnas:
        if col in df_libros.columns:
            df_libros[col] = df_libros[col].astype(str).str.strip().str.lower()
    
    
    
    return df_libros


def eliminar_duplicados(df_libros, columnas):
  return df_libros.drop_duplicates(subset=columnas)


def eliminar_simbolos(df_libros, columnas):
    simbolos = ["$", "kg", "gr", "g", "ml", "cm", "mt"]
    for col in columnas:
        if col in df_libros.columns:
            df_libros[col] = df_libros[col].astype(str)
            for s in simbolos:
                df_libros[col] = df_libros[col].str.replace(s, "", regex=False)
            df_libros[col] = df_libros[col].str.strip()
    return df_libros
 
 
    
    





