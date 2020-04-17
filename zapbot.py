from selenium import webdriver
import time

class WhattsappBot():
    def __init__(self):
        self.mensagem = "Mensagem enviada pelo ZapBot, criado por Diego favor responder como recebido."
        self.contatos = ["Douglas Tim","Mena"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome('/home/diego/Projetos/robos/zapbot/chromedriver')

    def EnviarMensagens(self):
        print("Acessando whattsappWeb...")
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for contatos in self.contatos:
            campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{contatos}']")
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(3)
            chat_box.click()
            print("Escrevendo mensagem...")
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhattsappBot()
bot.EnviarMensagens()