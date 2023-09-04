#
# # 10% done - Introducing requests module:
# import requests
# # when working with APIs, we need requests module.
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response)
# # Output: <Response [200]> (Responses Codes)
# # 1XX: Hold On
# # 2XX: Here you go
# # 3XX: Don't have permission, go away.
# # 4XX: Requester screwed up
# # 5XX: Server screwed up
#
# # print(response.status_code)     # Only output codes
#
# response.raise_for_status()
# # time to raise error to see what's going on:
# # (when we raise an error, we are expecting it doing something,
# # like showing more info)
#
# # Let's go view requests documentation,
# # to check how it handles Errors and Exceptions: Response.raise_for_status()
#
# data = response.json()
# print(data)
# print(type(data))
#
# data = response.json()["iss_position"]
# print(data)
# latitude = data["latitude"]
# longitude = data["longitude"]
# iss_position = (longitude, latitude)
# print(iss_position)
# # go to LatLong.net and see where it's at!


# # 20% done - API Parameters: Sunrise & Sunset times API
#
# import requests
# from datetime import datetime
#
# MY_LAT = 34.052235
# MY_LNG = -118.243683
#
# # Based on the API itself, "lat" and "lng" are required when using it.
# # We can go LatLong.net and search it: (LA, USA)
# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LNG,
#     "formatted": 0  # 12 to 24hrs
# }
#
# response = requests.get("https://api.sunrise-sunset.org/json",
#                         params=parameters)
# response.raise_for_status()
# data = response.json()
# # print(data)
# sunrise = data["results"]["sunrise"]
# sunset = data["results"]["sunset"]
#
# # Now, THIS is the most important part that we use when working:
# print(sunset.split("T")[1].split(":")[0])
# print(sunrise.split("T")[1].split(":")[0])
#
# time_now = datetime.now()
# # print(time_now)
# print(time_now.hour)


# 100% done - ISS Overhead Notifier project (without BONUS finished yet ...)
import requests
from datetime import datetime
import pytz
import smtplib

MY_EMAIL = "wanyudevtest@gmail.com"
PASSWORD = "btbgsmumwrcsdivg"
RECEIVER = "wanyudevtest@yahoo.com"
MY_LAT = 34.052235
MY_LNG = -118.243683

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
# print(data)
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# print(iss_latitude, iss_longitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

sunset = data["results"]["sunset"]
# print(sunset)
sunset_date = data["results"]["sunset"].split("T")[0].split("-")
# print(sunset_date)
sunset_hr = data["results"]["sunset"].split("T")[1].split(":")
# print(sunset_hr)
sunset = sunset_date + sunset_hr
# print(sunset)
# sunset = [int(i) for i in sunset[:3]]
utc_datetime = datetime(year=int(sunset[0]), month=int(sunset[1]), day=int(sunset[2]),
                        hour=int(sunset[3]), tzinfo=pytz.timezone("UTC"))
# print(utc_datetime)
pt_datetime = utc_datetime.astimezone(pytz.timezone("US/Pacific"))
# print(pt_datetime)
# print(type(pt_datetime))
pt = pt_datetime.strftime("%Y-%m-%d %H")
# print(type(pt))
# print(pt[-2:])
pt_hr = int(pt[-2:])

time_now = datetime.now()
# print(time_now)
# print(time_now.hour)

# If the ISS is close to my current position, VVV
# and it is currently dark VVV
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

# Your position is within +5 or -5 degrees of the ISS position.

lat_abs = abs(MY_LAT - iss_latitude)
lng_abs = abs(MY_LNG - iss_longitude)

if lat_abs <= 5 and lng_abs <= 5:
    if time_now.hour >= pt_hr:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=RECEIVER,
                                msg=f"Subject:Hey LOOK UP!\n\n"
                                    f"ISS is overhead! Take a good look of it")








