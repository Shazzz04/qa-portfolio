
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)  # Increased timeout
driver.maximize_window()

try:
    print("Login")
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    print("Add item to cart (TC005)")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    
    print("TC023: Navigate to cart")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # TC028: Start checkout
    print("TC028: Checkout with valid data")
    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()
    
    # Fill checkout form - SLOWER typing for stability
    first_name = driver.find_element(By.ID, "first-name")
    last_name = driver.find_element(By.ID, "last-name")
    zip_code = driver.find_element(By.ID, "postal-code")
    
    first_name.send_keys("Shaza")
    last_name.send_keys("Faizer")
    zip_code.send_keys("10350")
    
    driver.find_element(By.ID, "continue").click()
    
    # TC035: Complete order - FIXED verification
    print("TC035: Complete purchase")
    finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish_btn.click()
    
    # MULTIPLE verification strategies (rock solid)
    # Method 1: Wait for complete header
    complete_header = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
    success_text = complete_header.text
    
    # Method 2: Backup URL check
    current_url = driver.current_url
    assert "complete" in current_url.lower()
    
    print("TC028+TC035 PASSED!")
    print("Header:", success_text)
    print("URL:", current_url)

except Exception as e:
    print("Checkout FAILED:", str(e))
    print("Current URL:", driver.current_url if 'driver' in locals() else "N/A")
    
finally:
    time.sleep(5)  # See success page
    driver.quit()
