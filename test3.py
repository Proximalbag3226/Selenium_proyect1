from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from config.constants import *
import time
from docx import Document
import requests

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
    
class WordDocumentCreator:
    def __init__(self, file_name):
        self.file_name = file_name
        self.doc = Document()
        
    def add_paragraph(self, text):
        self.doc.add_paragraph(text)
    
    def add_heading(self, text, level=1):
        self.doc.add_heading(text, level = level)
        
    def save_document(self):
        self.doc.save(self.file_name)
        print(f"Word document {self.file_name} created and save whit success")

class image_management:
    def __init__(self, img_name):
        self.img_name = img_name
        self.driver = self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
    def get_url(self, amount_img, class_img):
        img = self.driver.find_elements(By.CLASS_NAME, class_img)
        for images in img[:amount_img]:            
            link = images.get_attribute('src')
        return link
    
    def request_managment(self, link):
        news_img = requests.get(link)
        if news_img.status_code == 200:
            print(link)
            i += 1
            Image_name = "Img" + str(i) + '.jpg'
            with open(Image_name, 'wb') as img:
                img.write(news_img.content) 
                
hola = Navigation()
hola.get_url_navigator(jornada)
hola.latest_news(xpath_jornada)
hola.title_news(title_jornada, 5)

        
        