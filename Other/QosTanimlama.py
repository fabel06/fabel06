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
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']/div[@class='app-body']/div[@class='sidebar']/nav[@class='sidebar-nav']/ul[@class='nav']/li[8]/a[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[normalize-space()='QoS']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Yeni QoS Ekle']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name='qdName']").send_keys("yeni3")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-qos-definition[@class='ng-star-inserted']/p-dialog[2]/div/div[@role='dialog']//form//p-dropdown[@name='qdBandType']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Veri']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name='description']").send_keys("YOK")
driver.find_element(By.NAME, "qdRate").send_keys("1")
driver.find_element(By.NAME, "qdCeil").send_keys(100)
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='p-checkbox-box']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(),'Değişiklikleri Kaydet')]").click()

