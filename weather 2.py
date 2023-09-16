import requests

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = '3fd651a2f7486508f45cdc4eef108e9f'

# Enter the city and country for which you want to get the weather forecast
city_name = input("Enter city name: ")
country_code = input("Enter country code (e.g., US): ")

# Make the API request
url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid=3fd651a2f7486508f45cdc4eef108e9f'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    
    print(f"Weather in {city_name}, {country_code}:")
    print(f"Description: {weather_description}")
    print(f"Temperature: {temperature}°F")
    print(f"Humidity: {humidity}%")
else:
    print("Failed to retrieve weather data")

