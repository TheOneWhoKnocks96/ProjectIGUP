import unicodedata
import sys
import time
import datetime
import calendar
from os import listdir
from openpyxl import load_workbook

#Value Limits

#Temperature (Celsius)
temp_max = 45
temp_min = -1

#Altimeter Pressao (Barometro) (mm)
pressure_max = 790
pressure_min = 710

#Atmospheric Vapor Tension (mm)
vapor_max = 17
vapor_min = 1

#Humidity (%)
humidity_max = 100
humidity_min = 0

#Ozonometer (in grains)
ozone_max = 20
ozone_min = 0

#Cloud Quantity (int)
cloud_max = 25
cloud_min = 0

#Pluvimeter (mm)
pluv_max = 50
pluv_min = 0

#Udometer (mm)
udo_max = 50
udo_min = 0

#Absolute wind velocity (km)
abso_wind_speed_max = 150
abso_wind_speed_min = 0

#"Velocidade Horaria"
clock_wind_speed_max = 40
clock_wind_speed_min = 0
