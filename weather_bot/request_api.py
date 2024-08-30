import requests


#---------------------------Tarjima qilinmagani-----------------------------
# def weather(city):
#     API_KEY = "faf1b0e5cc92c7c666c125b5c957e65f"
#     URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"

#     response = requests.get(URL)
#     if response.status_code == 200:
#         data = response.json()
#         harorat = data['main']['temp']
#         holat = data['weather'][0]['description']
#         if city == 'Khiva':
#             return f"<b>Xorazm</b>, ya'ni <b>Xiva</b>dagi havo harorati: <b>{harorat}°C,</b> Holat: <b>{holat}</b>"
#         if city == "Termiz":
#             return f"<b>Surxondaryo</b>, ya'ni <b>Termiz</b>dagi havo harorati: <b>{harorat}°C</b>, Holat: <b>{holat}</b>"
#         if city == "Nukus":
#             return f"<b>Qoraqalpog'iston Respublikasi</b>, ya'ni <b>Nukus</b>dagi havo harorati: <b>{harorat}°C</b>, Holat: <b>{holat}</b>"
#         else:
#             return f"<b>{city.capitalize()}</b>dagi havo harorati: <b>{harorat}°C</b>, Holat: <b>{holat}</b>"
#     else:
#         return "Ob-havo ma'lumotlarini olishda xato yuz berdi."
    
# print(weather('Samarqand'))



#---------------------------Tarjima qilingani-----------------------------
weather_conditions = {
    "clear": "Ochiq",
    "clouds": "Bulutli",
    "rain": "Yomg'ir",
    "snow": "Qor",
    "mist": "Tuman",
    "clear sky" : "Musaffo osmon",
    "few clouds" : "Kam bulutlar",
    "thunderstorm" : "Momaqaldiroq",
    "ясно": "Ochiq",
    "облачно": "Bulutli",
    "дождь": "Yomg'ir",
    "снег": "Qor",
    "туман": "Tuman",
    "пасмурно": "Asosan bulutli",
    "небольшой снег": "Yengil qor",
    "небольшой снегопад": "Yengil qor yog'adi",
    "облачно с прояснениями": "Qisman bulutli"
    # Qo'shimcha holatlar
}

def weather(city):
    API_KEY = "YOUR_API_KEY"
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"  # yoki lang=en

    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        harorat = data['main']['temp']
        holat_key = data['weather'][0]['description']
        # Tarjima qilish
        holat = weather_conditions.get(holat_key, "Ma'lumot mavjud emas")
        if city == 'Khiva':
            return f"<b>Xorazm</b>, ya'ni <b>Xiva</b>dagi havo harorati: <b>{harorat}°C,</b>\nHolat: <b>{holat}</b>"
        if city == "Termiz":
            return f"<b>Surxondaryo</b>, ya'ni <b>Termiz</b>dagi havo harorati: <b>{harorat}°C</b>,\nHolat: <b>{holat}</b>"
        if city == "Nukus":
            return f"<b>Qoraqalpog'iston Respublikasi</b>, ya'ni <b>Nukus</b>dagi havo harorati: <b>{harorat}°C</b>,\nHolat: <b>{holat}</b>"
        else:
            return f"<b>{city.capitalize()}</b>dagi havo harorati: <b>{harorat}°C</b>,\nHolat: <b>{holat}</b>"
    else:
        return "Ob-havo ma'lumotlarini olishda xato yuz berdi."
    




#---------------------------------Bir kunlik--------------------------

# def get_daily_weather(city, lat, lon):
#     API_KEY = "dd8819d964d19f2fe5f41f5b720c8edf"
#     URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=hourly,minutely,current,alerts&appid={API_KEY}&units=metric&lang=ru"

#     response = requests.get(URL)
#     print(response.status_code)
#     print(response.text)

#     # if response.status_code == 200:
#     #     data = response.json()
#     #     daily_weather = data['daily'][0]  # Bugungi kun
#     #     max_temp = daily_weather['temp']['max']
#     #     min_temp = daily_weather['temp']['min']
#     #     condition = daily_weather['weather'][0]['description']
#     #     return f"<b>{city.capitalize()}</b>dagi bugungi maksimal harorat: <b>{max_temp}°C</b>, minimal harorat: <b>{min_temp}°C</b>, Holat: <b>{condition}</b>"
#     # else:
#     #     return "Ob-havo ma'lumotlarini olishda xato yuz berdi."

# # Misol uchun, Toshkent shahri uchun bugungi ob-havo ma'lumotlarini olish
# # Toshkentning geografik koordinatalari: kenglik (lat) 41.2995 va uzunlik (lon) 69.2401
# print(get_daily_weather("Toshkent", 41.2995, 69.2401))

