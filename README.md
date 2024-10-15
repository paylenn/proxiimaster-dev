
# ProxiiMaster

![ProxiiMaster Banner](https://via.placeholder.com/728x90.png?text=ProxiiMaster)
![Enhanced ProxiiMaster](https://via.placeholder.com/728x90.png?text=Enhanced+ProxiiMaster)

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/paylenn/proxiimaster-dev/actions)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/paylenn/proxiimaster-dev/blob/main/LICENSE)

ProxiiMaster is a powerful proxy management tool that allows you to scrape, check, and retrieve working proxies efficiently.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Display Banner](#display-banner)
  - [Scrape Proxies](#scrape-proxies)
  - [Check Proxies](#check-proxies)
  - [Get Working Proxies](#get-working-proxies)
- [License](#license)

## Features
- 🚀 **Scrape Proxies**: Scrape proxies from multiple sources.
- ✅ **Check Proxies**: Check the validity of proxies.
- 📋 **Retrieve Proxies**: Get a list of working proxies.

## Installation
To install the required dependencies, run:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Usage
ProxiiMaster provides a command-line interface (CLI) for managing proxies.

### Display Banner
\`\`\`bash
python3 ProxiiMaster.py
\`\`\`

### Scrape Proxies
\`\`\`bash
python3 ProxiiMaster.py -S
\`\`\`

### Check Proxies
To check all proxies:
\`\`\`bash
python3 ProxiiMaster.py -C
\`\`\`

To check a specific number of proxies:
\`\`\`bash
python3 ProxiiMaster.py -C -N <number>
\`\`\`

### Get Working Proxies
\`\`\`bash
python3 ProxiiMaster.py -G
\`\`\`

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
