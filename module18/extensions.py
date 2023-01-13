import requests
import json
from config import API_KEY, API

class ServiceConverter:
    @staticmethod
    def getPrice(from_currency: str, to_currency: str, total: int) -> float:
        headers = {'authorization': API_KEY}
        res = requests.get(f'{API}?fsym={from_currency}&tsyms={to_currency}', headers=headers)
        if res.status_code != 200:
            return 0

        data = res.json()
        amount = float(data[to_currency]*total)
        
        return round(amount, 2)



