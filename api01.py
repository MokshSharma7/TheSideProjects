import requests

api_key = "2b9e90c599c1041bc792ff8cf00a8c64"
base_url= "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):

    params = {
        "q": city_name,       # City name
        "appid": "2b9e90c599c1041bc792ff8cf00a8c64",     # API key
        "units": "metric"     # Use 'metric' for Celsius, 'imperial' for Fahrenheit
    }

    response = requests.get(base_url,params=params)

    if response.status_code == 200:
        data=response.json()
        main=data["main"]
        weather=data["weather"][0]

        temperature = main["temp"]
        feels_like= main['feels_like']
        humidity= main['humidity']
        weather_description=weather['description']
 
        print(f"Weather in {city_name.capitalize()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description.capitalize()}")
    else:
        print(f"Error: Unable to fetch weather data for '{city_name}'. Please check the city name or API key.")

# Main program
if __name__ == "__main__":
    print("Welcome to the Weather App!")
    city = input("Enter the name of the city: ")
    get_weather(city)