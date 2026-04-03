# Proxy_check
Simple script to check a http/https/socks proxy. It checks that the proxy is valid and counts average respond time. 

## Installing

Needs Python >= 3.10

It uses 'uv'.

Activate the virtual environment by typing a command:

```.venv/bin/activate```

Install the package by the following command:

```uv pip install .```

After that the command 'proxycheck' will become available in this this virtual environment. 

## Usage

After installing the package you can use 'proxycheck' from the terminal. 

There two arguments which you can choose. 

The first one is '--proxy' or '-p'. 
It checks only one proxy which you need to type in the terminal in a format 'http://ip:port':

```proxycheck -p socks5://54.23.123.344:443 (as an example)```

The second argument is '--file' or '-f'. 
It requires a path to the file with list of proxies. So, create a file and then put down the path to it.
Make sure that the each proxy in the file is on the separate line, format must be 'http://ip:port':

```proxycheck --file path/to/file.txt```

## Adjusting urls file

There is a file with urls. There are several websites whic are checked and then the average time is calculated. 
If you need, feel free to change urls, add or delete. 
Do not recomment to put a lot of urls in the file as it will take quite a lot of time to check a proxy.
