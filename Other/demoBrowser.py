from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service

# --chrome
service_obj= Service("/Users/feskin/Desktop/document/chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)

# --Firefox
#service_obj= Service("/Users/feskin/Desktop/document/geckodriver.exe");
#driver = webdriver.Firefox(service=service_obj)

# --IE edge
#service_obj= Service("/Users/feskin/Desktop/document/msedgedriver.exe");
#driver = webdriver.Edge(service=service_obj)

driver.maximize_window()
driver.get("https://www.elazig.bel.tr/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.firat.edu.tr/tr")
driver.minimize_window()
driver.back()
driver.forward()
driver.close()

