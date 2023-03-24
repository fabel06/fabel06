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

driver.get("http://10.1.112.103/#/pages/login")
driver.maximize_window()
#--find locatorswat
driver.find_element(By.NAME,"username").send_keys("@dettaadmin")
driver.find_element(By.NAME, "password").send_keys("admin")

#//tagname[@attribute='value']  //input[@type='submit']
driver.find_element(By.XPATH, "(//button[contains(text(),'Oturum Açınız')])[1]").click()
time.sleep(1)
#Tanımlamalar menüsüne tıkla
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']/div[@class='app-body']/div[@class='sidebar']/nav[@class='sidebar-nav']/ul[@class='nav']/li[8]/a[1]").click()
time.sleep(1)
#İLETİŞİM KANALI ALT MENÜSÜNE TIKLANILIR
driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(8) > .nav-dropdown-items > li:nth-of-type(3) > .nav-link.ng-star-inserted").click()
time.sleep(1)
#Yeni Kanal Ekle butonuna tıklanılır
driver.find_element(By.XPATH, "//span[@class='p-button-icon p-button-icon-left fa fa-plus']").click()
time.sleep(1)
#1.İLETİŞİM KANALI EKLEME
driver.find_element(By.NAME, "channelName").send_keys("hf1")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div/div[1]//p-dropdown[@name='channelType']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='HF']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[1]/div[1]//p-dropdown[@name='deviceSwitch']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").click()
driver.find_element(By.XPATH, "//input[@name='description']").send_keys("Yok")
driver.find_element(By.XPATH, "//input[@name='channelIp']").send_keys("17220.1.2/24")
driver.find_element(By.XPATH, "//input[@name='swPort']").send_keys("5")
time.sleep(2)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Normal']").click()
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[2]/div//p-dropdown[@name='s5066SelectedNc']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='nchf1']").click()
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[2]/div//p-dropdown[@name='s5066SelectedSdm']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='sdmhf1']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[2]/div//p-dropdown[@name='s5066SelectedRadioHf']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='telsizhf1']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(),'Değişiklikleri Kaydet')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Evet']").click()
time.sleep(2)

