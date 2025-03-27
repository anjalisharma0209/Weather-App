import requests

# Step 1: API Key aur URL set karo
API_KEY = '666fa5ac53c4dcaac91e04e0acd18e03'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Step 2: Function to get weather data
def get_weather(city):
        try:
            if not city:
                print("⚠️ City name cannot be empty.")
                return 
            
            print(f"\n🌏 Fetching weather details in {city}...🌏")
            url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()

            if data['cod'] == 200:
                temp = data['main']['temp']
                condition = data['weather'][0]['description']
                humidity = data['main']['humidity']
                
                #print(f"\n📍 Weather in {city}:\n")
                print(f"\n🌡️  Temperature: {temp}°C")
                print(f"🌥️  Condition: {condition}")
                print(f"💧  Humidity: {humidity}%")
                
            else:
                print("❌ City not found! Please try again. 🚫")
        
        except Exception as e:
            print(f"❌ Error occurred:{e}")

def main():
    while True:
        ask_user = input("\nDo you want to check weather details in your city? (yes/no): ").strip().lower()

        if ask_user == "yes":
            city = input("🏙️ Enter city name: ")
            get_weather(city)
        elif ask_user == "no":
            print("Ok! Bye 🙋‍♂️")
            break
        else:
            print("⚠️ Please enter 'yes' or 'no' only!")

# Step 3: User se input lena
if __name__ == "__main__":
    main()