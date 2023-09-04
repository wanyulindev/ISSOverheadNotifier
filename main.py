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


# 20% done - API Parameters: Sunrise & Sunset times API

import requests
from datetime import datetime

MY_LAT = 34.052235
MY_LNG = -118.243683

# Based on the API itself, "lat" and "lng" are required when using it.
# We can go LatLong.net and search it: (LA, USA)
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0  # 12 to 24hrs
}

response = requests.get("https://api.sunrise-sunset.org/json",
                        params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

# Now, THIS is the most important part that we use when working:
print(sunset.split("T")[1].split(":")[0])
print(sunrise.split("T")[1].split(":")[0])

time_now = datetime.now()
# print(time_now)
print(time_now.hour)












