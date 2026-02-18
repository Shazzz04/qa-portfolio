from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()

try:
    # TC001: Login first 
    print("Login")
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # TC023: Click cart icon -> Cart page opens
    print("TC023: Cart Navigation Test")
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()

    # Verify cart page loaded - FIXED: "title" not "titile"
    cart_page_header = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
    header_text = cart_page_header.text

    assert "Your Cart" in header_text
    print("TC023 PASSED! Cart page loaded. Header:", header_text)

except Exception as e:
    print("TC023 FAILED:", str(e))

finally:
    time.sleep(3)
    driver.quit()
