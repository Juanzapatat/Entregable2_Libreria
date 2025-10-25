import pandas as pd

def generar_reporte_html(ventas_por_categoria, nombre_archivo="reporte.html"):
   

   
    tabla_ventas = ventas_por_categoria.reset_index()
    tabla_ventas.columns = ["Categoría", "Ventas Totales ($)"]

   
    tabla_html = tabla_ventas.to_html(index=False, border=0, classes="tabla")

    html_contenido = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Reporte de Ventas por Categoria</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                color: #333;
                margin: 40px;
            }}
            h1 {{
                text-align: center;
                color: #2c3e50;
            }}
            table {{
                border-collapse: collapse;
                margin: 0 auto;
                width: 60%;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            th, td {{
                border: 1px solid #ccc;
                padding: 10px;
                text-align: center;
            }}
            th {{
                background-color: #16a085;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #ecf0f1;
            }}
        </style>
    </head>
    <body>
        <h1> Reporte de Ventas Totales por Categoria</h1>
        {tabla_html}

        <script>


        </script>
    </body>
    </html>
    """

    with open(nombre_archivo, "w") as f:
        f.write(html_contenido)

    print(f"\nReporte generado correctamente: {nombre_archivo}")

