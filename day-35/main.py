import requests
import smtplib

parameters = { "days" : 1,
              "hours" : 3
              }

url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/bagerhat%2Cbangladesh?unitGroup=us&key=U8G3LPY4MZKJ8NTZRWK5P8CKC&contentType=json"

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()
returned_data = data["days"][0]["hours"][0]
def check_rain():
    for hour in data["days"][0]["hours"][::3]:
        if hour["conditions"] == "Rain" or hour["conditions"] == "Thunderstorm" or hour["conditions"] == "Partially cloudy":
            print(f"At {hour['datetime']}, it's {hour['conditions']}. Take a umbrella")
        else:
            print(f"At {hour['datetime']}, it's {hour['conditions']}. No rain, enjoy your day")

my_email = "ahonarahman2026@gmail.com"
password = "kuedtaitjjarlfet" 
send_to_email = "myshaafrinjeba916@gmail.com"       

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        print("step 4: logged in to email server")
        connection.sendmail(from_addr=my_email,
                                to_addrs= send_to_email,
                                msg=f"Subject:Weather Update\n\n{check_rain()}"
                            )
        print("step 5: email sent")
