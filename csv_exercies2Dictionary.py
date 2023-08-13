
import csv

'''
date,temperature(F)
Jan 1,27
Jan 2,31
Jan 3,23
Jan 4,34
Jan 5,37
Jan 6,38
Jan 7,29
Jan 8,30
Jan 9,35
Jan 10,30


a. What was the temperature on Jan 9?
b. What was the temperature on Jan 4?

'''

with open('nyc_weather.csv', 'r') as f:
    file_reader = csv.reader(f)
    weather_dict = {}

 
    next(file_reader)
    for element in file_reader:
        weather_dict[element[0]] = element[1]
        
    #prints temperature for Jan 9
    print(weather_dict['Jan 9'])
    #prints temp for jan 4
    print(weather_dict['Jan 4'])