import requests

api_key = "71dbe179ffa19771c15ad090befe3da4"
MY_LAT = 13.00 # Your latitude
MY_LONG = 77.583333 # Your longitude

parameters ={
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
}

api_url = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(url=api_url, params=parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()

print(data["hourly"])