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

driver.get("http://10.1.112.108/#/pages/login")
driver.maximize_window()
#--find locators
driver.find_element(By.NAME,"username").send_keys("@admin")
driver.find_element(By.NAME, "password").send_keys("admin")

#//tagname[@attribute='value']  //input[@type='submit']
driver.find_element(By.XPATH, "(//button[contains(text(),'Oturum Açınız')])[1]").click()
time.sleep(1)
#Tanımlamalar menüsüne tıkla
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']/div[@class='app-body']/div[@class='sidebar']/nav[@class='sidebar-nav']/ul[@class='nav']/li[8]/a[1]").click()
time.sleep(1)
#İLETİŞİM KANALI ALT MENÜSÜNE TIKLANILIR
driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(8) > .nav-dropdown-items > li:nth-of-type(3) > .nav-link.ng-star-inserted").click()
time.sleep(2)
#Sil Butonuna Tıklanılır
driver.find_element(By.XPATH, "").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/div[2]/p-table[@class='commSettingDT']//table[@role='grid']/tbody/tr[1]/td[7]/div[@class='ng-star-inserted']/button[@type='button']/span[1]").click()
driver.close()