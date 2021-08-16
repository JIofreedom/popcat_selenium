from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://popcat.click/")
driver.implicitly_wait(5)
cat = driver.find_element_by_id("app")

while True:
    cat.click()