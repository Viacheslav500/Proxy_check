import argparse
from src.checker.check_single_proxy import check_single_proxy
from src.checker.file_check import to_check_a_file


def main():
    parser = argparse.ArgumentParser(description='Simple proxy checker. You can check one proxy or a file with list of proxies')
    parser.add_argument('--proxy', '-p', help='Write down only one proxy (http://ip:port)')
    parser.add_argument('--file', '-f', help='Write down a path to the file with list of proxies')
    args = parser.parse_args()

    if args.proxy:
        print(check_single_proxy(args.proxy))
    elif args.file:
        to_check_a_file(args.file)
        print('File was checked')
    else:
        print('Use --proxy/-p or --file/-f to start the script')

if __name__ == '__main__':
    main()
        
