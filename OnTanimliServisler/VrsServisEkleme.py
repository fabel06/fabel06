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
#Servis alt menüsüne tıklanılır
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//nav[@class='sidebar-nav']/ul[@class='nav']/li[8]/ul[@class='nav-dropdown-items']/li[4]/a[@href='#/definitions/service']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Yeni Servis Ekle']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//body/app-dashboard[@class='ng-star-inserted']//app-servicedefinition[@class='ng-star-inserted']/p-dialog/div/div[@role='dialog']//form/div//p-autocomplete[@name='serviceName']//input[@role='searchbox']").send_keys("VRS")
driver.find_element(By.XPATH,"//input[@id='serviceDesc']").send_keys("Yok")
time.sleep(1)
driver.find_element(By.XPATH,"//body/app-dashboard[@class='ng-star-inserted']//app-servicedefinition[@class='ng-star-inserted']/p-dialog/div/div[@role='dialog']//form/div//p-dropdown[@name='serviceQdTypes']//span[.='Seçiniz']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//li[@aria-label='Veri']").click()
driver.find_element(By.XPATH,"//span[@class='p-dropdown-trigger-icon ng-tns-c57-21 pi pi-chevron-down']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//li[@aria-label='Düşük']").click()
driver.find_element(By.XPATH,"//span[@class='ng-tns-c57-22 p-dropdown-label p-inputtext p-placeholder ng-star-inserted']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//li[@aria-label='Yüksek']").click()
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-servicedefinition[@class='ng-star-inserted']/p-dialog/div/div[@role='dialog']/div[@class='ng-tns-c31-15 p-dialog-content']/form/div//p-dropdown[@name='errorLimitValue']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Normal']").click()
driver.find_element(By.XPATH, "//span[@class='p-dropdown-trigger-icon ng-tns-c57-24 pi pi-chevron-down']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='TCP']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//p-chips[@id='destPort']//ul//input[@type='text']").send_keys("9500")
time.sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(),'Değişiklikleri Kaydet')]").click()



