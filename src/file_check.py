import os
from src.checker.check_single_proxy import check_single_proxy

def to_check_a_file(path_to_file):
    if os.path.exists(path_to_file):
        return None
    else:
        print('The file does not exist or entered incorrect file path')

    with open(path_to_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    result = list()
    invalid = {'Invalid proxy', 'Timeout occurred', 'Connection Error occurred'}

    for line in lines:
        valid = check_single_proxy(line.strip())
        if valid in invalid:
            continue
        else:
            result.append(valid)

    with open(path_to_file, 'w', encoding='utf-8') as file:
        for res in result:
            file.write(res)
