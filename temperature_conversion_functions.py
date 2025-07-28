def celsius_to_fahrenheit():
    C = float(input('Enter the input: '))
    F = (C *(9/5)+32)
    return F
def fahrenheit_to_kelvin():
    F=float(input('Enter the input: '))
    K = (F-32)*(5/9) + 273.15
    return K
def kelvin_to_celsius():
    K=float(input('Enter the input: '))
    C = K-273.15
    return C

