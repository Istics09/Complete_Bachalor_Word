# Complete_Bachelor_Work (Kraken)

Hi all! Here you can find my complete bachelor work, which aims to provide a simple penetration testing tool with a GUI interface.

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Disclaimer](#disclaimer)
5. [License](#license)

---

## Overview
This repository contains two main components:
1. **install.sh** – A script that installs all required tools and libraries for penetration testing.  
2. **main.py** – The primary application that provides a GUI for running various penetration tests.

The script automatically installs several common tools, including:
- **nmap**
- **gobuster**
- **nikto**
- **aircrack-ng**
- **hydra**

It also downloads useful wordlists from Git, which can be utilized for brute-forcing (password login attempts). This setup allows you to quickly get started with basic penetration testing tasks.

---

## Installation
Before running the main tool, please install the required dependencies by executing the `install.sh` script **with root privileges**. From the repository root:

```bash
sudo ./install.sh
