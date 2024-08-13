class WeatherForecast:
    def __init__(self, city):
        self.city = city
        self.weather_data = self.fetch_weather_data()

    def fetch_weather_data(self):
        
        print(f"Fetching weather data for {self.city}...")
        
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(self.city, {})

    def parse_weather_data(self):
        
        if not self.weather_data:
            return "Weather data not available"
        city = self.weather_data["city"]
        temperature = self.weather_data["temperature"]
        condition = self.weather_data["condition"]
        humidity = self.weather_data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

    def get_detailed_forecast(self):

        return self.parse_weather_data()

    def display_weather(self):
    
        if not self.weather_data:
            return f"Weather data not available for {self.city}"
        else:
            return self.parse_weather_data()

