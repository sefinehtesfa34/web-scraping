from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from credential import USERNAME, PASSWORD, PHONE

COMMON_ID = 'mount_0_0_K0'
COMMON_PATH = 'div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[3]'
FRIENDS_XPATH = f'//*[@id="{COMMON_ID}"]/{COMMON_PATH}/*/div[2]/div[1]/a/span'
ABOUT_XPATH = f'//*[@id="{COMMON_ID}"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]/div[1]/span'
CONTACTS_XPATH = f'//*[@id="{COMMON_ID}"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[1]/*/a/span'

def login(driver):
    facebook = 'https://facebook.com'
    URL = 'https://www.facebook.com/sefineh.tesfa.3/friends'
    driver.get(facebook)

    username_field = driver.find_element(By.ID, 'email')
    password_field = driver.find_element(By.ID, 'pass')
    username_field.send_keys(PHONE)
    password_field.send_keys(PASSWORD)

    login_button = driver.find_element(By.NAME, 'login')
    login_button.click()
    WebDriverWait(driver, 10).until(EC.url_contains("facebook.com"))
    driver.get(URL)

def click_element_by_xpath(driver, xpath):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.click()
    except NoSuchElementException:
        print(f"Element not found: {xpath}")

def get_contacts_info(driver):
    try:
        contacts = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="{COMMON_ID}"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div'))
        )
        print(contacts.text.split('\n'))
    except NoSuchElementException:
        print("Contacts information not found")

def pipline(driver):
    click_element_by_xpath(driver, ABOUT_XPATH)
    click_element_by_xpath(driver, CONTACTS_XPATH)
    get_contacts_info(driver)
    driver.execute_script("window.history.go(-1)")
    driver.execute_script("window.history.go(-1)")

def main():
    options = Options()
    driver = webdriver.Chrome(options=options)
    login(driver)
    friends_xpath = f'//*[@id="{COMMON_ID}"]/{COMMON_PATH}/*/div[2]/div[1]/a/span'
    friends = driver.find_elements(By.XPATH, friends_xpath) 
    n_friends = len(friends)
    # Loop through friends
    for index in range(1, n_friends + 1):
        friend_xpath = f'//*[@id="{COMMON_ID}"]/{COMMON_PATH}/div[{index}]'
        click_element_by_xpath(driver, friend_xpath)
        pipline(driver)
if __name__ == "__main__":
    main()
