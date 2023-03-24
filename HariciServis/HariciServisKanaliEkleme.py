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
driver.find_element(By.XPATH, "//span[contains(text(),'Yeni Harici Servis Kanalı Ekle')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder='Ağ Adı']").send_keys("none8")
driver.find_element(By.XPATH, "//input[@placeholder='Açıklama']").send_keys("yok")
time.sleep(1)
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//app-networkmanagement[@class='ng-star-inserted']/p-dialog//div[@role='dialog']//form/div/div[2]/div[2]/p-dropdown[@name='channelList']//span[.='Lütfen Kanal Seçiniz']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='vuhf1']").click()
driver.find_element(By.XPATH, "//input[@name='netIp']").send_keys("1921681.0/24")
driver.find_element(By.XPATH, "//input[@name='ncGateway']").send_keys("17221.1.9")
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(),'Değişiklikleri Kaydet')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//td[normalize-space()='none8']").click()
driver.find_element(By.XPATH, "//span[contains(text(),'Harici Servis Kanalına Atanan Servisler')]").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Servis Ekle']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-networkmanagement[@class='ng-star-inserted']/p-dialog//div[@role='dialog']//form/div//p-dropdown[@name='serviceList']//span[.='Lütfen Servis Seçiniz']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='ICMP']").click()
driver.find_element(By.XPATH, "//span[contains(text(),'Değişiklikleri Kaydet')]").click()
time.sleep(1)
#Harici Servis kanalını aktif'e alma
driver.find_element(By.XPATH, "//button[@class='p-button-success p-button p-component p-button-icon-only']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='Evet']").click()
time.sleep(2)
driver.close()

