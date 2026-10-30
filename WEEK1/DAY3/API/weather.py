
import requests
import json

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 14.4644,
    "longitude": 75.9218,
    "current": [
        "temperature_2m",
        "relative_humidity_2m",
        "wind_speed_10m"
    ]
}

try:
    # Send GET request
    response = requests.get(url, params=params, timeout=10)

    # Check HTTP status
    response.raise_for_status()

    # Convert JSON response into Python dictionary
    data = response.json()

    # Save response into JSON file
    with open("weather.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Weather data fetched successfully!")
    print("Temperature:", data["current"]["temperature_2m"])
    print("Humidity:", data["current"]["relative_humidity_2m"])
    print("Wind Speed:", data["current"]["wind_speed_10m"])

except requests.exceptions.Timeout:
    print("Error: Request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Check your internet connection.")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.RequestException as e:
    print("Request Error:", e)

except (ValueError, json.JSONDecodeError) as e:
    print("JSON Error:", e)

except OSError as e:
    print("File Error:", e)
