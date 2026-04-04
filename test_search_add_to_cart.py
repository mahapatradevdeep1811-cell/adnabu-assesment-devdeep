from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Function to launch browser and maximize window
def setup_driver():
    driver = webdriver.Chrome()  # Launch Chrome browser
    driver.maximize_window()     # Maximize window for better visibility
    return driver


# Function to open website and enter store password
def open_store(driver):
    driver.get("https://adnabu-store-assignment1.myshopify.com")

    wait = WebDriverWait(driver, 10)

    # Wait until password input field is visible
    password_input = wait.until(
        EC.presence_of_element_located((By.ID, "password"))
    )

    # Enter store password
    password_input.send_keys("AdNabuQA")

    # Click on enter button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()


# Function to search for a product
def search_product(driver, product_name):
    wait = WebDriverWait(driver, 10)

    # Click on search icon
    search_icon = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//summary[contains(@aria-label,'Search')]"))
    )
    search_icon.click()

    # Wait for search input field and enter product name
    search_input = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_input.send_keys(product_name)

    # Press Enter to search
    search_input.send_keys(Keys.ENTER)


# Function to select first product from search results
def select_product(driver):
    wait = WebDriverWait(driver, 10)

    # Click on first available product
    product = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/products')]"))
    )
    product.click()


# Function to add product to cart
def add_to_cart(driver):
    wait = WebDriverWait(driver, 10)

    # Click on "Add to Cart" button
    add_button = wait.until(
        EC.element_to_be_clickable((By.NAME, "add"))
    )
    add_button.click()


# Function to verify product is added to cart
def verify_cart(driver):
    wait = WebDriverWait(driver, 10)

    # Click on cart icon
    cart_icon = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/cart')]"))
    )
    cart_icon.click()

    # Check if at least one item is present in cart
    cart_items = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'cart-item')]"))
    )

    # Simple validation
    if len(cart_items) > 0:
        print("Product is present in cart")
    else:
        print("Cart is empty")


# Main function to run the test
def main():
    driver = setup_driver()

    try:
        open_store(driver)                  # Open site and login
        search_product(driver, "iPhone")    # Search for product
        select_product(driver)              # Open product
        add_to_cart(driver)                 # Add to cart
        verify_cart(driver)                 # Verify cart

        print("Test Passed")

    except Exception as e:
        print("Test Failed:", e)

    finally:
        driver.quit()  # Close browser


# Run the script
if __name__ == "__main__":
    main()
