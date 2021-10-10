
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome import options
import time

class WhatsaapBoot:
    def __init__(self):
        self.text = "O mãeeeeeeeee"
        self.grupo = ["Mãe"]
        options= webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def verificação(self):
        self.driver.get('https://web.whatsapp.com')
        while len(self.driver.find_elements_by_id('side')) < 1:
            time.sleep(1)

    def EnviarMensagens(self):    
        for grupos in self.grupo:#para grupos dentro de "TCM" faça se achar grupo no span da barra ao lado click nela
            campo_grupo = self.driver.find_element_by_xpath(
            f"//span[@title='{grupos}']")
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.text)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsaapBoot()
bot.verificação()
bot.EnviarMensagens()