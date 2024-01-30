from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import constants
from docx import Document

#Create a class that will be used to manage the functions of the chrome windows
class ChromeWindow(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(ChromeWindow, self).__init__()
        self.maximize_window()
        self.implicitly_wait(10)
    
    def new_page(self, page):
        self.execute_script(f"window.open('{page}');")
        self.switch_to.window(self.window_handles[1])

class Navigation(webdriver.Chrome):
    
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Navigation, self).__init__()
        self.maximize_window()
        self.implicitly_wait(10)
    
    def __exit__(self, exc_type, exc_value, trace):
        if self.teardown:
            self.quit()
    
    def return_page(self):
        self.back()
    def get_url(self):
        self.get(constants.jornada)
        self.maximize_window()
    
    def latest_news(self):
        news_bttn = self.find_element_by_xpath('//*[@id="header-ljn"]/div[2]/a')
        print(news_bttn.text)
        news_bttn.click()
    
    def title_news(self):
        title = self.find_element_by_xpath('')
        
class WordDocumentCreator:
    def __init__(self, file_name):
        self.file_name = file_name
        self.doc = Document()

    def add_paragraph(self, text):
        self.doc.add_paragraph(text)

    def add_heading(self, text, level=1):
        self.doc.add_heading(text, level=level)

    def save_document(self):
        self.doc.save(self.file_name)
        print(f"Documento Word '{self.file_name}' creado y guardado correctamente.")
