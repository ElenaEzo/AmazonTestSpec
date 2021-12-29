from behave import *
from Features.steps.conftest import *


@given('I start the browser')
def start_the_browser(context):
    initialize_browser(context)


@when("I open '{url}' site in the browser")
def open_web_site(context, url):
    context.driver.get(url)


@when("I close the browser")
def close_the_browser(context):
    close_browser(context)
