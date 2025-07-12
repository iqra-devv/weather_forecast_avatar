import requests
import time
from avatar import Avatar

from dotenv import load_dotenv
import os

load_dotenv(".config")

API_KEY = os.getenv("WEATHER_API_KEY")


# make  function
def get_location_by_ip():
    print("Wait we are fetching your location by IP address...")
    ip = requests.get("https://api.ipify.org").text

   
    request = requests.get(f"http://ip-api.com/json/{ip}")
    data = request.json()

    print(f"IP: {data['query']}")
    city = data['city']
    return city
    

def get_weather(city):
    try:
        URL = f"https://api.weatherapi.com/v1/current.json?q={city}"

        response = requests.get(URL,headers={'key': API_KEY})
        
        if response.status_code !=200:
            print("ERROR fatching data from API")

        data = response.json()
        locaton_name = data['location']['name']
        temp = data['current']['temp_c']
        return locaton_name,temp
    
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None, None
    except KeyError as e:
        print("Unexpected data format from API:", e)
        return None, None   
    except Exception as e:
        print("An unexpected error occurred:", e)
        return None, None
 

def get_outfit(temp):
    outfit_flags = {'gloves': False, 'shoes': False, 'cap': False , 'jacket': False, 'scarf': False, 'pants': False, 'tshirt': False, 'shorts': False, }
    if(temp < 0):
        outfit_flags['gloves'] = True
        outfit_flags['shoes'] = True
        outfit_flags['jacket'] = True
        outfit_flags['scarf'] = True
        return  "Heavy jacket, gloves, scarf, boots", outfit_flags
    elif(temp < 10):
       outfit_flags['pants'] = True
       outfit_flags['jacket'] = True
       return "Jacket, jeans", outfit_flags
    elif(temp < 20):
        outfit_flags['jacket'] = True
        outfit_flags['pants'] = True
        return "Light jacket, long pants", outfit_flags
    elif(temp < 30):
        outfit_flags['tshirt'] = True
        outfit_flags['pants'] = True
        return "T-shirt, jeans", outfit_flags  
    else:
        outfit_flags['shorts'] = True
        outfit_flags['tshirt'] = True
        outfit_flags['cap'] = True
        return "Shorts, T-shirt, cap", outfit_flags


def main():
   
    city = get_location_by_ip()

  
    print(f"Fetching weather information for {city}...")
    if not city:
        print("Could not determine your city. Exiting.")
        return
    
    while True:

        location_name,temp = get_weather(city)

        if location_name and temp is not None:
            print(f"current temperature in {location_name} is {temp}°C")
            outfit, outfit_flags = get_outfit(temp)
            print(f"So, Recommanded outfit is: {outfit}")
            avatar = Avatar()
            avatar.draw_character(outfit_flags)
            avatar.stayopen()
           
        else:
            print("failed to get weather information. Please try again later")

        print("wait for 4 hours")
        time.sleep(14400)
if __name__ == "__main__":
    main()
