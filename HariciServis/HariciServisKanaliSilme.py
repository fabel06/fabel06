import time
##
from select import select
from selenium import webdriver
# chrome driver
from selenium.webdriver.chrome.service import Service
# --chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service_obj= Service("/Users/feskin/Desktop/document/chromedriver.exe");
driver: WebDriver = webdriver.Chrome(service=service_obj)
driver.get("http://10.1.112.107/#/pages/login")
driver.maximize_window()
#--find locators
driver.find_element(By.NAME,"username").send_keys("@dettaadmin")
driver.find_element(By.NAME, "password").send_keys("admin")

#//tagname[@attribute='value']  //input[@type='submit']
driver.find_element(By.XPATH, "(//button[contains(text(),'Oturum Açınız')])[1]").click()
time.sleep(1)
#Tanımlamalar menüsüne tıkla
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']/div[@class='app-body']/div[@class='sidebar']/nav[@class='sidebar-nav']/ul[@class='nav']/li[8]/a[1]").click()
time.sleep(1)
#Harici Servis Kanali alt menüsüne tıkla
driver.find_element(By.XPATH, "//a[contains(text(),'Harici Servis Kanalı')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//td[normalize-space()='none8']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//tbody//button[4]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Evet']").click()
time.sleep(2)
driver.close()
