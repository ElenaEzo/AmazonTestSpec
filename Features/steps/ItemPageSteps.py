from behave import *
from Features.steps.PageObjects.ItemPageObject import *


@then("I see that item is opened on a new page")
def i_see_item_is_opened(context):
    assert ItemPageObject(context).item_name.is_displayed() is True


@when("I click on 'See All Buying Options' button")
def i_click_button(context):
    ItemPageObject(context).see_option_button.click()
