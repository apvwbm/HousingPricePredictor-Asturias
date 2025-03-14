import requests
import pandas as pd

# URL base de la API de Nestoria
BASE_URL = "https://api.nestoria.es/api"

# Parámetros iniciales
params = {
    "encoding": "json",
    "pretty": 1,
    "action": "search_listings",
    "country": "es",
    "listing_type": "buy",  # Compra (equivale a "comprar")
    "place_name": "principado-de-asturias",  # Ubicación
    "property_type": "house",  # Tipo de inmueble (equivale a "casa")
    "page": 1,  # Página inicial
}

# Lista para almacenar todos los resultados
all_results = []

# Función para procesar una página de resultados
def fetch_page(page):
    params["page"] = page
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        listings = data.get("response", {}).get("listings", [])
        return listings
    else:
        print(f"Error al obtener datos: {response.status_code}")
        return []

# Bucle para recorrer múltiples páginas
page = 1
while True:
    print(f"Obteniendo página {page}...")
    listings = fetch_page(page)
    
    # Si no hay más resultados, detener el bucle
    if not listings:
        print("No hay más resultados.")
        break
    
    # Procesar cada anuncio
    for listing in listings:
        result = {
            "Título": listing.get("title", ""),
            "Tipo de inmueble": listing.get("property_type", ""),
            "Precio": listing.get("price_formatted", "").replace("€", "").replace(".", "").strip(),
            "Metros cuadrados construidos": listing.get("size", ""),
            "Habitaciones": listing.get("bedroom_number", ""),
            "Baños": listing.get("bathroom_number", ""),
            "Barrio": listing.get("area", ""),
            "Municipio": listing.get("location", ""),
            "Latitud": listing.get("latitude", ""),
            "Longitud": listing.get("longitude", ""),
            "URL": listing.get("lister_url", ""),
        }
        all_results.append(result)
    
    # Incrementar la página
    page += 1

# Crear un DataFrame con los resultados
if all_results:
    df = pd.DataFrame(all_results)

    # Limpiar columnas numéricas
    df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce")
    df["Metros cuadrados construidos"] = pd.to_numeric(df["Metros cuadrados construidos"], errors="coerce")
    df["Habitaciones"] = pd.to_numeric(df["Habitaciones"], errors="coerce")
    df["Baños"] = pd.to_numeric(df["Baños"], errors="coerce")

    # Guardar en un archivo CSV
    df.to_csv("nestoria_asturias.csv", index=False)
    print("Datos guardados en 'nestoria_asturias.csv'")
else:
    print("No se encontraron datos para guardar.")