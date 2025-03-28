import requests 

# Step 1: API Key aur URL set karo
API_KEY = '666fa5ac53c4dcaac91e04e0acd18e03'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'
GEO_URL = 'http://api.openweathermap.org/geo/1.0/direct'

# Step 2: Function to validate city using Geocoding API
def validate_city(city):
    url = f"{GEO_URL}?q={city}&limit=1&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    # Debug ke liye response dekho
    #print(f"\n📢 Geocoding Response: {data}")

    if data:
        # Sirf India ke cities ko allow karo
        if data[0]['country'] == 'IN':          #🌍 API me country code ke liye ISO 3166-1 alpha-2 codes ka use hota hai. EX: IN/US/CN/GB etc.
            return data[0]['name']
        else:
            print(f"❌ '{city}' is not an Indian city. 🚫")
            return None
    else:
        return None

# Step 3: Function to get weather data
def get_weather(city):
    try:
        # City validate karo pehle
        valid_city = validate_city(city)
        if not valid_city:
            print(f"❌ '{city}' is not a valid city name. 🚫")
            return
        
        print(f"\n🌏 Fetching weather details for '{valid_city}'... 🌏")
        url = f"{WEATHER_URL}?q={valid_city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get('cod') == 200:
            temp = data['main']['temp']
            condition = data['weather'][0]['description']
            humidity = data['main']['humidity']
            country = data['sys']['country']
            
            print(f"\n📍 Weather in 🌆 **{data['name']}, {country}**:")
            print(f"🌡️  Temperature: {temp}°C")
            print(f"🌥️  Condition: {condition.capitalize()}")
            print(f"💧  Humidity: {humidity}%")
        else:
            print("❌ City not found! Please try again. 🚫")
    
    except Exception as e:
        print(f"❌ Error occurred: {e}")

# Step 4: Main function to get user input
def main():
    while True:
        ask_user = input("\nDo you want to check weather details in your city? (yes/no): ").strip().lower()

        if ask_user == "yes":
            city = input("🏙️ Enter city name: ").strip()
            if city:
                get_weather(city)
            else:
                print("⚠️ City name cannot be empty!")
        elif ask_user == "no":
            print("Ok! Bye 🙋‍♂️")
            break
        else:
            print("⚠️ Please enter 'yes' or 'no' only!")

# Step 5: Start the program
if __name__ == "__main__":
    main()