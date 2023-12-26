from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Use WebDriverManager to automatically download and manage ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Test 1: Perform a search on Google
driver.get('https://www.google.com')
search_box = driver.find_element('name', 'q')
search_box.send_keys('Selenium testing with Python')
search_box.send_keys(Keys.RETURN)

# Wait for the results page to load
driver.implicitly_wait(5)

# Test 2: Click on the first search result
search_results = driver.find_elements(By.CSS_SELECTOR, '.tF2Cxc')
if search_results:
    first_result = search_results[0]
    first_result.click()

    # Wait for the page to load
    time.sleep(3)

    # Test 3: Go back to the search results page
    driver.back()

# Wait for the page to load
    time.sleep(3)

# Re-fetch the search results
    search_results = driver.find_elements(By.CSS_SELECTOR, '.tF2Cxc')

# Test 4: Check if the search results contain the term "Python"
    contains_python = any('Python' in result.text for result in search_results)

# Print test results
    print('Test 1: Search on Google - Passed')
    print('Test 2: Click on the first result - Passed')
    print('Test 3: Go back to search results - Passed')
    print(f'Test 4: Search results contain "Python" - {"Passed" if contains_python else "Failed"}')

else:
    print('No search results found.')

# Close the browser window
driver.quit() 

