from django.shortcuts import render
from django.template.response import TemplateResponse
import xmltodict
import urllib.request

# Create your views here.
def get_data(request):
    if request.method ==  'POST':
        city_name = request.POST['city']
        response_xml = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&mode=xml&appid=9575a6b0be31e2052f17b15b1700603f&units=metric').read()
        response_dict = xmltodict.parse(response_xml)
        temp = float(response_dict['current']['temperature']['@value'])
        temp = round(temp,1)
        temperature = str(temp) + " °C"
        weather_icon = str(response_dict['current']['weather']['@icon'])
        weather_condition = str(response_dict['current']['weather']['@value'])
        country = str(response_dict['current']['city']['country'])

        return render(request, 'datapage.html', {"temp":temperature, "icon":weather_icon, "weather":weather_condition, "city":city_name, "country":country})
    else:
        return render(request, 'datapage.html', {})

def custom_error404(request, exception):
    return render(request, '404.html')

def custom_error500(request):
    return render(request, '500.html')
    