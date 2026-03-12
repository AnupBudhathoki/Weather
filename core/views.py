from django.shortcuts import render
import requests
from django.contrib import messages

# Create your views here.
def index(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city="kathmandu"

    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf22686cf11682e29d657b984d138978"
    param={'units':'metric'}
    data=requests.get(url,param).json()

    img_url=f"https://api.unsplash.com/search/photos?query={city}&per_page=1&client_id=AocYclv8-7zt1nkxHU7cN4ZMEXoOoNvgBwIvjMYUufI"
    response=requests.get(img_url).json()
    

    try:
        temp=data['main']['temp']
        pressure=data['main']['pressure']
        humi=data['main']['humidity']
        wind=data['wind']['speed']
        desc=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        visibility=data['visibility']
        image=response['results'][0]['urls']['regular']

        context={
            'temp':temp,
            'wind':wind,
            'humi':humi,
            'city':city,
            'desc':desc,
            'icon':icon,
            'pressure':pressure,
            'visibility':visibility,
            'image':image
        }
    except:
        desc='no such city'
        messages.error(request,"City Error!!!!!")
        

        context={
            'desc':desc
        }


    return render(request, "index.html",context)
