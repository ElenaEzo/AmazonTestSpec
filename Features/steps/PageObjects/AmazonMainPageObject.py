from selenium.common.exceptions import NoSuchElementException


class AmazonMainPageObject:
    def __init__(self, context):
        context.driver.implicitly_wait(10)
        # initialize elements on the page
        self.context = context.driver
        self.title_element = self.context.find_element_by_id('nav-logo-sprites')
        self.search_field = self.context.find_element_by_id('twotabsearchtextbox')
        self.search_button = self.context.find_element_by_id('nav-search-submit-button')
        self.basket = self.context.find_element_by_id('nav-cart-count')
        self.login_button = self.context.find_element_by_id('nav-link-accountList-nav-line-1')

    def sort_by_value(self, select_value):
        # open dropdown
        self.context.find_element_by_class_name('a-dropdown-container').click()
        # select value in the dropdown
        sort_by_list = self.context.find_elements_by_class_name('a-dropdown-item')
        (next(item for item in sort_by_list if item.text == select_value)).click()

    def check_search_result_exists(self):
        try:
            self.context.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]')
        except NoSuchElementException:
            return False
        return True

    def get_first_available_item(self):
        if self.check_search_result_exists():
            search_list = self.context.find_elements_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div')
            for item in search_list:
                if is_available_to_buy(item):
                    return item
        return None


def is_available_to_buy(element):
    try:
        element.find_element_by_xpath('.//*/div/div/div[2]/div[3]/div')
    except NoSuchElementException:
        return True
    return False
