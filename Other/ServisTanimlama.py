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
driver.find_element(By.XPATH, "//a[contains(text(),'Servis İzinleri')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Yeni Servis Ekle']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Seçim yapınız yada servis ismini giriniz.']").send_keys("deneme")
driver.find_element(By.XPATH, "//input[@id='serviceDesc']").send_keys("yok")
time.sleep(2)
#Veri tipi seçme combo box'ı
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-servicedefinition[@class='ng-star-inserted']/p-dialog/div/div[@role='dialog']//form/div//p-dropdown[@name='serviceQdTypes']//div[@role='button']/span").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[@aria-label='Veri']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//p-dropdown[@id='bandwidth']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(),'Düşük')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-servicedefinition[@class='ng-star-inserted']/p-dialog/div/div[@role='dialog']//form/div//div[@class='row']/div[5]/div[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Yüksek']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-servicedefinition[@class='ng-star-inserted']/p-dialog/div/div[@role='dialog']//form/div//p-dropdown[@name='errorLimitValue']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Normal']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-servicedefinition[@class='ng-star-inserted']/p-dialog/div/div[@role='dialog']//form/div//p-dropdown[@name='protocol']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='ICMP']").click()
driver.find_element(By.NAME, "ipWithSubnetSource").send_keys("17230.106.5/24")
time.sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(),'Değişiklikleri Kaydet')]").click()












