import requests
import urllib3
import http.client
import time

urllib3.disable_warnings()


def check_single_proxy(proxy_address):
    proxy_address = proxy_address.strip()
    proxies = {
        'http': proxy_address,
        'https': proxy_address
        }

    #create to variables, 'total' to sum up time for all urls in the 'urls.txt'
    #'success_count' for counting ulrs which answered with status 200

    total = 0
    success_count = 0

    #create 'max_retries' to make sure proxy is invalid
    #create 'time_delay' to start checking after specified time

    
    max_retries = 3
    time_delay = 2

    urls = list()

    with open('urls.txt', 'r', encoding='utf-8') as file:
        for line in file:
            urls.append(line.strip())

    for url in urls:
        for attempt in range(max_retries):
            try:
                valid_proxy = requests.get(url, proxies=proxies, verify=False, timeout=10)
                if valid_proxy.status_code == requests.codes.ok:
                    elapsed = valid_proxy.elapsed.total_seconds()
                    total += elapsed
                    success_count += 1
                    break
                else:
                    time.sleep(time_delay)
            except requests.exceptions.Timeout:
                return 'Timeout occurred'
            except requests.exceptions.ConnectionError:
                return 'Connection Error occurred'

    if success_count / len(urls) > 0.5:
        return f'Proxy: {proxy_address} | Average time: {total / success_count}'
    else:
        return 'Invalid proxy'

#except requests.exceptions.Timeout:
#    print('Timeout occurred')
#except requests.exceptions.ConnectionError:
#   print('Connection Error occurred')
#except requests.exceptions.SSLError:
#    print('SSLError occurred')
#except http.client.RemoteDisconnected:
#    print('Proxy is unavailable')
#except urllib3.exceptions.ProtocolError:
#    print('Protocol Error occurred')
