# Header
# DSC 510
# Week 12
# Programming Assignment Week 12 - FINAL
# Author Melissa Young
# 06/04/2022

"""
Weather Program
For your class project we will be creating an application to interacts with a webservice in order to obtain data.
Your program will use all of the information you’ve learned in the class in order to create a useful application.
Your program must prompt the user for their city or zip code and request weather forecast data from OpenWeatherMap.
Your program must display the weather information in a READABLE format to the user.
Requirements:

    Create a header for your program just as you have in the past.
    Create a Python Application which asks the user for their zip code or city (Your program must perform both a city
    and a zip lookup). You must ask the user which they want to perform with each iteration of the program.
    Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
    Display the weather forecast in a readable format to the user. Do not display the weather data in Kelvin, since this
     is not readable to the average person.  You should allow the user to choose between Celsius and Fahrenheit and
     ideally also Kelvin.
    Use comments within the application where appropriate in order to document what the program is doing. Comments
    should add value to the program and describe important elements of the program.
    Use functions including a main function and a properly defined call to main. You should have multiple functions.
    Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
    Validate whether the user entered valid data. If valid data isn’t presented notify the user. Your program should
    never crash with bad user input.
    Use the Requests library in order to request data from the webservice.
        Use Try blocks to ensure that your request was successful. If the connection was not successful display a
         message to the user.
    Use Python 3
    Use try blocks when establishing connections to the webservice. You must print a message to the user indicating
    whether or not the connection was successful.
    You must have proper coding convention including proper variable names (See PEP8).

Deliverables:

    Final Program in a .py file (Due week 12)

Project Notes:

        Be creative. This assignment is a real world program. Use it as an opportunity to improve your knowledge.
        Sign up for API Key.
        The API key will look something similar to this: d5751b1a9e2e4b2b8c7983646072da8b
        Make a connection to the API using the Requests library.
"""

import requests
import json


class OpenWeather:  # Create a class (blueprints essentially) for object (weather data variables).
    def __init__(self, city, city_name, zipcode, country, curr_temp,
                 high_temp, low_temp, feels_like, weather_description, humidity, pressure, wind_speed):
        self.city = city
        self.city_name = city_name
        self.zipcode = zipcode
        self.country = country
        self.curr_temp = curr_temp
        self.high_temp = high_temp
        self.low_temp = low_temp
        self.feels_like = feels_like
        self.weather_description = weather_description
        self.humidity = humidity
        self.pressure = pressure
        self.wind_speed = wind_speed

    def print(self, temps):  # Define 3 options of temperature scales, celsius, fahrenheit and kelvin with
        # corresponding speed measurements.
        if temps.lower() == 'celsius':
            c_f_k = 'C'
            wind_speed_output = 'm/s'
        elif temps.lower() == 'fahrenheit':
            c_f_k = 'F'
            wind_speed_output = 'mph'
        elif temps.lower() == 'kelvin':
            c_f_k = 'K'
            wind_speed_output = 'm/s'
        if self.city:  # Define output when city is selected in input request.
            print(f'\nCurrent weather conditions for {self.city}, {self.country} in {temps} (°{c_f_k}):')
        elif self.zipcode:  # Define output when zip code is selected in input request.
            print(f'\nCurrent weather conditions for {self.zipcode}, {self.country} in {temps} (°{c_f_k}):')
        print(f'Current Temperature: {self.curr_temp:.0f}°{c_f_k}')  # Display Current Temp to 0 decimals.
        print(f'High Temperature: {self.high_temp:.0f}°{c_f_k}')  # Display High Temp to 0 decimals.
        print(f'Low Temperature: {self.low_temp:.0f}°{c_f_k}')  # Display Low Temp to 0 decimals.
        print(f'Feels Like Temperature: {self.feels_like:.0f}°{c_f_k}')  # Display Feels Like Temp to 0 decimals.
        print(f'Cloud Cover: {self.weather_description}')  # Display Cloud Cover.
        print(f'Humidity: {self.humidity}%')  # Display Humidity in %.
        print(f'Pressure: {self.pressure}hPa')  # Display Pressure in hPa.
        print(f'Wind Speed: {self.wind_speed}{wind_speed_output}\n')  # Display Wind Speed with proper scale.


