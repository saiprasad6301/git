import requests

def get_weather(city):
    api_key = "your_openweathermap_api_key_here"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] != 200:
            print("City not found.")
        else:
            print(f"City: {data['name']}")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Weather: {data['weather'][0]['description']}")
    except Exception as e:
        print("Error occurred:", e)

while True:
    city = input("\nEnter city name (or 'exit' to quit): ")
    if city.lower() == "exit":
        break
    get_weather(city)

