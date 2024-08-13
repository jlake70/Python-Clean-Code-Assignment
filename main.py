from Weather_Forecast import WeatherForecast

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
