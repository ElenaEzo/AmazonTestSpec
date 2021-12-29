from behave import *
from Features.steps.PageObjects.AllOffersDialogObject import *


@then("I see that All Offers Dialog is displayed")
def i_see_all_offers_dialog(context):
    assert AllOffersDialogObject(context).dialog_title.is_displayed() is True


@when("I choose the cheapest offer and click 'Add to Cart' button")
def i_choose_the_cheapest_offer(context):
    AllOffersDialogObject(context).get_button_for_the_cheapest_offer().click()


@when("I close All Offers Dialog")
def i_close_dialog(context):
    AllOffersDialogObject(context).close_dialog_button.click()

