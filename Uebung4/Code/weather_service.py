"""
Implementierung: Weather-API Service
====================================

TODO: Team A - Implementiert get_weather_category() hier!

Die Funktion soll:
1. Weather-API aufrufen (in Tests gemockt)
2. Temperatur extrahieren
3. Kategorie zurückgeben

Hinweise:
- Nutzt requests.get() für API-Aufrufe
- API-URL: https://api.weather.com/current?city={city}
- Response-Format: {"temperature": 20}
- Startet mit minimalster Implementierung!
"""

import requests


def get_weather_category(city: str) -> str:
    """
    Ruft Weather-API auf und gibt Temperatur-Kategorie zurück
    
    Args:
        city: Stadt, für die das Wetter abgefragt wird
        
    Returns:
        Temperatur-Kategorie als String:
        - "frostgefahr" (< 0°C)
        - "kalt" (0-10°C)
        - "kühl" (11-15°C)
        - "angenehm" (16-24°C)
        - "warm" (25-30°C)
        - "heiß" (> 30°C)
    """
    
    # # Test 1: 
    # return "angenehm"
    
    
    # Test 2: 
    # API-Call-Code:
    url = f"https://api.weather.com/current?city={city}"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    temperature = data.get("temperature")
    print(data) # mit pytest -s sichtbar     
    return get_category_string(temperature)


def get_category_string(value: int) -> str: 
    if value > 30: 
        return "heiß"
    elif value >= 25: 
        return "warm"
    elif value >= 16: 
        return "angenehm"
    elif value >= 11: 
        return "kühl"
    elif value >= 0: 
        return "kalt"
    else: 
        return "frostgefahr"