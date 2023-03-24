from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Chrome ayarları
options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--test-type")
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")
options.add_argument("--headless")  # Arka planda çalıştırmak için kullanılır

# Web sürücüsünü başlat
driver = webdriver.Chrome(options=options)
# Hepsiburada web sitesine git
driver.get("https://www.hepsiburada.com/")

# Ana sayfada yer alan arama kutusuna "Girişimci Kadın Ürünleri" kelimesi girilir
search_box = driver.find_element_by_name("k")
search_box.send_keys("Girişimci Kadın Ürünleri")
search_box.send_keys(Keys.RETURN)

# Sayfanın yüklenmesini bekle
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.page-title")))

# "Çok Satanlar" butonuna tıklanır
sort_button = driver.find_element_by_css_selector("button[data-bind='click: selectSort, css: sortCssClass']")
sort_button.click()

best_sellers_option = driver.find_element_by_xpath("//ul[@class='sorting-select-list']/li[2]")
best_sellers_option.click()

# Sayfanın yüklenmesini bekle
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.search-result-container")))

# 1000 TL üstündeki ilk ürüne tıklanır
price_limit = 1000

while True:
    products = driver.find_elements_by_css_selector("li.search-item")
    for product in products:
        product_price = product.find_element_by_css_selector("div.price-value").text
        product_price = int(''.join(filter(str.isdigit, product_price)))
        if product_price > price_limit:
            # İlgili ürüne tıkla
            ActionChains(driver).move_to_element(product).click().perform()
            break
    else:
        # Sayfada başka ürün yoksa veya 1000 TL üstündeki hiçbir ürün yoksa hata ver ve çık
        print("1000 TL üstünde ürün bulunamadı.")
        driver.quit()
        break

    # Ürün sepete eklenir
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.buttons > button.add-to-basket-button")))
        add_to_cart_button = driver.find_element_by_css_selector("div.buttons > button.add-to-basket-button")
        add_to_cart_button.click()
        print("Ürün sepete eklendi.")
    except NoSuchElementException:
        print("Ürün sepete eklenemedi.")

# Sepete gidilir
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.my-basket"))).click()

# Ürün sepetten çıkartılır ve sepetin boş olduğu doğrulanır
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.remove-item"))).click()
try:
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.hb-toast-text"), "Sepetinizde ürün bulunmamaktadır."))
    print("Sepet boşaltıldı.")
except TimeoutException:
    print("Sepet boşaltılamadı.")