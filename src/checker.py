import requests
import urllib3
import http.client

urllib3.disable_warnings()

proxy_address = input('Enter proxy address. For example, http://ip:port \n')
proxies = {
        'http': proxy_address,
        'https': proxy_address
        }

total = 0

urls = list()

with open('urls.txt', 'r', encoding='utf-8') as file:
    for line in file:
        urls.append(line)

try:
    for url in urls:
        free = requests.get(url, proxies=proxies, verify=False, timeout=10)
        elapsed = r.elapsed.total_seconds()
        total += elapsed

    print(f'Answer: {free} | Average time: {total // len(urls)}')
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
