import requests


def geolocalizacao(url_geolocalizacao, cidade):
    url = url_geolocalizacao
    params = {"name": cidade, "count": 10, "language": "en", "format": "json"}
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    dados = response.json()
    local = dados["results"][0]

    return (local["latitude"], local["longitude"], local["elevation"])


def previsao_tempo(url_previsao_tempo, latitude, longitude, elevation):
    url = url_previsao_tempo
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "elevation": elevation,
        "temperature_unit": "celsius",
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "wind_speed_10m_max",
            "precipitation_hours",
            "precipitation_sum",
        ],
        "hourly": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation_probability",
            "precipitation",
            "temperature_80m",
            "temperature_120m",
            "temperature_180m",
            "rain",
            "wind_speed_10m",
            "wind_speed_80m",
            "wind_speed_120m",
            "wind_speed_180m",
        ],
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
            "rain",
            "wind_speed_10m",
            "wind_gusts_10m",
        ],
        "timezone": "auto",
    }
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    dados = response.json()
    
    return dados
