import requests

def fetch_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    # Check if the API returned an error
    if response.status_code != 200:
        raise Exception(f"API Error: {data.get('message', 'Unknown error')}")

    # Ensure required fields are present
    if 'main' not in data or 'wind' not in data or 'weather' not in data:
        raise Exception("Invalid API response: Missing required fields")

    return data