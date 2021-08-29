import requests

url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/oportuno'
headers = {
    "Accept": "application/json",
    "Bmx-Token": "998e9ae2587c2e90d01c616faad0fa854d14fee0ae00e48c44d4dbcf90612c12"
}

resp = requests.get(url=url, headers=headers)
print(resp)
data = resp.json()
series = data.get('bmx').get('series')
if type(series) == list and len(series) > 0:
    datos = series[0].get('datos')
    if type(datos) == list and len(datos) > 0:
        exchange_rate = datos[0].get('dato')
        exchange_date = datos[0].get('fecha')
        print('tasa:', exchange_rate, " - fecha:", exchange_date)
