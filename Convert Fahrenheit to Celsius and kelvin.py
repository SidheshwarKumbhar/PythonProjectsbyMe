"""----------------------------------------------------------------------------------------------------------------
* Most countries around the world use the Celsius scale to indicate temperatures, but the United States
    still uses the Fahrenheit scale

* in this project will convert fahrenheit to the celsius to kelvin.

--------------------------------------------------------------------------------------------------------------------"""


def convert_f_to_c(f):
    c = (5 / 9) * (f - 32)
    print("The Temp in Degree Celsius = ", round(c, 2))


def convert_f_to_k(f):
    k = ((5 / 9) * (f - 32)) + 273.15
    print("The Temp in Kelvin = ", round(k, 2))


fahrenheit = float(input("enter the TEMP in Fahrenheit : "))

convert_f_to_c(fahrenheit)
convert_f_to_k(fahrenheit)
