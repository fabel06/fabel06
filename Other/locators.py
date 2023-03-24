from select import select
from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service

# --chrome
from selenium.webdriver.common.by import By

service_obj= Service("/Users/feskin/Desktop/document/chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#ID ,Xpath, CSSSelector, Classname, name, linkText(bulunan elementin uniqe olması önemli)
driver.find_element(By.NAME, "email").send_keys("faruk.eskin6@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# CSS tagname[attribute='value'] --> input[type='submit'], #id, .classname

# XPATH //tagname[@attribute='value']  //input[@type='submit']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Faruk")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1" ).click()

#static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
#dropdown.select_by_value()

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hellosgain")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

