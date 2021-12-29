

class PasswordPageObject:
    def __init__(self, context):
        context.driver.implicitly_wait(10)
        self.context = context.driver
        self.page_header = self.context.find_element_by_class_name('a-link-nav-icon')
        self.email_label = self.context.find_element_by_xpath(
            '//*[@id="authportal-main-section"]/div[2]/div/div/div/div/span')
        self.password_field = self.context.find_element_by_id('ap_password')
        self.signin_button = self.context.find_element_by_id('signInSubmit')
