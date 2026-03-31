import src.checker.check_single_proxy

def to_check_a_file(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    result = list()

    for line in lines:
        if check_single_proxy(line.strip()) == ('Invalid proxy' or 'Tomeout occurred' or 'COnnection Error uccurred':
            continue
        else:
            result.append(check_single_proxy(line.strip())

    with open(path_to_file, 'w', encoding='utf-8') as file:
        for res in result:
            file.writelines(res)
