import requests
import json
from datetime import datetime

# Coordenadas de Barcelona
latitud = 41.3888
longitud = 2.159

# URL API Open-Meteo
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&hourly=temperature_2m&forecast_days=1"

# Petición API
response = requests.get(url)

# Convertir respuesta JSON
data = response.json()

# Obtener temperaturas del día
temperaturas = data["hourly"]["temperature_2m"]

# Calcular temperatura máxima
temp_max = max(temperaturas)

# Calcular temperatura mínima
temp_min = min(temperaturas)

# Calcular temperatura media
temp_media = sum(temperaturas) / len(temperaturas)

# Fecha actual
fecha = datetime.now().strftime("%Y%m%d")

# Crear diccionario resultado
resultado = {
    "fecha": fecha,
    "temperatura_maxima": temp_max,
    "temperatura_minima": temp_min,
    "temperatura_media": round(temp_media, 2)
}

# Nombre archivo JSON
nombre_archivo = f"temp_{fecha}.json"

# Guardar JSON
with open(nombre_archivo, "w") as archivo:
    json.dump(resultado, archivo, indent=4)

print("Archivo JSON generado correctamente")
print("Nombre:", nombre_archivo)