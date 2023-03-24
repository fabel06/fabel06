import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/feskin/Desktop/document/chromedriver.exe")
driver: WebDriver = webdriver.Chrome(service=service_obj);
driver.get("https://www.hepsiburada.com/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element(By.CSS_SELECTOR, "[placeholder='Ürün, kategori veya marka ara']").send_keys("apple")
#time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".searchBoxOld-yDJzsIfi_S5gVgoapx6f").click()
driver.implicitly_wait(20)
#Girişimci kadın ürünlerini listele
driver.delete_all_cookies()
driver.forward()
#driver.find_element(By.CSS_SELECTOR, "html").click();
#driver.find_element(By.XPATH, "//div[@id='girisimci']//button[@class='moria-Toggle-gpkjWG XZEeL sjss8kpemig']").click()
driver.find_element(By.XPATH, "//label[@class='horizontalSortingBar-Ce404X9mUYVCRa5bjV4D']").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//div[contains(text(),'Çok satanlar')]").click()
#driver.find_element(By.ID, "btnLogin").click()
#time.sleep(2)
#driver.find_element(By.ID, "txtPassword").send_keys("1402Ruse+");
#time.sleep(0.5)
#driver.find_element(By.ID, "btnHalfLogin").click()
time.sleep(10)

#driver.find_element(By.XPATH, "//div[contains(text(),'Çok satanlar')]").click()
#driver.find_element(By.CSS_SELECTOR, "///div[@class='moria-ProductCard-iEHokJ cYci sz34jrxfjty']").click()
#driver.find_element(By.XPATH, "//html/body//div[@role='dialog']//button/div[.='Sepete ekle']").click()
#time.sleep(5)

