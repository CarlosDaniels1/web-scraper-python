import requests
from bs4 import BeautifulSoup

# 1. Dirección web que vamos a consultar
url = "https://example.com"

# 2. Hacemos la petición a la página web
respuesta = requests.get(url)

# 3. Procesamos la respuesta con BeautifulSoup
soup = BeautifulSoup(respuesta.text, "html.parser")

# 4. Extraemos el título principal (etiqueta <h1>) y la descripción (etiqueta <p>)
titulo = soup.find("h1").text
parrafo = soup.find("p").text

# 5. Mostramos los resultados en la terminal
print("--- DATOS EXTRAÍDOS ---")
print("Título:", titulo)
print("Texto:", parrafo)