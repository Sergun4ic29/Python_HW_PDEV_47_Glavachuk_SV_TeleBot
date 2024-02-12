import requests
import json
from config import keys


class APIException(Exception):
    pass
class CriptoConverter:
    @staticmethod
    def get_price(quot:str,base:str,amount:str):
        if quot == base:
            raise APIException('Нельзя сравнивать одинаковые валюты')
        try:
            base_tick = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            quot_tick = keys[quot]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quot}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quot_tick}&tsyms={base_tick}')
        total_base = json.loads(r.content)[keys[base]] * amount
        return total_base