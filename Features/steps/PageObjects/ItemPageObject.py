

class ItemPageObject:
    def __init__(self, context):
        context.driver.implicitly_wait(10)
        self.context = context.driver
        self.item_name = self.context.find_element_by_id('productTitle')
        self.see_option_button = self.context.find_element_by_class_name('a-button-inner')

