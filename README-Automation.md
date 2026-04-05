# Automation Test – Setup and Execution

## Overview

I automated a simple flow where a user searches for a product and adds it to the cart.
This section explains how to set up and run the script.

## Prerequisites

Before running the test, make sure you have:

* Python installed (version 3.0)
* Google Chrome browser
* ChromeDriver installed and added to your system PATH

## Setup Steps

1. Clone the repository:
   git clone <your-repo-link>

2. Go to the automation folder:
   cd automation

3. Install the required dependency:
   pip install -r requirements.txt

## How to Run the Test

Run the script using the following command:

python test_search_add_to_cart.py

## What Happens When You Run It

* The browser will open automatically
* It will navigate to the test website
* Enter the store password
* Search for a product (currently set to "iPhone")
* Open a product and add it to the cart
* Then it will check if the product is present in the cart

## Expected Output

If everything works correctly, you should see:

* "Product is present in cart"
* "Test completed successfully"

In case of failure:

* An error message will be printed in the console
* A screenshot (failure.png) will be saved for reference

## Notes

* I used explicit waits instead of fixed delays to make the script more stable
* The code is kept simple and easy to understand
* Only one scenario is automated as per the assignment requirement
