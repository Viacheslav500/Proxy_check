# Proxy_check
Simple script to check a http/https/socks proxy. It checks that the proxy is valid and counts average respond time. 

## Installing

It needs Python >= 3.10 to install the script, uv as package manager. 

First, install uv using guide in the official documentation.

Activate the virtual environment by typing a command:

```.venv/bin/activate```

Install the package by the following command:

```uv pip install .```

After that the command 'proxycheck' will become available in the terminal. 

## Usage

After installing the package you can use 'proxycheck' from the terminal. 

There two arguments which you can choose. 

The first one is '--proxy' or '-p'. 
It checks only one proxy which you need to type in the terminal in a format 'http://ip:port':

```proxycheck -p socks5://54.23.123.344:443```

The second argument is '--file' or '-f'. 
It requires a path to the file with list of proxies. So, create a file and then put down the path to it.
Make sure that the each proxy in the file is on the separate line, format must be 'http://ip:port':

```proxycheck --file path/to/file.txt```

For help use argument '--help' or '-h'.

## Adjusting urls file

There is a file with urls at the root of the project. There are several websites with which all proxies are checked and then the average time is calculated. 
If you need, feel free to change urls, add or delete urls in the file. 
Do not recommend to put a lot of urls in the file as it will take quite a lot of time to check a proxy.
Do not delete the file completely as it wil brek the whole script. 

##Note

This project was made in order to try request library, opening files, getting data, to try pytest, uv.
If it will be useful to someone, it will e great. But this project is nothing serious.  
