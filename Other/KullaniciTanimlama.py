import time

from selenium import webdriver
# chrome driver
from selenium.webdriver.chrome.service import Service
# --chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

service_obj= Service("/Users/feskin/Desktop/document/chromedriver.exe");
driver: WebDriver = webdriver.Chrome(service=service_obj)

driver.get("http://10.1.112.103/#/pages/login")
driver.maximize_window()
#--find locators
driver.find_element(By.NAME,"username").send_keys("@dettaadmin")
driver.find_element(By.NAME, "password").send_keys("admin")

#//tagname[@attribute='value']  //input[@type='submit']
driver.find_element(By.XPATH, "(//button[contains(text(),'Oturum Açınız')])[1]").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "body > app-dashboard:nth-child(2) > div:nth-child(1) > div:nth-child(1) > nav:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(),'Kullanıcı Yönetimi')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(),'Yeni Kullanıcı Ekle')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='e.g. onur00']").send_keys("fabel4")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("faruk.eskin6@gmail.com")
driver.find_element(By.XPATH, "//input[@id='maxsessiontime']").send_keys("120")
driver.find_element(By.XPATH, "//input[@id='password_reenter']").send_keys("1000")
driver.find_element(By.XPATH, "//span[contains(text(),'Değişiklikleri Kaydet')]").click()
time.sleep(2)
driver.close()


