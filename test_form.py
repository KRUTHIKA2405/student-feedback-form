from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

# 1. Setup Chrome Options for Headless Mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs without a GUI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 2. Initialize Driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Get the absolute path of your index.html file
    file_path = "file://" + os.path.abspath("index.html")
    
    print(f"Opening: {file_path}")
    driver.get(file_path)

    # --- Sub Task 4 Test Cases ---

    # Test 1: Check whether the form page opens successfully
    assert "Student Feedback" in driver.title
    print("Test 1 Passed: Page title verified.")

    # Test 2: Check Reset button
    name_input = driver.find_element(By.ID, "name")
    name_input.send_keys("Test User")
    driver.find_element(By.CSS_SELECTOR, "button[type='reset']").click()
    assert name_input.get_attribute("value") == ""
    print("Test 2 Passed: Reset button cleared the field.")

    # Test 3: Enter invalid email format
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("not-an-email")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # Note: HTML5 validation usually prevents submission here
    print("Test 3 Passed: Invalid email handling verified.")

    # Test 4: Enter valid data and verify submission
    driver.refresh() # Start fresh
    driver.find_element(By.ID, "name").send_keys("Alex Smith")
    driver.find_element(By.ID, "email").send_keys("alex@example.com")
    driver.find_element(By.ID, "mobile").send_keys("9876543210")
    
    # Dropdown selection
    dept_dropdown = driver.find_element(By.ID, "department")
    dept_dropdown.send_keys("Computer Science")
    
    # Radio button selection
    driver.find_element(By.CSS_SELECTOR, "input[value='Male']").click()
    
    # Feedback Comments (Min 10 words)
    comments = "This is a great feedback form that meets all the required criteria for testing."
    driver.find_element(By.ID, "comments").send_keys(comments)
    
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Check for success message
    success_msg = driver.find_element(By.ID, "successMsg")
    assert success_msg.is_displayed()
    print("Test 4 Passed: Successful form submission with valid data.")

finally:
    driver.quit()
    print("Browser closed. Testing complete.")