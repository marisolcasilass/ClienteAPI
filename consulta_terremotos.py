import requests

# Endpoint base de la API de la USGS para terremotos
url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

# Parámetros para la consulta
params = {
    "format": "geojson",          # Formato de respuesta
    "starttime": "2024-01-01",    # Fecha de inicio (YYYY-MM-DD)
    "endtime": "2024-10-28",      # Fecha de fin
    "minmagnitude": 5.0           # Magnitud mínima de los terremotos
}

# Realizar la solicitud GET
response = requests.get(url, params=params)

# Verificar el estado de la respuesta
if response.status_code == 200:
    data = response.json()
    # Procesar los datos obtenidos
    print("Eventos sísmicos obtenidos:")
    for event in data["features"]:
        properties = event["properties"]
        print(f"Ubicación: {properties['place']}")
        print(f"Magnitud: {properties['mag']}")
        print(f"Fecha y hora: {properties['time']}")
        print("------------")
else:
    print(f"Error en la solicitud: {response.status_code}")
