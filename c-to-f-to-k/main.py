
celsius = float(input("Please enter the temperature in Celsius: "))
fahrenheit = (celsius * 1.8) + 32
kelvin = celsius + 273.15 

print('''\n%0.1f Celsius is equal to %0.2f degrees Fahrenheit.\n'''%(celsius, fahrenheit))
print('''\n%0.1f Celsius is equal to %0.2f Kelvin.\n'''%(celsius, kelvin))