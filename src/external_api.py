import requests

API_KEY = "ya5tdkTSqRDkMmLk0KaVFEIAvGw84sRW"


def convert_currency(currency_from: str, currency_to: str, amount_from: float) -> float:
    """Ф-я конвертирует валюту по актуальному курсу"""

    url = "https://api.apilayer.com/exchangerates_data/convert"

    params = {
        "from": currency_from,
        "to": currency_to,
        "amount": amount_from
    }
    headers= {
      "apikey": API_KEY
    }

    response = requests.request("GET", url, headers=headers, params=params)

    #status_code = response.status_code
    result = response.json()
    return result['result']


# sum_result = convert_currency("EUR","USD",100)
# print(sum_result)
