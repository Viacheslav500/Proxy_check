import requests

proxy_address = input('Enter proxy address. For example, https://1.1.1.1:0000')
proxies = {
        'http': f'{proxy_address}',
        'https': f'{proxy_address}'
        }
free = requests.get('https://ya.ru/', proxies=proxies)
print(free)
