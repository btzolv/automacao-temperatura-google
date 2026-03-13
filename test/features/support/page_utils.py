# Autora: Beatriz
import unittest, base64, time, os, subprocess, pytz, allure, json, urllib3, behave, behave_html_formater
from behave import *
from selenium import webdriver
from support.ambiente import *

class PageUtils(unittest.TestCase):
    #Configurações e opções do Microsoft Edge
    edge_options = webdriver. EdgeOptions()
    edge_options.add_argument('--disable-site-isolation-trials')
    edge_options.add_argument('--ignore-certificate-erros')
    edge_options.add_argument('--start-maximized')
    driver = webdriver.Edge(options=edge_options)
    

    def abrir_um_browser(context, base_url):
        context.driver.get(base_url)
    def limpar_browser(context):
        context. driver. delete_all_cookies()
    def fechar_browser(context):
        context.driver.quit()