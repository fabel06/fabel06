Class DemoDropdownSingleSelect():

def demo_droppdown(self)
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("http://10.1.115.157/#/definitions/service")
    dropdown = driver.find_element(By.CSS_SELECTOR,".ng-tns-c62-122.p-dropdown-label.p-inputtext.p-placeholder.ng-star-inserted")
    dd = Select(dropdown)
    dd.select_by_index(0)
    time.sleep(3)

    dd.select_by_visible_text("Mesaj")
    time.sleep(3)

    dd.select_by_value("Ses")
    time.sleep(3)


dddemo = DemoDropdownSingleSelect()
dddemo.demo_dropdown()

#dropdown = Select(driver.find_element(By.XPATH, "//span[@class='ng-tns-c62-274 p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
#dropdown.select_by_index(0)
#dropdown.select_by_visible_text("Veri")
#driver.find_element(By.XPATH, "//span[@class='p-dropdown-trigger-icon ng-tns-c62-11 pi pi-chevron-down']").click()
#driver.find_element(By.XPATH, "//li[@aria-label='Veri']").click()