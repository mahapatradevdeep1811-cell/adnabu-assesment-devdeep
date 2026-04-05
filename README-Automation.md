# Automation Test – AdNabu Assignment

## Overview

For this assignment, I automated a simple user flow on the AdNabu test store.

The idea was to replicate what a normal user would do:
search for a product and add it to the cart.

## What I automated

* Open the website
* Enter the store password
* Search for a product (I used "iPhone" as an example)
* Open a product from the results
* Add the product to the cart
* Verify that the product is added

## How I approached it

I kept the script simple and focused on readability.

* Used functions for each step (search, add to cart, etc.)
* Used explicit waits to handle dynamic loading
* Avoided using time.sleep() to make the script more reliable

## Setup

1. Clone this repository:
   git clone <your-repo-link>

2. Navigate to the automation folder:
   cd automation

3. Install dependencies:
   pip install -r requirements.txt

## How to run

Run the script using:

python test_search_add_to_cart.py

## What to expect

If everything works fine:

* Product will be added to the cart
* Console will show:
  "Product is present in cart"
  "Test completed successfully"

If something fails:

* Error message will be printed
* A screenshot (failure.png) will be saved

## Notes

* I focused on keeping the solution simple rather than building a full framework
* Only one scenario is automated as per the assignment instructions
* The script can be extended later if needed

## Author

Devdeep Mahapatra
