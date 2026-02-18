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

    # TC005: Add Sauce Backback to cart
    print("TC005: Add to Cart Test")
    add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    add_to_cart_btn.click()

    # Verify cart badge shows "1" 
    cart_badge = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    badge_text = cart_badge.text  

    assert badge_text == "1"
    print("TC005 PASSED! Cart badge shows:", badge_text)

except Exception as e:
    print("TC005 FAILED:", str(e))

finally:
    time.sleep(3)
    driver.quit()
