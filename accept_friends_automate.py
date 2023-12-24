from getpass import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LinkedInBot:
    def __init__(self):
        self.driver = self.setup_driver()
    def setup_driver(self):
        options = Options()
        return webdriver.Chrome(options=options)

    def login(self, email, password):
        self.driver.get('https://linkedin.com')
        email_field = self.driver.find_element(By.ID, 'session_key')
        password_field = self.driver.find_element(By.ID, 'session_password')
        email_field.send_keys(email)
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
        login_button.click()

    def navigate_to_my_network(self):
        MY_NETWORK_XPATH = '//*[@id="global-nav"]/div/nav/ul/li[2]/a'
        my_network = self.driver.find_element(By.XPATH, MY_NETWORK_XPATH)
        my_network.click()

    def accept_connection_requests(self):
        ACCEPT_BUTTON_XPATH = "//button[span[text()='Accept']]"
        accept_buttons = self.driver.find_elements(By.XPATH, ACCEPT_BUTTON_XPATH)

        for button in accept_buttons:
            button.click()
            time.sleep(1)

    def close(self):
        self.driver.quit()
if __name__ == "__main__":
    EMAIL = input("Enter your email: ")
    PASSWORD = getpass("Enter your password: ")
    bot = LinkedInBot()
    bot.login(EMAIL, PASSWORD)
    time.sleep(5)  # Wait for page to load before navigating to my network
    bot.navigate_to_my_network()
    time.sleep(5)  # Wait for page to load before accepting connection requests
    bot.accept_connection_requests()
    time.sleep(5)  # Wait for page to load before closing the browser
    bot.close()