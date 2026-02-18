from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Setup Chrome
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()

try:
    # TC001: Valid Login
    print("🧪 TC001: Valid Login Test")
    driver.get("https://www.saucedemo.com/")
    
    # Enter credentials
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")
    
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_btn.click()
    
    # Verify products page loaded
    products_header = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
    header_text = products_header.text
    
    assert "Products" in header_text
    print("✅ TC001 PASSED! Login successful. Header:", header_text)
    
except Exception as e:
    print("❌ TC001 FAILED:", str(e))
    
finally:
    time.sleep(3)
    driver.quit()

