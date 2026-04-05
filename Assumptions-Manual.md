Assumptions
===========

While designing the test cases for this assignment, I made the following assumptions based on common e-commerce behavior:

- I assumed that the search functionality supports full and partial keyword matching, which is why I included test cases for both exact search ("iPhone") and partial search inputs.

- I assumed that the search feature is case-insensitive, so users can search using any combination of uppercase or lowercase letters.

- For invalid search inputs, I assumed the system should not return unrelated results and should instead display a "No results found" type message.

- For empty search input, I assumed the system may either show a validation message or display all products, depending on the implementation.

- I assumed that selecting a product from search results should open the product detail page correctly.

- I assumed that only in-stock products can be added to the cart, and out-of-stock products should show an appropriate message.

- I assumed that if a product has required options (such as size or color), the system should not allow adding it to the cart without selecting those options.

- I assumed that adding the same product multiple times should update the quantity in the cart instead of creating duplicate entries.

- I assumed that once a product is added to the cart, it should be visible on the cart page and counted correctly.

- Since this is a limited-scope assignment, I focused only on search and add-to-cart functionality and did not consider checkout or payment flows.
