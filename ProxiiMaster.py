
import requests
from bs4 import BeautifulSoup
import random
import argparse
from proxy_checker import ProxyChecker
from termcolor import colored

def display_banner():
    banner = colored('ProxiiMaster', 'green', attrs=['bold'])
    print(banner)

# List of proxy sources
proxy_sources = [
    'https://www.proxy-list.download/api/v1/get?type=https',
]

# Function to scrape proxies
def scrape_proxies():
    proxies = []
    for source in proxy_sources:
        try:
            response = requests.get(source)
            response.raise_for_status()
            proxies.extend(response.text.splitlines())
        except requests.RequestException as e:
            print(f"Error fetching proxies from {source}: {e}")
    with open('/home/user/proxiimaster-dev/proxy_list.txt', 'w') as f:
        for proxy in proxies:
            f.write(f"{proxy}\n")
    print(f"Scraped {len(proxies)} proxies.")

# Function to check proxy validity
def check_proxies(num_proxies=None):
    print("check_proxies function called")
    checker = ProxyChecker()
    valid_proxies = []
    with open('proxy_list.txt', 'r') as f:
        proxies = f.readlines()
    print(f"Total proxies available: {len(proxies)}")
    if num_proxies is None:
        num_proxies = len(proxies)
    for proxy in proxies[:num_proxies]:
        proxy = proxy.strip()
        try:
            result = checker.check_proxy(proxy)
            print(f"Checking proxy: {proxy}, Result: {result}")
            result = checker.check_proxy(proxy)
            if result and result['timeout'] < 2000:
                valid_proxies.append(proxy)
        except Exception as e:
            print(f"Error checking proxy {proxy}: {e}")
    with open('proxy_list.txt', 'w') as f:
        for proxy in valid_proxies:
            f.write(f"{proxy}\n")
    print(f"Checked proxies. {len(valid_proxies)} are valid.")

# Function to get working proxies
def get_proxies():
    with open('proxy_list.txt', 'r') as f:
        proxies = f.readlines()
    working_proxies = random.sample(proxies, min(4, len(proxies)))
    for proxy in working_proxies:
        print(proxy.strip())

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description='ProxiiMaster: A proxy management tool.')
    parser.add_argument('-S', '--scrape', action='store_true', help='Scrape proxies')
    parser.add_argument('-C', '--check', action='store_true', help='Check proxy validity')
    parser.add_argument('-N', '--num', type=int, help='Number of proxies to check')
    parser.add_argument('-G', '--get', action='store_true', help='Get working proxies')
    args = parser.parse_args()

    display_banner()

    print(f"Arguments: {args}")
    if args.scrape:
        scrape_proxies()
    if args.check is not None:
         check_proxies(args.num)
    if args.get:
        get_proxies()

if __name__ == '__main__':
    main()
