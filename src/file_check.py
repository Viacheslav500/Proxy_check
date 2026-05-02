import os
from .checker import check_single_proxy
import concurrent.futures

def to_check_a_file(path_to_file):
    if not os.path.exists(path_to_file):
        print('The file does not exist or entered incorrect file path')
        return

    with open(path_to_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    result = list()
    invalid = {'Invalid proxy', 'Timeout occurred', 'Connection Error occurred'}

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_proxy = [executor.submit(check_single_proxy, proxy) for proxy in lines]
        for future in concurrent.futures.as_completed(future_to_proxy):
            valid = future.result()
            if valid not in invalid:
                result.append(valid)

    with open(path_to_file, 'w', encoding='utf-8') as file:
        for res in result:
            file.write(res + '\n')
