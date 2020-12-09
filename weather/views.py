from django.http.response import HttpResponse
from the_weather.local_settings import API_KEY
import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm


def index(request):
    # Logic to add a new city
    if request.method == "POST":
        form = CityForm(request.POST)
        # The save should validate as well ( instead of using the validate pattern )
        form.save()

    form = CityForm()
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        # Make sure to add your api key from openweathermap.org
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city.name}&units=metric&appid={API_KEY}"

        try:
            r = requests.get(url).json()

            city_weather = {
                'city': city.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
            weather_data.append(city_weather)
        except Exception as e:
            print(e)
            print(f'failed to collect data for city: {city.name}')

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)


def delete(request, pk):
    city = City.objects.get(pk=pk)
    # city.delete()

    return HttpResponse(request, "Test")
