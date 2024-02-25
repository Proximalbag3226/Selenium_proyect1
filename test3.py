from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from config.constants import *
import time

class Navigation():
    def __init__(self, teardown=False):
        self.teardown = teardown
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        super(Navigation, self).__init__()
        self.driver.implicitly_wait(10)
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    
    def get_url_navigator(self, url):
        self.driver.get(url)
        time.sleep(5)
        print(self.driver.title)
    
    def latest_news(self, xpath):
        news_bttn = self.driver.find_element(By.XPATH, xpath)
        news_bttn.click()
        time.sleep(5)
    
    def title_news(self, class_name, amount):
        try:
            elements = self.driver.find_elements(By.CSS_SELECTOR, class_name)
            titles = '\n\n'.join([f"{element.text}: {element.get_attribute('href')}" for element in elements[:amount]])
            print(titles)
            return titles
        except Exception as e:
            print(f"Error: {e}")

hola = Navigation()
hola.get_url_navigator(jornada)
hola.latest_news(xpath_jornada)
hola.title_news(title_jornada, 5)

        
        