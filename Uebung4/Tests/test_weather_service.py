"""
TDD-Template für Weather-API Service
====================================

TODO: Team A - Implementiert get_weather_category() testgetrieben!

Aufgabe:
- Funktion ruft Weather-API auf (mocken!)
- Extrahiert Temperatur aus JSON
- Gibt Kategorie zurück basierend auf Temperatur

Temperatur-Kategorien:
- < 0°C:      "frostgefahr"
- 0-10°C:     "kalt"
- 11-15°C:    "kühl"
- 16-24°C:    "angenehm"
- 25-30°C:    "warm"
- > 30°C:     "heiß"

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!

Dokumentiert eure Autorschaft: Wer hat welchen TDD-Schritt gemacht?
"""

import pytest
from unittest.mock import patch

# TODO: Team A - Import nach erster Implementierung:
from ..Code.weather_service import get_weather_category


class TestWeatherService:
    

   
    def test_angenehm(self):
        """TDD-Zyklus 1: RED von [CRVA] um [15:09]"""
        with patch('requests.get') as mock_get:
            # Simuliere API-Response
            mock_get.return_value.json.return_value = {"temperature": 20}
            
            result = get_weather_category("Berlin")
            assert result == "angenehm"
            
            # Optional: Verifiziere API-Aufruf
            # mock_get.assert_called_once()
    
    def test_api_verschiedene_werte(self):
        """TDD-Zyklus 2: [CRVA]"""
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {"temperature": 20}
            result = get_weather_category("Berlin")
            assert result == "angenehm"

            mock_get.return_value.json.return_value = {"temperature": 3}
            result = get_weather_category("Berlin")
            assert result == "kalt"

            mock_get.return_value.json.return_value = {"temperature": -3}
            result = get_weather_category("Berlin")
            assert result == "frostgefahr"

            mock_get.return_value.json.return_value = {"temperature": 36}
            result = get_weather_category("Berlin")
            assert result == "heiß"

            mock_get.return_value.json.return_value = {"temperature": 28}
            result = get_weather_category("Berlin")
            assert result == "warm"

            mock_get.return_value.json.return_value = {"temperature": 12}
            result = get_weather_category("Berlin")
            assert result == "kühl"

            # Optional: Verifiziere API-Aufrufe
            assert mock_get.call_count == 6
    



    def test_richtiger_api_aufruf(self):
        try:
            result = get_weather_category("Berlin")
            print(result)
        except Exception as e:
            print("API Fehler:", e) # mit pytest -s sieht man, dass der Zugang mit richtigem API-Aufruf nicht klappt


