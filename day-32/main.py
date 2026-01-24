##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
import random
import datetime as dt

now =dt.datetime.now()

days_of_week = now.weekday()
print(days_of_week)


my_email = "ahonarahman2026@gmail.com"
password = "kuedtaitjjarlfet"  


if days_of_week == 5:
    with open("day-32/birthday.txt", "r") as file:
        print("opening file")
        quote_lines = file.readlines()
   # print(quote_lines)
if not quote_lines:
    print("file is empty")
else:
    random_quote = random.choice(quote_lines)
    print(random_quote)
    print('randomly_choosen')
    print("Step 1: creating SMTP object")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        print("Step 2: connected to server")

        connection.starttls()
        print("Step 3: TLS started")
        connection.login(my_email, password)
        print("Step 4: logged in")
        connection.sendmail(from_addr=my_email,
                            to_addrs="myshaafrinjeba916@gmail.com",
                            msg=f"Subject:Friday Motivation\n\n{random_quote}"
                            )
        print("Step 5: mail sent")

        
        print("Step 6: connection closed")

