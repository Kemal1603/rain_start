import requests
import smtplib
import os
open_weather_api_key = "445a71f05f1dfc317e7ff16be20d54e6"

parameters = {
	'lat': 53.89,
	'lon': 27.57,
	'exclude': 'current,minutely,daily',
	'appid': open_weather_api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
data_from_open_weather_map = response.json()
hourly = [i["weather"] for i in data_from_open_weather_map["hourly"][:12]]
bad_weather = False
my_email = "developer20201203@gmail.com"
password = os.environ.get("MY_GOOGLE_PASS")

for hour in hourly:
	if hour[0]['id'] < 622:
		bad_weather = True

if bad_weather:
	with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
		connection.starttls()
		connection.login(user=my_email, password=password)
		connection.sendmail(from_addr=my_email,
		                    to_addrs='cfqufcfquf@mail.ru',
		                    msg=f"Subject: Сообщение от Мужа:\n\n Любимая, если ты получила"
		                        f" это сообщение, значит сегодя будет отвратительная погода, пожалуйста"
		                        f"оденься потеплее и помни, что Муж любит тебя больше !".encode('utf-8'))
