# BasicWeatherWebAppExample

## Introduction
This is my first attempt to build a web application from scratch, that's why I chose a simple and common concept. 
It is supposed to work as a template for future more complex projects. The application will consist of a web page with 
a search bar that presents the current weather data for a selected area (using a city or village name).


## Technical Characteristics
For the development of this web app I am going to use the Django framework (Python-Based) and the following programming and markup languages:
 - Python
 - HTML(with internal CSS usage)

in the Visual Studio Code environment.

Weather APIs by [OpenWeatherMap](https://openweathermap.org/api).


## How to use the web app
Since you can run the app and opened it on your browser (locally) you will see the page with its welcoming form:

![web_app_1](https://github.com/ThomasKatsavos/BasicWeatherWebAppExample/assets/125153451/04e05f3f-3a80-4159-b860-f11bf1511d5a)

Next you can type in the searchbar the name of the city or village you want to view the weather for. The app returns the data 
with the same page-adress, with a slightly modified form. It should appear like the example bellow that showed up after searching the weather for 
'Thessaloniki':

![web_app_2](https://github.com/ThomasKatsavos/BasicWeatherWebAppExample/assets/125153451/f4e189d8-c3ef-4965-8620-46ac686832ef)

In case you search an address that doesn't exist locally (e.g.: 'http://127.0.0.1:8000/secondweatherpage') you will view a custom Error 404 page.
If you type two separate words in the searchbar (e.g.: 'Hong Kong') or a name for which data cannot be provided (e.g.: a false name such as 'KongHong' or the name of a tiny village) or you typed in a language other than English a custom Error 500 page will emerge with a few instructions.


## Instructions for running the app on your device
Here I will give some information on how to organize this project on a virtual environment (pipenv) and run the app on a local server on Windows.
!!!  In this project I have set 'DEBUG=False' !!!
- Create a directory, here I will call it 'testdir', where you want clone the repository : ``` mkdir testdir ```
- Enter this directory : ``` cd testdir ```
- Clone the repository : ``` git clone https://github.com/ThomasKatsavos/BasicWeatherWebAppExample.git ```
- Enter the project directory : ``` cd BasicWeatherWebAppExample ```
- Enter the WeatherWebApp file : ``` cd WeatherWebApp ```
- Create a virtual environment and install Django in it : ``` pipenv install django ```
- Copy the Virtualenv location
- Open the project on Visual Studio Code(Move the "BasicWeatherWebAppExample" dir)
- From 'View-Command Palette' select 'Select Interpreter'
- In the bar paste the Virtualenv location and add '\Scripts\python.exe', then hit enter and create a new terminal for the v.e.
- In the new terminal :
  - Install "xmltodict" library : ``` pip install xmltodict ```
  - (Skip this, but in some cases you may need to run ``` python manage.py migrate ```)
  - Run : ``` python manage.py runserver ```
  - Read the message to access the app!
 - Remember: To remove a virtual environment created with pipenv run : ``` pipenv --rm ```


###  THIS REPOSITORY AND README FILE WILL BE UPDATED IN CASE SOME ISSUES OCCUR
 

 
