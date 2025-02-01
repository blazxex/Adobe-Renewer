from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions #check if that element present
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta
import os
import time

def ItRenewer(Username,Password,Product):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)  

    driver.get('https://licenseportal.it.chula.ac.th/')

    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//input')))
    print(driver.title)


    username_input = driver.find_element(By.ID, 'UserName')
    username_input.send_keys(Username)

    password_input = driver.find_element(By.ID, 'Password')
    password_input.send_keys(Password)

    signin_button = driver.find_element(By.XPATH, '//button')
    signin_button.click()
    time.sleep(2)
    driver.get('https://licenseportal.it.chula.ac.th/Home/Borrow')
    
    dropdown = Select(driver.find_element(By.ID,'ProgramLicenseID'))
    dropdown.select_by_visible_text(Product)  

    wait.until(expected_conditions .presence_of_all_elements_located((By.ID, 'ExpiryDateStr')))
    
    expiry_date_input = driver.find_element(By.ID, 'ExpiryDateStr')
    week = datetime.now() + timedelta(days=7)
    driver.execute_script("arguments[0].value = arguments[1];", expiry_date_input, week.strftime('%d/%m/%Y'))
    time.sleep(2)
    save_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    save_button.click()
    print(driver.title)

    driver.quit()

###
Username = os.environ['USERNAME']
Password = os.environ['PASSWORD']
Product = 'Adobe ด้านกราฟิก สำหรับนิสิต'
ItRenewer(Username,Password,Product)
