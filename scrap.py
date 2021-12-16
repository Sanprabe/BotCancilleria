# import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime



def buscarSiHayCitas ():
    driver = webdriver.Chrome("C:\SeleniumDrivers\chromedriver.exe")
    driver.get('https://tramitesmre.cancilleria.gov.co/tramites/enlinea/agendamiento.xhtml')
    time.sleep(2)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "buttonPreSolicitar")))

    firstButton = driver.find_element_by_id("buttonPreSolicitar")
    firstButton.click()
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "inputOficina:select:entrada")))

    firstSelect = Select(driver.find_element_by_id("inputOficina:select:entrada"))
    firstSelect.select_by_visible_text('BTA. CALLE 100')
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "inputTramite:select:entrada")))

    secondSelect = Select(driver.find_element_by_id("inputTramite:select:entrada"))
    secondSelect.select_by_visible_text('PASAPORTE - ORDINARIO')
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "inputServicio:select:entrada")))

    thirdSelect = Select(driver.find_element_by_id("inputServicio:select:entrada"))
    thirdSelect.select_by_value('SOLICITAR')
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ui-messages-error-summary")))

    try:
        error = driver.find_element_by_class_name("ui-messages-error-summary")
        print('---------------------------------------------------------------------------------')
        print(error.text)
        print(error.text)
        print(error.text)
        print(error.text)
        print(error.text)
        print(error.text)
        print(error.text)
        print(error.text)
    except:
        print('---------------------------------------------------------------------------------')
        print('Hay citas!!!!!!')
        print('Hay citas!!!!!!')
        print('Hay citas!!!!!!')
        print('Hay citas!!!!!!')
        print('Hay citas!!!!!!')
        print('Hay citas!!!!!!')
        print('Hay citas!!!!!!')
        print('Hay citas!!!!!!')

    driver.close()


while True:
    buscarSiHayCitas()
    print('-------------------------',datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '-------------------------')
    time.sleep(20)