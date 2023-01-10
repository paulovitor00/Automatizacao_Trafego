import datetime

import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import datetime
from selenium.webdriver.common.keys import Keys
import pyautogui as py
import time
import pandas as pd
import matplotlib.pyplot as plt

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)


def gerar_relatorio():
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2
    })
    driver.maximize_window()
    driver.get("https://www.facebook.com/")

    # realiza login#
    email_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div['
                                                  '1]/form/div[1]/div[ '
                                                  '1]/input')
    email_element.send_keys('**********')
    password_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div['
                                                     '1]/form/div[1]/div[2]/div/input')
    password_element.send_keys('********')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div['
                                                                          '1]/div/div/div/div[2]/div/div['
                                                                          '1]/form/div[2]/button'))).click()

    try:
        time.sleep(2)
        alert = WebDriverWait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        text = alert.text
        alert.accept()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div['
                                                                              '3]/div/div/div/div[1]/div[1]/div/div['
                                                                              '1]/div/div/div[1]/div/div/div[1]/div['
                                                                              '1]/ul/li[2]/div/a/div[1]/div['
                                                                              '2]/div/div/div/div/span/span'))).click()

    except:
        # acessa o gerenciador de anúncios#
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div['
                                                                              '3]/div/div/div/div[1]/div[1]/div/div['
                                                                              '1]/div/div/div[1]/div/div/div[1]/div['
                                                                              '1]/ul/li[2]/div/a/div[1]/div['
                                                                              '2]/div/div/div/div/span/span'))).click()

    # clica no icone para trocar conta de ads#
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div/div/div['
                                                                          '1]/div/span/div/div[1]/div/div/div[ '
                                                                          '1]/span/div/div/div/div[1]/div[1]/div/div['
                                                                          '2]/div/div/button/div/div/div/div/div/img'))).click()

    time.sleep(3)
    # clica na conta de anúncio#
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div/div/div/div/div/div/div['
                                  '2]/div/div/div/div/div/li[2]/a/div[2]/span/div').click()
    time.sleep(8)
    # clica no botão ferramentas#
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div['
                                  '1]/span/div/div/div/div[1]/div[1]/div[1]/span/div/div[1]/div[2]/div/span/div/div['
                                  '2]/div/div').click()
    time.sleep(3)
    # clica no botão relatório de anúncios#
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/span/div/div[1]/div/div/div['
                                  '1]/span/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div['
                                  '5]/div/div[2]/div[6]/div[1]/a/div/div').click()
    time.sleep(10)
    # Gera um novo relatório#
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/span/div/div[1]/div[2]/div[2]/div/div/div['
                                  '2]/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div/span/div/div/div['
                                  '2]').click()

    time.sleep(2)
    py.typewrite('relatório final', interval=0.002)

    # seleciona todas as contas de anúncio#
    driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div['
                                  '3]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div/div/div['
                                  '1]/input').click()
    time.sleep(3)
    # clica em criar relatorio#
    criar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[text() = "Criar"]'))
    )
    criar.click()

    # clica em continuar#
    continuar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[text() = "Continuar"]')))
    continuar.click()

    # seleciona a opção de mostrar o nome das campanhas de anúncio#
    campanhaName = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div['
                                                                                             '1]/div/div/div/div/div'
                                                                                             '/span/div/div[1]/div['
                                                                                             '2]/div['
                                                                                             '2]/div/div/div/div['
                                                                                             '3]/div[2]/div['
                                                                                             '1]/div/div/div/div/div['
                                                                                             '1]/div[4]/div[2]/div['
                                                                                             '1]/div/div[2]/div['
                                                                                             '1]/div/div/div['
                                                                                             '2]/div/div/div/div['
                                                                                             '2]/div['
                                                                                             '1]/label/div/div/div['
                                                                                             '1]/div/div/div['
                                                                                             '1]/input')))
    campanhaName.click()
    # seleciona a opção de mostrar a idade do público de todas campanhas#
    idade = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[text() = "Idade"]')))
    idade.click()
    # clica em exportar#
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div['
                                                                          '1]/div/span/div/div[1]/div[2]/div['
                                                                          '2]/div/div/div/div[1]/div/div['
                                                                          '2]/div/span/div/div/span/div/div['
                                                                          '2]/div/div'))).click()
    # seleciona o formato do arquivo para CSV#
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div['
                                                                          '1]/div/div/div/div/div[2]/div[1]/div['
                                                                          '2]/div[2]/div/div[2]/div/div/div/label['
                                                                          '3]/div/div/div[2]/div'))).click()

    # finaliza a exportação#
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div['
                                                                          '1]/div/div/div/div/div[3]/div/div[2]/div['
                                                                          '1]/span/div/div/div'))).click()
    input('f')


def extracao():
    a = pd.read_csv(
        '/Users/paulovitor/PycharmProjects/Automatizacao_Trafego/venv/Relatório-sem-título-Jan-1-2023-a-Jan-9'
        '-2023.csv')
