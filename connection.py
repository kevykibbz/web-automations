from selenium import webdriver
import requests
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import logging
from colorama import init, Fore, Style



class ChromeConnector:
    def __init__(self):
        # Initialize colorama
        init(autoreset=True)

    def get_options(self):
        options=webdriver.ChromeOptions()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        #options.add_experimental_option("excludeSwitches",["enable logging"])
        options.add_argument('--disable-infobars')
        options.add_argument("--profile-directory=Default")
        options.add_argument("--start-maximized")
        # options.add_argument(f"--user-data-dir=C:\\Users\\{os.getlogin()}\\AppData\\Local\\Google\\Chrome\\User Data\\")
        options.add_experimental_option("detach",True)
        return options


    def chrome_driver(self):
        if self.check_connection():
            print(Fore.CYAN + "[?] Attempting to chrome chrome...")
            driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),
            options=self.get_options())
            return driver
        return None

    def check_connection(self):
        print(Fore.CYAN + "[?] checking connection...")
        try:
            requests.get("https://www.google.com",timeout=5)
            print(Fore.GREEN + "[+] Connection check successful." + Style.RESET_ALL)
            return True
        except(requests.exceptions.RequestException,requests.exceptions.Timeout) as e:
            logging.error(f"An error occurred: {e}")
            print(Fore.RED + f"[-] An error occurred: {e}" + Style.RESET_ALL)
            return False