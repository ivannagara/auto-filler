from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

# Configure Chrome options to spoof User-Agent
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

def login(driver, username, password):
    # Wait for the login form to load
    time.sleep(2)
    
    # Enter the username and password
    username_field = driver.find_element(By.NAME, 'loginKey')
    password_field = driver.find_element(By.NAME, 'password')
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    # Click the login button
    login_button = driver.find_element(By.XPATH, '//button[contains(text(), "登入")]')
    login_button.click()
    
    # Wait for the login to complete
    time.sleep(5)

# Load the Shopee product page
shopee_url = 'https://shopee.tw/The-North-Face%E5%8C%97%E9%9D%A2%E7%94%B7%E5%A5%B3%E6%AC%BE%E9%BB%91%E8%89%B2%E4%BE%BF%E6%8D%B7%E8%88%92%E9%81%A9%E4%BC%91%E9%96%92%E5%BE%8C%E8%83%8C%E5%8C%85%EF%BD%9C52TBKX7-i.854257746.20846317774?sp_atk=e0e114a6-3ee8-4d05-8946-782b001c560d&xptdk=e0e114a6-3ee8-4d05-8946-782b001c560d'
driver.get(shopee_url)

# Monitor the URL
initial_url = driver.current_url

# Your Shopee login credentials
username = "your_username"  # Replace with your Shopee username
password = "your_password"  # Replace with your Shopee password

while True:
    current_url = driver.current_url
    if "login" in current_url:
        print(f"URL changed to login page: {current_url}")
        login(driver, username, password)
        initial_url = driver.current_url  # Update the initial URL after login
    elif current_url == shopee_url:
        # Extract HTML content
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # Extract product details using consistent classes
        product_name_div = soup.find('div', {'class': 'attM6y'})
        price_div = soup.find('div', {'class': 'pmmxKx'})
        description_div = soup.find('div', {'class': 'OitLRu'})
        image_tag = soup.find('img', {'class': 'Yd3WfG'})

        # Check if elements exist and extract text
        product_name = product_name_div.text if product_name_div else "Product Name Not Found"
        price = price_div.text if price_div else "Price Not Found"
        description = description_div.text if description_div else "Description Not Found"
        image_url = image_tag['src'] if image_tag else "Image Not Found"

        print("Product Name:", product_name)
        print("Price:", price)
        print("Description:", description)
        print("Image URL:", image_url)

        break  # Exit the loop once the product details are extracted
    else:
        print(f"URL unchanged or redirected to a different page: {current_url}")
    
    # Sleep for a short duration before checking again
    time.sleep(2)

# Open the Google Form
google_form_url = 'https://docs.google.com/forms/d/e/your_form_id/viewform'
driver.get(google_form_url)

# Fill the form fields
time.sleep(2)  # Wait for the page to load

# Fill the Product Name field
product_name_field = driver.find_element(By.XPATH, '//input[@aria-label="Product Name"]')
product_name_field.send_keys(product_name)

# Fill the Price field
price_field = driver.find_element(By.XPATH, '//input[@aria-label="Price"]')
price_field.send_keys(price)

# Fill the Description field
description_field = driver.find_element(By.XPATH, '//textarea[@aria-label="Description"]')
description_field.send_keys(description)

# Optionally handle image upload if the form supports it
# Submit the form
submit_button = driver.find_element(By.XPATH, '//div[@role="button" and @aria-label="Submit"]')
submit_button.click()

# Close the browser
time.sleep(2)  # Wait for the form to be submitted
driver.quit()

print("Form submitted successfully.")
