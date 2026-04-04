Test Cases – AdNabuTestStore
============================

Precondition (Applicable for all test cases)
-------------------------------------------
1. Open browser  
2. Navigate to: https://adnabu-store-assignment1.myshopify.com  
3. Enter store password: AdNabuQA  
4. Click "Enter" to access the store  

==================================================

(A) Product Search
--------------

TC_01: Search with a valid keyword (Positive)
--------------------------------------------
Priority: High  
Severity: Critical  
Test Data: "iPhone"  

Steps:
1. Access the store using the precondition steps  
2. Enter "iPhone" in the search bar  
3. Click on the search button  

Expected Result:
- Relevant products are displayed  
- Results match the searched keyword  

--------------------------------------------------

TC_02: Search using partial keyword (Positive)
---------------------------------------------
Priority: Medium  
Severity: Major  
Test Data: "iPh"  

Steps:
1. Access the store using the precondition steps  
2. Enter "iPh" in the search bar  
3. Click on the search button  

Expected Result:
- Matching products are displayed  
- Search works with partial input  

--------------------------------------------------

TC_03: Search with different case input (Positive)
-------------------------------------------------
Priority: Low  
Severity: Minor  
Test Data: "iphone"  

Steps:
1. Access the store using the precondition steps  
2. Enter keyword in lowercase  
3. Click on the search button  

Expected Result:
- Search is case-insensitive  
- Correct results are displayed  

--------------------------------------------------

TC_04: Search with invalid keyword (Negative)
--------------------------------------------
Priority: Medium  
Severity: Major  
Test Data: "xyz123ABC!@#$"  

Steps:
1. Access the store using the precondition steps  
2. Enter invalid keyword  
3. Click on the search button  

Expected Result:
- "No results found" message is displayed  
- No unrelated products appear  

--------------------------------------------------

TC_05: Search with empty input (Edge Case)
-----------------------------------------
Priority: Medium  
Severity: Minor  
Test Data: Empty input  

Steps:
1. Access the store using the precondition steps  
2. Leave the search bar empty  
3. Click on the search button  

Expected Result:
- Validation message is shown OR all products are displayed  
- Application remains stable  

==================================================

(B) Add to Cart
-----------

TC_01: Add an in-stock product to cart (Positive)
------------------------------------------------
Priority: High  
Severity: Critical  
Test Data: Product searched using "iPhone"  

Steps:
1. Access the store using the precondition steps  
2. Search for "iPhone"  
3. Open any available product from results  
4. Click on "Add to Cart"  

Expected Result:
- Product is added successfully  
- Cart count is updated  
- Product appears in the cart  

--------------------------------------------------

TC_02: Add multiple different products (Positive)
------------------------------------------------
Priority: Medium  
Severity: Major  
Test Data: Product from "iPhone" search + another product  

Steps:
1. Access the store using the precondition steps  
2. Add a product from "iPhone" results  
3. Add another product to cart  

Expected Result:
- Both products are added  
- Cart reflects correct items and count  

--------------------------------------------------

TC_03: Add out-of-stock product (Negative)
-----------------------------------------
Priority: High  
Severity: Major  
Test Data: Any out-of-stock product  

Steps:
1. Access the store using the precondition steps  
2. Open an out-of-stock product  
3. Click on "Add to Cart"  

Expected Result:
- Error message is displayed  
- Product is not added to cart  

--------------------------------------------------

TC_04: Add to cart without selecting required options (Negative)
---------------------------------------------------------------
Priority: Medium  
Severity: Major  
Test Data: Product with size/color options  

Steps:
1. Access the store using the precondition steps  
2. Open product with required options  
3. Do not select any option  
4. Click on "Add to Cart"  

Expected Result:
- Validation message is displayed  
- Product is not added  

--------------------------------------------------

TC_05: Add same product multiple times (Edge Case)
-------------------------------------------------
Priority: Medium  
Severity: Major  
Test Data: Same product added repeatedly  

Steps:
1. Access the store using the precondition steps  
2. Click "Add to Cart" multiple times  

Expected Result:
- Quantity updates correctly  
- No duplicate entries are created  

