import time

from selenium import webdriver
# chrome driver
from selenium.webdriver.chrome.service import Service
# --chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

service_obj = Service("/Users/feskin/Desktop/document/chromedriver.exe");
driver: WebDriver = webdriver.Chrome(service=service_obj)

driver.get("http://10.1.112.114/#/pages/login")
driver.maximize_window()
# Find locators
driver.find_element(By.NAME, "username").send_keys("@dettaadmin")
driver.find_element(By.NAME, "password").send_keys("admin")

# //tagname[@attribute='value']  //input[@type='submit']
driver.find_element(By.XPATH, "(//button[contains(text(),'Oturum Açınız')])[1]").click()
time.sleep(3)
#Sistem Yönetimi Menüsüne Tıklanılır
driver.find_element(By.XPATH,"//app-dashboard[@class='ng-star-inserted']//nav[@class='sidebar-nav']/ul[@class='nav']/li[14]/a[@id='dropdownMenu']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[normalize-space()='Harita Yönetimi']").click()
time.sleep(1)
# 1.Yeni Unsur Ekleme
driver.find_element(By.XPATH, "//span[normalize-space()='Yeni Unsur Ekle']").click()
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("goksu")
driver.find_element(By.XPATH, "//input[@name='ipAddress']").send_keys("17216.1.1")
driver.find_element(By.XPATH, "//input[@name='latitude']").send_keys("39.53")
driver.find_element(By.XPATH, "//input[@name='longitude']").send_keys("32.23")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,
                    "div[role='dialog'] p-footer > .p-button.p-button-success.p-component > .p-button-label").click()
time.sleep(3)
# 2.Yeni Unsur Ekleme
driver.find_element(By.XPATH, "//span[normalize-space()='Yeni Unsur Ekle']").click()
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("gokova")
driver.find_element(By.XPATH, "//input[@name='ipAddress']").send_keys("17216.18.1")
driver.find_element(By.XPATH, "//input[@name='latitude']").send_keys("39.53")
driver.find_element(By.XPATH, "//input[@name='longitude']").send_keys("32.23")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,
                    "div[role='dialog'] p-footer > .p-button.p-button-success.p-component > .p-button-label").click()
time.sleep(3)
# 3.Yeni Unsur Ekleme
driver.find_element(By.XPATH, "//span[normalize-space()='Yeni Unsur Ekle']").click()
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("heybeliada")
driver.find_element(By.XPATH, "//input[@name='ipAddress']").send_keys("17218.1.1")
driver.find_element(By.XPATH, "//input[@name='latitude']").send_keys("39.53")
driver.find_element(By.XPATH, "//input[@name='longitude']").send_keys("32.23")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,
                    "div[role='dialog'] p-footer > .p-button.p-button-success.p-component > .p-button-label").click()
time.sleep(3)
# 4.Yeni Unsur Ekleme
driver.find_element(By.XPATH, "//span[normalize-space()='Yeni Unsur Ekle']").click()
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("buyukada")
driver.find_element(By.XPATH, "//input[@name='ipAddress']").send_keys("17219.1.1")
driver.find_element(By.XPATH, "//input[@name='latitude']").send_keys("39.53")
driver.find_element(By.XPATH, "//input[@name='longitude']").send_keys("32.23")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,
                    "div[role='dialog'] p-footer > .p-button.p-button-success.p-component > .p-button-label").click()
time.sleep(3)
# 5.Yeni Unsur Ekleme
driver.find_element(By.XPATH, "//span[normalize-space()='Yeni Unsur Ekle']").click()
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("aksaz")
driver.find_element(By.XPATH, "//input[@name='ipAddress']").send_keys("17227.1.1")
driver.find_element(By.XPATH, "//input[@name='latitude']").send_keys("39.53")
driver.find_element(By.XPATH, "//input[@name='longitude']").send_keys("32.23")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,
                    "div[role='dialog'] p-footer > .p-button.p-button-success.p-component > .p-button-label").click()
time.sleep(3)
# 6.Yeni Unsur Ekleme
driver.find_element(By.XPATH, "//span[normalize-space()='Yeni Unsur Ekle']").click()
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("gkm")
driver.find_element(By.XPATH, "//input[@name='ipAddress']").send_keys("17228.1.1")
driver.find_element(By.XPATH, "//input[@name='latitude']").send_keys("39.53")
driver.find_element(By.XPATH, "//input[@name='longitude']").send_keys("32.23")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,
                    "div[role='dialog'] p-footer > .p-button.p-button-success.p-component > .p-button-label").click()
time.sleep(3)
driver.close()
