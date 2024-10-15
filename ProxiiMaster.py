
import requests
from bs4 import BeautifulSoup
import random
import argparse
from proxy_checker import ProxyChecker

# List of proxy sources
proxy_sources = [
    'https://www.proxy-list.download/api/v1/get?type=https',
]

# Function to scrape proxies
def scrape_proxies():
    proxies = []
    for source in proxy_sources:
        response = requests.get(source)
        proxies.extend(response.text.splitlines())
    with open('proxy_list.txt', 'w') as f:
        for proxy in proxies:
            f.write(f"{proxy}\n")
    print(f"Scraped {len(proxies)} proxies.")

# Function to check proxy validity
def check_proxies():
    checker = ProxyChecker()
    valid_proxies = []
    with open('proxy_list.txt', 'r') as f:
        proxies = f.readlines()
    for proxy in proxies:
        proxy = proxy.strip()
        result = checker.check_proxy(proxy)
        if result and result['timeout'] < 2000:
            valid_proxies.append(proxy)
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
    parser.add_argument('-G', '--get', action='store_true', help='Get working proxies')
    args = parser.parse_args()

    if args.scrape:
        scrape_proxies()
    if args.check:
        check_proxies()
    if args.get:
        get_proxies()

if __name__ == '__main__':
    main()
