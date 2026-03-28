import requests
import urllib3
import http.client

urllib3.disable_warnings()

proxy_address = input('Enter proxy address. For example, http://ip:port \n')
proxies = {
        'http': proxy_address,
        'https': proxy_address
        }
try:
    free = requests.get('https://ya.ru/', proxies=proxies, verify=False, timeout=10)
    print(free)
except requests.exceptions.Timeout:
    print('Timeout occurred')
except requests.exceptions.ConnectionError:
    print('Connection Error occurred')
except requests.exceptions.SSLError:
    print('SSLError occurred')
except http.client.RemoteDisconnected:
    print('Proxy is unavailable')
except urllib3.exceptions.ProtocolError:
    print('Protocol Error occurred')


#free = requests.get('https://ya.ru/', proxies=proxies)
#print(free)
