import requests
import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim

def get_weather(city):
    api_key = "b343a139ba2825ed14b6f1610c9d136e" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_info = (
            f"{data['main']['temp']}°C\n"
            f"{data['weather'][0]['description'].capitalize()}\n"
            f"{city}, {data['sys']['country']}\n"
            f"Feels like: {data['main']['feels_like']}°C\n"
            f"Humidity: {data['main']['humidity']}%"
        )
        weather_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", "Could not retrieve weather data. Please check the city name.")

def get_location_weather():
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode("Kathmandu, Nepal")  # Default location
    if location:
        get_weather(location.address.split(",")[0])

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")

tk.Label(root, text="Weather App", font=("Arial", 16, "bold")).pack()
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack()

tk.Button(root, text="Get Weather", command=lambda: get_weather(city_entry.get())).pack()
tk.Button(root, text="Get Device Location", command=get_location_weather).pack()

weather_label = tk.Label(root, text="", font=("Arial", 14), justify="center")
weather_label.pack()

root.mainloop()