#2.İLETİŞİM KANALI EKLEME
#Yeni Kanal Ekle butonuna tıklanılır
driver.find_element(By.XPATH, "//span[@class='p-button-icon p-button-icon-left fa fa-plus']").click()
time.sleep(1)
driver.find_element(By.NAME, "channelName").send_keys("hf2")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div/div[1]//p-dropdown[@name='channelType']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='HF']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[1]/div[1]//p-dropdown[@name='deviceSwitch']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").click()
driver.find_element(By.XPATH, "//input[@name='description']").send_keys("Yok")
driver.find_element(By.XPATH, "//input[@name='channelIp']").send_keys("17220.2.2/24")
driver.find_element(By.XPATH, "//input[@name='swPort']").send_keys("7")
time.sleep(2)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Normal']").click()
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[2]/div//p-dropdown[@name='s5066SelectedNc']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='nchf2']").click()
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[2]/div//p-dropdown[@name='s5066SelectedSdm']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='sdmhf2']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[2]/div//p-dropdown[@name='s5066SelectedRadioHf']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='telsizhf2']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(),'Değişiklikleri Kaydet')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Evet']").click()
time.sleep(3)
#3.İLETİŞİM KANALI EKLEME
#Yeni Kanal Ekle butonuna tıklanılır
driver.find_element(By.XPATH, "//span[@class='p-button-icon p-button-icon-left fa fa-plus']").click()
time.sleep(1)
driver.find_element(By.NAME, "channelName").send_keys("hf3")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div/div[1]//p-dropdown[@name='channelType']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='HF']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[1]/div[1]//p-dropdown[@name='deviceSwitch']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").click()
driver.find_element(By.XPATH, "//input[@name='description']").send_keys("Yok")
driver.find_element(By.XPATH, "//input[@name='channelIp']").send_keys("17220.3.2/24")
driver.find_element(By.XPATH, "//input[@name='swPort']").send_keys("9")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Normal']").click()
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[2]/div//p-dropdown[@name='s5066SelectedNc']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='nchf3']").click()
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[2]/div//p-dropdown[@name='s5066SelectedSdm']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='sdmhf3']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[2]/div//p-dropdown[@name='s5066SelectedRadioHf']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='telsizhf3']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(),'Değişiklikleri Kaydet')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Evet']").click()
time.sleep(3)
#4.İLETİŞİM KANALI EKLEME
#Yeni Kanal Ekle butonuna tıklanılır
driver.find_element(By.XPATH, "//span[@class='p-button-icon p-button-icon-left fa fa-plus']").click()
time.sleep(1)
driver.find_element(By.NAME, "channelName").send_keys("hf4")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div/div[1]//p-dropdown[@name='channelType']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='HF']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[1]/div[1]//p-dropdown[@name='deviceSwitch']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").click()
driver.find_element(By.XPATH, "//input[@name='description']").send_keys("Yok")
driver.find_element(By.XPATH, "//input[@name='channelIp']").send_keys("17220.4.2/24")
driver.find_element(By.XPATH, "//input[@name='swPort']").send_keys("11")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Normal']").click()
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[2]/div//p-dropdown[@name='s5066SelectedNc']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='nchf4']").click()
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[2]/div//p-dropdown[@name='s5066SelectedSdm']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='sdmhf4']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[2]/div//p-dropdown[@name='s5066SelectedRadioHf']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='telsizhf4']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(),'Değişiklikleri Kaydet')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Evet']").click()
time.sleep(3)
#5.İLETİŞİM KANALI EKLEME
#Yeni Kanal Ekle butonuna tıklanılır
driver.find_element(By.XPATH, "//span[@class='p-button-icon p-button-icon-left fa fa-plus']").click()
time.sleep(1)
driver.find_element(By.NAME, "channelName").send_keys("vuhf1")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div/div[1]//p-dropdown[@name='channelType']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='V/UHF']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[1]/div[1]//p-dropdown[@name='deviceSwitch']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").click()
driver.find_element(By.XPATH, "//input[@name='description']").send_keys("Yok")
driver.find_element(By.XPATH, "//input[@name='channelIp']").send_keys("17221.1.2/24")
driver.find_element(By.XPATH, "//input[@name='swPort']").send_keys("13")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Normal']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[3]/div//p-dropdown[@name='s4691SelectedNc']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='ncvuhf1']").click()
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[3]/div//p-dropdown[@name='s4691SelectedSdm']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='sdmvuhf1']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[3]/div//p-dropdown[@name='s4691SelectedRadioVuhf']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='telsizvuhf1']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(),'Değişiklikleri Kaydet')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Evet']").click()
time.sleep(3)
#6.İLETİŞİM KANALI EKLEME
#Yeni Kanal Ekle butonuna tıklanılır
driver.find_element(By.XPATH, "//span[@class='p-button-icon p-button-icon-left fa fa-plus']").click()
time.sleep(1)
driver.find_element(By.NAME, "channelName").send_keys("vuhf2")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div/div[1]//p-dropdown[@name='channelType']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='V/UHF']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[1]/div[1]//p-dropdown[@name='deviceSwitch']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").click()
driver.find_element(By.XPATH, "//input[@name='description']").send_keys("Yok")
driver.find_element(By.XPATH, "//input[@name='channelIp']").send_keys("17221.2.2/24")
driver.find_element(By.XPATH, "//input[@name='swPort']").send_keys("15")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Normal']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[3]/div//p-dropdown[@name='s4691SelectedNc']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='ncvuhf2']").click()
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[3]/div//p-dropdown[@name='s4691SelectedSdm']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='sdmvuhf2']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[3]/div//p-dropdown[@name='s4691SelectedRadioVuhf']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='telsizvuhf2']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(),'Değişiklikleri Kaydet')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Evet']").click()
time.sleep(3)
#7.İLETİŞİM KANALI EKLEME
#Yeni Kanal Ekle butonuna tıklanılır
driver.find_element(By.XPATH, "//span[@class='p-button-icon p-button-icon-left fa fa-plus']").click()
time.sleep(1)
driver.find_element(By.NAME, "channelName").send_keys("vuhf3")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div/div[1]//p-dropdown[@name='channelType']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='V/UHF']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[1]/div[1]//p-dropdown[@name='deviceSwitch']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").click()
driver.find_element(By.XPATH, "//input[@name='description']").send_keys("Yok")
driver.find_element(By.XPATH, "//input[@name='channelIp']").send_keys("17221.3.2/24")
driver.find_element(By.XPATH, "//input[@name='swPort']").send_keys("17")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Normal']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[3]/div//p-dropdown[@name='s4691SelectedNc']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='ncvuhf3']").click()
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[3]/div//p-dropdown[@name='s4691SelectedSdm']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='sdmvuhf3']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[3]/div//p-dropdown[@name='s4691SelectedRadioVuhf']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='telsizvuhf3']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(),'Değişiklikleri Kaydet')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Evet']").click()
time.sleep(3)
#8.İLETİŞİM KANALI EKLEME
#Yeni Kanal Ekle butonuna tıklanılır
driver.find_element(By.XPATH, "//span[@class='p-button-icon p-button-icon-left fa fa-plus']").click()
time.sleep(1)
driver.find_element(By.NAME, "channelName").send_keys("vuhf4")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div/div[1]//p-dropdown[@name='channelType']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='V/UHF']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[1]/div[1]//p-dropdown[@name='deviceSwitch']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").click()
driver.find_element(By.XPATH, "//input[@name='description']").send_keys("Yok")
driver.find_element(By.XPATH, "//input[@name='channelIp']").send_keys("17221.4.2/24")
driver.find_element(By.XPATH, "//input[@name='swPort']").send_keys("19")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Normal']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[3]/div//p-dropdown[@name='s4691SelectedNc']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='ncvuhf4']").click()
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[3]/div//p-dropdown[@name='s4691SelectedSdm']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='sdmvuhf4']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[3]/div//p-dropdown[@name='s4691SelectedRadioVuhf']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='telsizvuhf4']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(),'Değişiklikleri Kaydet')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Evet']").click()
time.sleep(3)
#9.İletişim kanalı Ekleme -KİM
#Yeni Kanal Ekle butonuna tıklanılır
driver.find_element(By.XPATH, "//span[@class='p-button-icon p-button-icon-left fa fa-plus']").click()
time.sleep(1)
driver.find_element(By.NAME, "channelName").send_keys("kim")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div/div[1]//p-dropdown[@name='channelType']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='KİM']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[1]/div[1]//p-dropdown[@name='deviceSwitch']//div[@role='button']/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").click()
driver.find_element(By.XPATH, "//input[@name='description']").send_keys("Yok")
driver.find_element(By.XPATH, "//input[@name='channelIp']").send_keys("17222.1.2/24")
driver.find_element(By.XPATH, "//input[@name='swPort']").send_keys("23")
time.sleep(1)
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]/div/div[@role='dialog']//form/div[1]/div[4]//p-multiselect[@name='errorLimitValue']//span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Normal']").click()
driver.find_element(By.XPATH, "//body/app-dashboard[@class='ng-star-inserted']//app-commlink[@class='ng-star-inserted']/p-dialog[1]//div[@role='dialog']//form/div[4]/div//p-dropdown[@name='kim']//span[.='Seçim Yapınız']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='KİM']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(),'Değişiklikleri Kaydet')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Evet']").click()
time.sleep(2)
driver.close()








