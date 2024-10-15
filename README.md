
# ProxiiMaster

ProxiiMaster is a proxy management tool that allows you to scrape, check, and get working proxies.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Scrape Proxies

To scrape proxies and save them to `proxy_list.txt`:
```bash
python ProxiiMaster.py -S
```

### Check Proxy Validity

To verify the gathered proxies and remove invalid ones:
```bash
python ProxiiMaster.py -C
```

### Get Working Proxies

To output 4 working proxies:
```bash
python ProxiiMaster.py -G
```

### Run All Commands

To run all the above commands in sequence:
```bash
python ProxiiMaster.py -S -C -G
```

## Requirements

- requests
- beautifulsoup4
- proxy-checker
