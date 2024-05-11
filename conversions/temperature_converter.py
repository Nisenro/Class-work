'''
 A basic script, called kelvin_to_celsius.py, could only be used to do that one task. 
 But what if we wanted to extend this script, call it temperature_converter.py, 
 and use it to also convert Kelvin to Fahrenheit (following the formula F = (K − 273.15) * 9/5 + 32)? 
 And what if these two features should be able to run independently of each other?
'''
def kelvin_to_celsius(temperature):
    temp_in_celsius = temperature - 273.15
    return temp_in_celsius

def kelvin_to_fahrenheit(temperature):
    temp_in_fahrenheit = (temperature -273.15) * 9/5 + 32
    return temp_in_fahrenheit
      
    
def valid_input(temp):
    try:
        float_input = float(temp)
        return float_input
    except ValueError:
        print("Please input a digit")
        return None
       

if __name__ == "__main__":
    temperature_input = input("Temperature in kelvin: ")
    temperature = valid_input(temperature_input)
    if temperature is not None:
        celsius = kelvin_to_celsius(temperature)
        print(celsius)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        print(fahrenheit)

#
