import smtplib
import random
import datetime as dt
import pandas

now = dt.datetime.now()
current_day = now.day
print(f"current day is {current_day}")
my_email = "ahonarahman2026@gmail.com"
password = "kuedtaitjjarlfet"  

with open("day-32/birthdays.csv") as file:
    data = pandas.read_csv(file)
    birthdays_dict = data.to_dict(orient="records")
    print("step 1: birthdays dict created")
if current_day == birthdays_dict[2]["day"]:
    print("birthday match found")
    with open("day-32/letter1.txt") as letter_file:
        letter_contents1 = letter_file.read()
        print("step2 :read letter 1")
    with open("day-32/letter2.txt") as letter_file:
        letter_contents2 = letter_file.read()
        print("reade letter 2")
    with open("day-32/letter3.txt") as letter_file:
        letter_contents3 = letter_file.read()
        print("read letter 3")
    letter_content = random.choice([letter_contents1, letter_contents2, letter_contents3])
    letter_sent_to = birthdays_dict[1]["name"]
    print("step 3: letter content chosen")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        print("step 4: logged in to email server")
        connection.sendmail(from_addr=my_email,
                                to_addrs="myshaafrinjeba916@gmail.com",
                                msg=f"Subject:Friday Motivation\n\n{letter_content}"
                            )
        print("step 5: email sent")