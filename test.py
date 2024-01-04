from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

user_data_dir = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Google\\Chrome\\User Data"

options=Options()
options.add_experimental_option("detach",True)
options.add_argument("--disable-infobars")
options.add_argument("--profile-directory=Default")
options.add_argument("--start-maximized")
options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option("excludeSwitches",["enable logging"])
options.add_experimental_option("useAutomationExtension",False)


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://wwww.facebook.com")