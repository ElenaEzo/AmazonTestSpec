from behave import *
from Features.steps.PageObjects.AmazonMainPageObject import *


@then("I see the main page is open")
def i_see_the_main_page(context):
    assert AmazonMainPageObject(context).title_element.is_displayed() is True


@when("I type in the Search field '{search_value}' and click the Search button on the main Amazon page")
def i_type_value_in_search_field(context, search_value):
    main_page = AmazonMainPageObject(context)
    main_page.search_field.send_keys(search_value)
    main_page.search_field.submit()


@then("I see the results of the search")
def i_see_the_results(context):
    assert AmazonMainPageObject(context).check_search_result_exists() is True


@when("I choose '{select_value}' in 'Sort by' DropDown on the main Amazon page")
def i_select_in_dropdown(context, select_value):
    AmazonMainPageObject(context).sort_by_value(select_value)


@when("I click on the first item in the search result that available to buy")
def i_click_first_on_element(context):
    AmazonMainPageObject(context).get_first_available_item().click()


@when("I clear the Search field on the main Amazon page")
def i_clear_search_field(context):
    AmazonMainPageObject(context).search_field.clear()


@when("I click on the basket on the Amazon page")
def i_click_the_basket(context):
    AmazonMainPageObject(context).basket.click()


@when("I click 'Sign In' link on the main Amazon page")
def i_click_sign_in_link(context):
    AmazonMainPageObject(context).login_button.click()
