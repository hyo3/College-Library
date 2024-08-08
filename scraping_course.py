from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

from dotenv import load_dotenv; load_dotenv()
import os


manaba_username = os.getenv('MANABA_USERNAME')
manaba_password = os.getenv('manaba_password')

# chromeドライバのパスとオプションを設定
chrome_path = 'webdriver/chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument('--headless')  # ヘッドレスモードで起動
service = Service(executable_path=chrome_path)

def get_courses():
    # chromeドライバを起動
    with webdriver.Chrome(options=chrome_options) as driver:

        # 指定したURLのページを開く
        url = "https://manaba.kic.kagoshima-u.ac.jp/ct/home"
        
        driver.get(url)
        driver.implicitly_wait(2)

        
        manaba_username_field = driver.find_element(By.NAME, "j_username")
        manaba_username_field.send_keys(manaba_username)

        manaba_password_field = driver.find_element(By.NAME, "j_password")
        manaba_password_field.send_keys(manaba_password)

        driver.implicitly_wait(2)

        login_button = driver.find_element(By.NAME, "_eventId_proceed")
        login_button.click()

        driver.implicitly_wait(2)
        
        courses_html = driver.find_elements(By.CSS_SELECTOR, ".course a[href^='course_']")
        courses = list(map(lambda course : course.text, courses_html))
        
        print(courses)

        return courses

if __name__ == "__main__":
    get_courses()