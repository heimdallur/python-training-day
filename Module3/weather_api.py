import requests

key = "608d437b89e04d8db26180044222202"


def current_for_city(city: str) -> dict:

    api_url: str = f'http://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=no'

    response: dict = requests.request("GET", url=api_url).json()

    return response


def atro_for_city(city: str) -> dict:

    api_url: str = f'http://api.weatherapi.com/v1/astronomy.json?key={key}&q={city}&aqi=no'

    response: dict = requests.request("GET", url=api_url).json()

    return response
