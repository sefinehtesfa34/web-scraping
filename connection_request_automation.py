import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LinkedInBot:
    def __init__(self):
        self.options = Options()
        self.driver = webdriver.Chrome(options=self.options)
        self.linkedin_url = 'https://linkedin.com'
        self.wait = WebDriverWait(self.driver, 10)
        self.connect_buttons_xpath = "//button[span[text()='Connect']]"
        self.title_xpath = '//*[starts-with(@id, "ember")]/div/section/div[2]/a/span[4]'
        self.mutual_connections_xpath = '//*[starts-with(@id, "ember")]/div/section/div[3]/div/div/span/span'

    def login(self):
        self.driver.get(self.linkedin_url)
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, 'session_key')))
        password_field = self.wait.until(EC.presence_of_element_located((By.ID, 'session_password')))
        email_field.send_keys(EMAIL)
        password_field.send_keys(PASSWORD)
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')))
        login_button.click()

    def navigate_to_my_network(self):
        my_network_xpath = '//*[@id="global-nav"]/div/nav/ul/li[2]/a'
        my_network = self.wait.until(EC.element_to_be_clickable((By.XPATH, my_network_xpath)))
        my_network.click()

    def get_connection_elements(self):
        connect_buttons = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.connect_buttons_xpath)))
        titles = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.title_xpath)))
        mutual_friends = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.mutual_connections_xpath)))

        return connect_buttons, titles, mutual_friends

    def send_connection_requests(self, connect_buttons, titles, mutual_friends):
        for button, title, mutual_count in zip(connect_buttons, titles, mutual_friends):
            try:
                mutual_count = int(mutual_count.text.split()[0])
            except ValueError:
                mutual_count = 0
            title_text = title.text.lower()
            is_software_engineer = 'software' in title_text
            is_software_engineer = title.text.lower().find('software') != -1
            is_machine_learning_engineer = title.text.lower().find('machine learning') != -1
            is_ai_engineer = title.text.lower().find('ai') != -1
            is_ml_engineer = title.text.lower().find('ml') != -1
            is_data_scientist = title.text.lower().find('data scientist') != -1
            is_data_analyst = title.text.lower().find('data analyst') != -1
            is_data_engineer = title.text.lower().find('data engineer') != -1
            is_ml_engineer_or_ai_or_data_scientist_or_analyst = is_ai_engineer or is_ml_engineer or is_data_scientist or is_data_analyst
            
            if is_software_engineer or is_data_engineer or is_machine_learning_engineer or is_ml_engineer_or_ai_or_data_scientist_or_analyst:
                if mutual_count >= 100:
                    button.click()
                    print(f'Sent connection request to {title_text}')
                else:
                    print(f'Not sending connection request to {title_text} because mutual friends count is less than 100')
                    print(f'Mutual friends count: {mutual_count}')
            time.sleep(3)
    def run(self):
        self.login()
        self.navigate_to_my_network()
        connect_buttons, titles, mutual_friends = self.get_connection_elements()
        self.send_connection_requests(connect_buttons, titles, mutual_friends)

if __name__ == "__main__":
    EMAIL = getpass('Enter your email: ')
    PASSWORD = getpass('Enter your password: ')
    linkedin_bot = LinkedInBot()
    linkedin_bot.run()
