import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if "main" in weather_data:
        main_info = weather_data["main"]
        temperature = main_info.get("temp")
        description = weather_data["weather"][0]["description"]
        print(f'Temperature in {city}: {temperature}°C, Description: {description}')
    else:
        print(f'City not found or weather data not available: {city}')

if __name__ == "__main__":
    api_key = 'Enter api key'
    city = input("Enter city name: ")
    
    get_weather(api_key, city)

