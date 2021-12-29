Feature: Amazon purchasing Test
#As a new Amazon user, I want to search for the cheapest Snickers and Skittles on the page.
#Add the cheapest ones to your Basket and check if the basket calculates the result correctly
#Check if on Checkout, without an account, the user gets redirected to the registration page.

  Scenario: 001-Not authorized user adds to basket the cheapest 2 items and click Buy button
    # Launch browser and open Amazon website
    Given I start the browser
    When I open 'https://www.amazon.com' site in the browser
    Then I see the main page is open

    # Search Skittles
    When I type in the Search field 'Skittles' and click the Search button on the main Amazon page
    Then I see the results of the search
    # sort results by Price: Low to High
    When I choose 'Price: Low to High' in 'Sort by' DropDown on the main Amazon page
    # choose the first item that is available and can be added to the cart
    And I click on the first item in the search result that available to buy
    Then I see that item is opened on a new page
    # get all offers
    When I click on 'See All Buying Options' button
    Then I see that All Offers Dialog is displayed
    # select the cheapest one
    When I choose the cheapest offer and click 'Add to Cart' button
    And I close All Offers Dialog

    # search and add Snickers to the basket
    When I clear the Search field on the main Amazon page
    And I type in the Search field 'Snickers' and click the Search button on the main Amazon page
    Then I see the results of the search
    When I choose 'Price: Low to High' in 'Sort by' DropDown on the main Amazon page
    And I click on the first item in the search result that available to buy
    Then I see that item is opened on a new page
    When I click on 'See All Buying Options' button
    Then I see that All Offers Dialog is displayed
    When I choose the cheapest offer and click 'Add to Cart' button
    When I close All Offers Dialog

    When I click on the basket on the Amazon page
    Then I see 'Shopping Cart' is opened on a new page
    And There are 2 items in the Shopping Cart
    And I see that sum of items is equal Subtotal field

    When I click to 'Proceed to checkout' on the Shopping Cart page
    Then I see the Login page is opened on a new page

    When I close the browser




