
import os
import requests
from bs4 import BeautifulSoup
import random
import argparse
from proxy_checker import ProxyChecker
from termcolor import colored

def display_banner():
    banner = '''
    [92m
    [92m
    [92m
    [92m
    [92mProxiiMaster[0m
    [0m
    [0m
    [0m
    [0m
    '''
    print(banner)

# List of proxy sources
proxy_sources = [
    'https://www.proxy-list.download/api/v1/get?type=https',
]

# Function to scrape proxies
def scrape_proxies():
    proxies = []
    if not os.path.exists('proxy_list.txt'):
        open('proxy_list.txt', 'w').close()
    with open('proxy_list.txt', 'a') as f:
        for proxy in proxies:
            f.write(f"{proxy}\n")
    print(colored(f"Scraped {len(proxies)} proxies.", 'blue'))

# Function to check proxy validity
def check_proxies(num_proxies=None):
    print(colored("check_proxies function called", 'yellow'))
    checker = ProxyChecker()
    valid_proxies = []
    with open('proxy_list.txt', 'r') as f:
        proxies = f.readlines()
    print(colored(f"Total proxies available: {len(proxies)}", 'cyan'))
    if num_proxies is None:
        num_proxies = len(proxies)
    for proxy in proxies[:num_proxies]:
        proxy = proxy.strip()
        try:
            result = checker.check_proxy(proxy)
            print(colored(f"Checking proxy: {proxy}, Result: {result}", 'green'))
            if result and result['timeout'] < 2000:
                valid_proxies.append(proxy)
        except Exception as e:
            print(colored(f"Error checking proxy {proxy}: {e}", 'red'))
    with open('proxy_list.txt', 'w') as f:
        for proxy in valid_proxies:
            f.write(f"{proxy}\n")
    print(colored(f"Checked proxies. {len(valid_proxies)} are valid.", 'blue'))

# Function to get working proxies
def get_proxies():
    with open('proxy_list.txt', 'r') as f:
        proxies = f.readlines()
    working_proxies = random.sample(proxies, min(4, len(proxies)))
    print(colored("Working proxies:", 'yellow'))
    for proxy in working_proxies:
        print(colored(proxy.strip(), 'green'))

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description=colored('ProxiiMaster: A proxy management tool.', 'cyan'))
    parser.add_argument('-S', '--scrape', action='store_true', help=colored('Scrape proxies', 'yellow'))
    parser.add_argument('-C', '--check', action='store_true', help=colored('Check proxy validity', 'yellow'))
    parser.add_argument('-N', '--num', type=int, help=colored('Number of proxies to check', 'yellow'))
    parser.add_argument('-G', '--get', action='store_true', help=colored('Get working proxies', 'yellow'))
    args = parser.parse_args()

    display_banner()

    print(colored(f"Arguments: {args}", 'magenta'))
    if args.scrape:
        scrape_proxies()
    if args.check:
        check_proxies(args.num)
    if args.get:
        get_proxies()

if __name__ == '__main__':
    main()
