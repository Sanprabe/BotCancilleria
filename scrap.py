# import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from datetime import datetime

count = 0

def buscarSiHayCitas():

    def askService (servicio):

        time.sleep(randomTime)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "inputServicio:select:entrada")))

        thirdSelect = Select(driver.find_element_by_id("inputServicio:select:entrada"))
        thirdSelect.select_by_value(servicio)
        
        time.sleep(randomTime)

        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "ui-messages-error-summary")))
            error_ = driver.find_element_by_class_name("ui-messages-error-summary")
            print('---------------------------------------------------------------------------------')
            if error_: print(f'No hay citas en {oficina} para {servicio}')

        except:
            print('---------------------------------------------------------------------------------')
            print(f'Hay citas para en {oficina} para {servicio}' )
        
        finally:
            print('-------------------------',datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '-------------------------')


    def askSite (oficina):
        
        time.sleep(2)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "inputOficina:select:entrada")))

        firstSelect = Select(driver.find_element_by_id("inputOficina:select:entrada"))
        firstSelect.select_by_visible_text(oficina)
        
        time.sleep(randomTime)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "inputTramite:select:entrada")))

        secondSelect = Select(driver.find_element_by_id("inputTramite:select:entrada"))
        secondSelect.select_by_visible_text('PASAPORTE - ORDINARIO')

        servicios = ['SOLICITAR', 'ENTREGA']

        for servicio in servicios:
            askService (servicio)


    randomTime = random.uniform(2.2, 3.5)

    driver = webdriver.Chrome("C:\SeleniumDrivers\chromedriver.exe")
    driver.get('https://tramitesmre.cancilleria.gov.co/tramites/enlinea/agendamiento.xhtml')
    time.sleep(2)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "buttonPreSolicitar")))

    firstButton = driver.find_element_by_id("buttonPreSolicitar")
    firstButton.click()

    oficinas = ['BTA. CENTRO', 'BTA. CALLE 53', 'BTA. CALLE 100']

    for oficina in oficinas:
        askSite(oficina)

    driver.close()

while True:
    buscarSiHayCitas()
    count += 1
    print('//////////////////////////////////////////////', count, '//////////////////////////////////////////////')
    time.sleep(random.randint(150,250))