def fetch_data(city, zipcode, units):  # Use the current weather API from OpenWeatherMap
    if units == 'c':
        units_query = '&units=metric'
    elif units == 'f':
        units_query = '&units=imperial'
    elif units == 'k':
        units_query = ''
    if city:
        loc_query = f'q={city}'
    elif zipcode:
        loc_query = f'zip={zipcode},us'
    api_key = '953977807420356b069d96f845038aed'  # Sign up for a free current weather API from OpenWeathermap.org/api
    url = f'https://api.openweathermap.org/data/2.5/weather?{loc_query}{units_query}&appid={api_key}'
    resp = requests.request('GET', url)
    data = json.loads(resp.text)
    city_name = data['name']
    country = data['sys']['country']
    curr_temp = data['main']['temp']
    high_temp = data['main']['temp_max']
    low_temp = data['main']['temp_min']
    feels_like = data['main']['feels_like']
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind_speed = data['wind']['speed']
    return OpenWeather(zipcode if zipcode else None, city if city else None, city_name, country, curr_temp, high_temp,
                       low_temp, feels_like, weather_description, humidity, pressure, wind_speed)


def main():  # You must have a well-defined welcome message.
    print('Welcome to WeatherApp!  What US city or zip code would you like to see current weather conditions for?')
    while True:
        print('For City, enter the number 1')
        print('For Zip Code, enter the number 2')
        city_zip = int(input('Please choose number 1 or 2: '))  # Request user to select option for city or zip code
        # weather lookup.
        if city_zip == 1:  # Crete try blocks for each city scenario test.
            while True:
                city_input = input('Please enter the city name:')
                print('\nWhat temperature type would you like to see?')
                print('Fahrenheit, enter the number 1')
                print('Celsius, enter the number 2')
                print('Kelvin, enter the number 3\n')
                temps_input = int(input('Input temperature type of your choice: '))
                if temps_input == 1:
                    try:
                        weather_data = fetch_data(city_input, None, 'f')
                        weather_data.print('Fahrenheit')
                        break
                    except:
                        print('Please enter a valid city name.')
                        continue
                elif temps_input == 2:
                    try:
                        weather_data = fetch_data(city_input, None, 'c')
                        weather_data.print('Celsius')
                        break
                    except:
                        print('Please enter a valid city name.')
                        continue
                elif temps_input == 3:
                    try:
                        weather_data = fetch_data(city_input, None, 'k')
                        weather_data.print('Kelvin')
                        break
                    except:
                        print('Please enter a valid city name.')
                        continue
                else:
                    print('Input error, enter a valid number!')
                    continue
        elif city_zip == 2:  # Crete try blocks for each zip code scenario test.
            while True:
                zip_input = input('Please enter a US zip code:')
                print('\nWhat temperature type would you like to see?')
                print('Fahrenheit, enter the number 1')
                print('Celsius, enter the number 2')
                print('Kelvin, enter the number 3\n')
                temps_input = int(input('Input temperature type of your choice 1, 2 or 3: '))
                if temps_input == 1:
                    try:
                        weather_data = fetch_data(None, zip_input, 'f')
                        weather_data.print('Fahrenheit')
                        break
                    except:
                        print('Please enter a valid US Zip Code.')
                        continue
                elif temps_input == 2:
                    try:
                        weather_data = fetch_data(None, zip_input, 'c')
                        weather_data.print('Celsius')
                        break
                    except:
                        print('Please enter a valid US Zip Code.')
                        continue
                elif temps_input == 3:
                    try:
                        weather_data = fetch_data(None, zip_input, 'k')
                        weather_data.print('Kelvin')
                        break
                    except:
                        print('Please enter a valid US Zip Code.')
                        continue
                else:
                    print('Input error, enter a valid number!')
                    continue
        else:
            print('Input error, enter a valid number!')
            continue
        search_input = input('Would you like to perform another weather search? (Y/N): ').lower()  # Allow user to
        # perform as many lookups as they would like.
        if search_input == 'y':
            continue
        else:
            print('Thank you for visiting WeatherApp!')
            break


if __name__ == "__main__":
    main()
