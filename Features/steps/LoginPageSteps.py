from behave import *
from Features.steps.PageObjects.EmailPageObject import *
from Features.steps.PageObjects.PasswordPageObject import *


@then("I see the {page_name} page is opened on a new page")
def i_see_login_page(context, page_name):
    if page_name == 'Login':
        assert EmailPageObject(context).page_header.is_displayed() is True
    elif page_name == 'Password':
        assert PasswordPageObject(context).page_header.is_displayed() is True
        pass


@when("I set '{value_field}' in the {type_field} field")
def i_set_value_in_email_field(context, value_field, type_field):
    if type_field == 'Login':
        EmailPageObject(context).email_field.send_keys(value_field)
    elif type_field == 'Password':
        PasswordPageObject(context).password_field.send_keys(value_field)


@when("I click '{button_name}' button")
def i_click_continue_button(context, button_name):
    if button_name == 'Continue':
        EmailPageObject(context).continue_button.click()
    elif button_name == 'SignIn':
        PasswordPageObject(context).signin_button.click()


@then("I see '{label_value}' label on the Password page")
def i_see_the_label_on_page(context, label_value):
    assert PasswordPageObject(context).email_label.text == label_value
