# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 11:54:09 2016

@author: joshuabarnett
"""
temp1_float = 15.0
temp2_float = 0.0
temp3_float = -15.0
speed1_float = 10.0
speed2_float = 20.0
speed3_float = 30.0
windChill1 = 35.74 + (0.6215*temp1_float) - (35.75*speed1_float**0.16) + (0.4275*temp1_float*speed1_float**0.16)
windChill2 = 35.74 + (0.6215*temp2_float) - (35.75*speed2_float**0.16) + (0.4275*temp2_float*speed2_float**0.16)
windChill3 = 35.74 + (0.6215*temp3_float) - (35.75*speed3_float**0.16) + (0.4275*temp3_float*speed3_float**0.16)
print('Wind Chill Conversions:\n')
print('Temperature (degrees F):', temp1_float)
print('Wind Speed (MPH):', speed1_float)
print('Wind Chill Temperature Index:', windChill1,'\n')
print('Temperature (degrees F):', temp2_float)
print('Wind Speed (MPH):', speed2_float)
print('Wind Chill Temperature Index:', windChill2,'\n')
print('Temperature (degrees F):', temp3_float)
print('Wind Speed (MPH):', speed3_float)
print('Wind Chill Temperature Index:', windChill3)

temp_float = float(input("Enter the temperature in Fahrenheit: " ))
speed_float = float(input("Enter windspeed in MPH: " ))

windChill = 35.74 + (0.6215*temp_float) - (35.75*speed_float**0.16) + (0.4275*temp_float*speed_float**0.16)

print('\nTemperature (degrees F):', temp_float)
print('Wind Speed (MPH):', speed_float)
print('Wind Chill Temperature Index:', windChill)