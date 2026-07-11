import requests

API_KEY = "282539aaead560ddafc580021bb8712e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
	url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=imperial"
	response = requests.get(url)
	if response.status_code == 200:
		return response.json()
	else:
		print(f"Failed to retrieve data {response.status_code}")
		return None

while True:
    print("\n====================================")
    city = input("Enter a city name (or type 'exit' to quit): ")		
    
    
    if city.lower() == 'exit':
        print("Goodbye! Thanks for using the weather app.")
        break
        
    weather_data = get_weather(city)

    if weather_data:
        main_info = weather_data["main"]
        weather_desc = weather_data["weather"][0]
        
        temp = main_info["temp"]
        humidity = main_info["humidity"]
        description = weather_desc["description"]
        
        print(f"\n--- Weather in {city.title()} ---")
        print(f"Temperature: {temp}°F")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {description.capitalize()}")
