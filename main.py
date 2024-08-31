from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    try:
        city = text.get()


        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)


        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")


        lat = location.latitude
        lon = location.longitude
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=450677898e8e0a8f020dd3dae9530063&units=metric"


        json_data = requests.get(api).json()

        if 'weather' in json_data and 'main' in json_data:
            # Extract weather data
            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp'])
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']

            # Update labels
            t.config(text=f"{temp}°C")
            c.config(text=f"{condition} | FEELS LIKE {temp}°C")
            w.config(text=wind)
            h.config(text=humidity)
            d.config(text=description)
            p.config(text=pressure)
        else:
            messagebox.showerror("Weather App", "Weather data not found for this location.")

    except Exception as e:
        messagebox.showerror("Weather App", f"Invalid Entry or Error: {e}")


search_image= PhotoImage(file="Copy of search.png")
myimage=Label(image=search_image)
myimage.place(x=20,y=20)

text=tk.Entry(root,justify="left",width=17,font=("poppins",20),bg="#404040",border=0,fg="#fff")
text.place(x=50,y=40)
text.focus()

search_icon=PhotoImage(file='icons8-search-50.png')
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
myimage_icon.place(x=400,y=34)

logo_image=PhotoImage(file='Copy of logo.png')
logo=Label(image=logo_image)
logo.place(x=150,y=100)

Frame_image=PhotoImage(file="Copy of box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

name=Label(root,font=('arial',15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=('Helvetica',20))
clock.place(x=30,y=130)

label1=Label(root,text="WIND",font=('helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=('helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=('helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=('helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label4.place(x=650,y=400)

t=Label(font=('arial',70,'bold'),fg='#ee666d')
t.place(x=400,y=150)
c=Label(font=('arial',15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=('arial',20,'bold'),bg='#1ab5ef')
w.place(x=120,y=430)

h=Label(text="...",font=('arial',20,'bold'),bg='#1ab5ef')
h.place(x=280,y=430)

d=Label(text="...",font=('arial',20,'bold'),bg='#1ab5ef')
d.place(x=430,y=430)

p=Label(text="...",font=('arial',20,'bold'),bg='#1ab5ef')
p.place(x=670,y=430)

root.mainloop()
