from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service

# --chrome
from selenium.webdriver.common.by import By

service_obj= Service("/Users/feskin/Desktop/document/chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT ,"Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "//form/div[2]/input").send_keys("1406Ruse")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("1406Ruse")
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()


## Buraya tekrardan bakılacak..