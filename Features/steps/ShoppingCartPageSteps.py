from behave import *
from Features.steps.PageObjects.ShoppingCartPageObject import *


@then("I see '{title}' is opened on a new page")
def i_see_shopping_card_page(context, title):
    shopping_page = ShoppingCartPageObject(context)
    assert shopping_page.page_header.is_displayed() is True
    assert shopping_page.page_header.text == title


@then("There are {items_number} items in the Shopping Cart")
def there_are_items(context, items_number):
    shopping_page = ShoppingCartPageObject(context)
    assert len(shopping_page.items_list) == int(items_number)


@then("I see that sum of items is equal Subtotal field")
def i_check_sum_with_subtotal(context):
    shopping_page = ShoppingCartPageObject(context)
    assert shopping_page.get_sum_of_items() == shopping_page.get_subtotal()


@when("I click to 'Proceed to checkout' on the Shopping Cart page")
def i_click_to_proceed_to_checkout(context):
    ShoppingCartPageObject(context).proceed_button.click()
