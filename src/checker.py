import requests
import urllib3

urllib3.disable_warnings

proxy_address = input('Enter proxy address. For example, http://ip:port \n')
proxies = {
        'http': f'{proxy_address}',
        'https': f'{proxy_address}'
        }
try:
    free = requests.get('https://ya.ru/', proxies=proxies, verify=False, timeout=5)
    print(free)
except requests.exceptions.SSLError:
    print('SSLError occurred')
except http.client.RemoteDisconnected:
    print('Proxy is unavailable')
except urllib3.exceptions.ProtocolError:
    print('Protocol Error occurred')
except requests.exceptions.ConnectionError:
    print('Conection Error occurred')

#free = requests.get('https://ya.ru/', proxies=proxies)
#print(free)
