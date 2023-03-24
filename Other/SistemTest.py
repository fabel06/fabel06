import time

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

driver.get("http://10.1.112.109/#/pages/login")
driver.maximize_window()
#Login olma ekranında kullanıcı adı ve password girişi yapılır

driver.find_element(By.NAME,"username").send_keys("@dettaadmin")
driver.find_element(By.NAME, "password").send_keys("admin")

#//tagname[@attribute='value']  //input[@type='submit']
driver.find_element(By.XPATH, "(//button[contains(text(),'Oturum Açınız')])[1]").click() #Oturum Açınız Butonuna tıkla
time.sleep(2)
#sistem yönetimi menüsüne tıkla
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//nav[@class='sidebar-nav']/ul[@class='nav']/li[16]/a[@id='dropdownMenu']").click()
time.sleep(1)
#CİT yönetimi alt menüsüne tıkla
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//nav[@class='sidebar-nav']/ul[@class='nav']/li[16]/ul[@class='nav-dropdown-items']/li[2]/a[@href='#/systemManagement/citManagement']").click()
time.sleep(1)
#Sistem Test butonuna tıkla
driver.find_element(By.XPATH, "//span[normalize-space()='Sistem Test']").click()
print("Sistem Testi başlatıldı...")
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-citmanagement[@class='ng-star-inserted']/p-toast//p-toastitem//div[@role='alert']//div[.='Bilgi']")

print("Sistem Testi tamamlandı.")


