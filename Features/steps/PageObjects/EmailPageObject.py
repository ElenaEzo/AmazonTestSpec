

class EmailPageObject:
    def __init__(self, context):
        context.driver.implicitly_wait(10)
        self.context = context.driver
        self.page_header = self.context.find_element_by_class_name('a-link-nav-icon')
        self.email_field = self.context.find_element_by_id('ap_email')
        self.continue_button = self.context.find_element_by_id('continue')
