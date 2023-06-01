import requests

city = str(input("\nPlease enter a city name (San Jose): "))
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="

API_KEY = "ENTER YOUR API KEY HERE"
URL = BASE_URL+city+"&appid=" + API_KEY
response = requests.get(URL)
x = response.json()
if x['cod'] != 401:
    temperature = float(x["main"]['temp'] - 273.15)
    print("City Name:", x["name"])
    print("Weather:", x["weather"][0]['main'])
    print("Temperature: ", "{:.2f}".format(x["main"]['temp'] - 273.15) + " °C -", "{:.2f}".format(
        ((x["main"]['temp'] - 273.15) * 1.8) + 32) + " °F -", "{:.2f}".format(x["main"]['temp']) + " K")
    print("Humidity:", x["main"]['humidity'])
    print("Pressure:", x["main"]['pressure'])
    print("\n")
else:
    print('The City you entered was not found.')