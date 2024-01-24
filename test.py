from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el navegador Chrome
options = webdriver.ChromeOptions()
options.add_argument('--disable-web-security')

driver = webdriver.Chrome(options=options)

try:
    #Nos dirigimos a la primer pagina de noticas que en este caso sera la jornada, maximozamos la ventana y esperamos si es que aparecen anuncios o alertas en la pagina
    driver.get("https://www.jornada.com.mx")
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    
    time.sleep(5)
    # Imprimir el título de la página actual
    print("Título de la página:", driver.title)

finally:
    # Cerrar el navegador al finalizar
    driver.quit()
