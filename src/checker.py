import requests
import urllib3
import http.client

urllib3.disable_warnings()

proxy_address = input('Enter proxy address. For example, http://ip:port \n').strip()
proxies = {
        'http': proxy_address,
        'https': proxy_address
        }

#create to variables, 'total' to sum up time for all urls in the 'urls.txt'
#'success_count' for counting ulrs which answered with status 200

total = 0
success_count = 0

urls = list()

with open('urls.txt', 'r', encoding='utf-8') as file:
    for line in file:
        urls.append(line.strip())

try:
    for url in urls:
        valid_proxy = requests.get(url, proxies=proxies, verify=False, timeout=10)
        elapsed = valid_proxy.elapsed.total_seconds()
        total += elapsed
        success_count += 1
    if success_count > 1:
        print(f'Proxy: {proxy_address} | Answer: {valid_proxy} | Average time: {total // success_count}')
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
