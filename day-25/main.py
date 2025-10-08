
import csv



with open("weather.csv") as data_file:
    data = csv.reader(data_file)
    print(data)