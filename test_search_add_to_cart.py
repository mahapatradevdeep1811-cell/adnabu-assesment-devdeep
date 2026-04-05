from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Launch browser
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


# Open store and enter password
def open_store(driver):
    driver.get("https://adnabu-store-assignment1.myshopify.com")

    wait = WebDriverWait(driver, 10)

    # Wait for password field and enter password
    password_input = wait.until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_input.send_keys("AdNabuQA")

    # Click enter
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Logged into store")


# Search for product
def search_product(driver, product_name):
    wait = WebDriverWait(driver, 10)

    # Open search bar
    search_icon = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//summary[contains(@aria-label,'Search')]"))
    )
    search_icon.click()

    # Enter product name
    search_input = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_input.send_keys(product_name)
    search_input.send_keys(Keys.ENTER)

    print(f"Searched for: {product_name}")


# Select first product
def select_product(driver):
    wait = WebDriverWait(driver, 10)

    product = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/products')]"))
    )
    product.click()

    print("Opened first product from results")


# Add product to cart
def add_to_cart(driver):
    wait = WebDriverWait(driver, 10)

    add_button = wait.until(
        EC.element_to_be_clickable((By.NAME, "add"))
    )
    add_button.click()

    print("Clicked on Add to Cart")


# Verify cart
def verify_cart(driver):
    wait = WebDriverWait(driver, 10)

    cart_icon = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/cart')]"))
    )
    cart_icon.click()

    cart_items = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'cart-item')]"))
    )

    if len(cart_items) > 0:
        print("Product is present in cart")
    else:
        raise Exception("Cart is empty")


# Main test flow
def main():
    driver = setup_driver()

    try:
        open_store(driver)
        search_product(driver, "iPhone")
        select_product(driver)
        add_to_cart(driver)
        verify_cart(driver)

        print("Test completed successfully")

        # OPTIONAL: Take screenshot after success
        driver.save_screenshot("success.png")

    except Exception as e:
        print("Test failed:", e)

        # OPTIONAL: Capture screenshot on failure
        driver.save_screenshot("failure.png")

    finally:
        driver.quit()
        print("Browser closed")


if __name__ == "__main__":
    main()
