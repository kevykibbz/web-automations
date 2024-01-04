from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from connection import ChromeConnector
from colorama import init, Fore, Style
import pandas as pd

class Scavange:
    def __init__(self):
        # Initialize colorama
        init(autoreset=True)
        
    def run(self):
        target = "https://stenosearch.com/_connect/Court_ReportersDIR.html#Nebraska_Court_Reporters"
        get_driver = ChromeConnector()
        driver = get_driver.chrome_driver()

        if driver:
            print(Fore.GREEN + "[+] Chrome browser opened successfully. Redirecting to target..." + Style.RESET_ALL)
            driver.get(target)

            # Wait for the page to load and find email elements
            try:
                email_elements = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href, "mailto:")]'))
                )

                # Extract email addresses
                email_addresses = [element.get_attribute("href").split(":")[1] for element in email_elements]

                # Print the extracted email addresses and count
                count = len(email_addresses)
                for email in email_addresses:
                    print(email)

                print(Fore.YELLOW + f"[+] Extracted {count} Email Addresses:" + Style.RESET_ALL)
                print(Fore.CYAN + "[+] Writing into a file..." + Style.RESET_ALL)
                # Write email addresses to an Excel file
                df = pd.DataFrame({'Email Addresses': email_addresses})
                df.to_excel('extracted_emails.xlsx', index=False, engine='openpyxl')
                print(Fore.GREEN + "[+] Email addresses written to 'extracted_emails.xlsx'" + Style.RESET_ALL)

            except Exception as e:
                print(Fore.RED + f"[-] An error occurred: {e}" + Style.RESET_ALL)

            finally:
                # Close the browser
                driver.quit()


if __name__ == '__main__':
    scavenger = Scavange()
    scavenger.run()
