import requests
import sys
import os


sys.path.append(os.path.join(sys.path[0], 'bot'))

from config import YANDEX_MAP_KEY



async def get_adres(city:str) -> str:
    adres = f'{city}+Ленина+1'
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={YANDEX_MAP_KEY}&geocode={adres}&format=json&results=1"
    response = requests.get(url)
    data = response.json()
    coord = data['response']['GeoObjectCollection']['featureMember'][-1]['GeoObject']['Point']['pos']
    latitude, width = coord.split(' ')
    return(f'https://yandex.ru/maps/?pt={latitude},{width}&z=18&l=map')



