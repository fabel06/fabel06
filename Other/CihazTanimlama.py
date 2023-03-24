import time
from selenium import webdriver
# chrome driver
from selenium.webdriver.chrome.service import Service
# --chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

service_obj= Service("/Users/feskin/Desktop/document/chromedriver.exe");
driver: WebDriver = webdriver.Chrome(service=service_obj)

driver.get("http://10.1.115.157/#/pages/login")
driver.maximize_window()
#--find locators
driver.find_element(By.NAME,"username").send_keys("@admin")
driver.find_element(By.NAME, "password").send_keys("admin")

#//tagname[@attribute='value']  //input[@type='submit']
driver.find_element(By.XPATH, "(//button[contains(text(),'Oturum Açınız')])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']/div[@class='app-body']/div[@class='sidebar']/nav[@class='sidebar-nav']/ul[@class='nav']/li[8]/a[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[normalize-space()='Cihaz']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Yeni Cihaz Ekle']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//span[@class='p-dropdown-trigger-icon ng-tns-c62-17 pi pi-chevron-down']").click()
driver.find_element(By.XPATH, "//span[contains(text(),'YTM Ağ Kontrolcüsü')]").click()
driver.find_element(By.XPATH, "//input[@id='deviceName']").send_keys("ncvuhf2")
driver.find_element(By.XPATH, "//input[@id='deviceBrand']").send_keys("onur")
driver.find_element(By.XPATH, "//input[@id='deviceModel']").send_keys("onur")
driver.find_element(By.XPATH, "//input[@id='deviceSerialNumber']").send_keys("45")
driver.find_element(By.XPATH, "//input[@id='deviceVersionNumber']").send_keys("1.0")
driver.find_element(By.XPATH, "//input[@id='deviceDescription']").send_keys("yok")
driver.find_element(By.XPATH, "//input[@id='location']").send_keys("telsiz")
driver.find_element(By.XPATH, "//input[@id='ipAddress']").send_keys("17231.1.31/24")
driver.find_element(By.XPATH, "//input[@id='port']").send_keys("58001")
driver.find_element(By.XPATH, "//input[@id='gateway']").send_keys("17231.1.5")
driver.find_element(By.XPATH, "//input[@id='macAddresss']").send_keys("aa:22:33:44:55:66")
time.sleep(2)

driver.find_element(By.XPATH, "//button[@name='saveDeviceButton']").click()



















