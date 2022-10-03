import json
import requests
from config import keys

class APIException(Exception):
    pass


class CashConverter:
    @staticmethod
    def get_price(base: str, qutoe: str, amount: str):
        if base == qutoe:
            raise APIException(f'Ну и зачем переводить {base} в {qutoe}?')

        try:
           base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            qutoe_ticker = keys[qutoe]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {qutoe}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать кол-во {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={qutoe_ticker}')
        exch_cash = json.loads(r.content)[keys[qutoe]]

        return exch_cash