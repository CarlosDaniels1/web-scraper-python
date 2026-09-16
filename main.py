import csv
import requests
from bs4 import BeautifulSoup

# 1. Dirección web de la tienda de práctica
url = "http://books.toscrape.com/"

# 2. Petición y procesamiento HTML con codificación UTF-8
respuesta = requests.get(url)
respuesta.encoding = "utf-8"
soup = BeautifulSoup(respuesta.text, "html.parser")

# 3. Extraemos todos los contenedores de libros
todos_los_libros = soup.find_all("article", class_="product_pod")

# 4. Crearemos y guardaremos los datos en un archivo CSV
with open("libros.csv", mode="w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)

    # Escribimos los encabezados de la tabla
    escritor.writerow(["Título", "Precio"])

    # Recorremos cada libro y guardamos las filas
    for libro in todos_los_libros:
        titulo = libro.h3.a["title"]
        precio = libro.find("p", class_="price_color").text

        # Escribimos una fila con el título y precio de cada libro
        escritor.writerow([titulo, precio])

print(
    "--- ¡DATOS GUARDADOS CON ÉXITO EN 'libros.csv'! ---"
)