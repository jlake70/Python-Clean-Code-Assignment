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

def main():
    
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break

        weather_forecast = WeatherForecast(city)
        
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = weather_forecast.get_detailed_forecast()
        else:
            forecast = weather_forecast.display_weather()
        print(forecast)

if __name__ == "__main__":
    main()
