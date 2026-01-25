import smtplib
import random
import datetime as dt
import pandas

now = dt.datetime.now()
current_day = now.day

with open("day-32\project/birthdays.csv") as file:
    data = pandas.read_csv(file)
    birthdays_dict = data.to_dict(orient="records")
    print(birthdays_dict)