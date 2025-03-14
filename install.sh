#!/bin/bash
# Frissítjük a csomaglistát
sudo apt-get update

# Telepítjük a szükséges eszközöket
sudo apt-get install -y nmap nikto macchanger aircrack-ng python3-tk gobuster git

# SecLists repository letöltése
git clone https://github.com/danielmiessler/SecLists.git --depth=1

