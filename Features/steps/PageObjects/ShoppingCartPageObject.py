

class ShoppingCartPageObject:
    def __init__(self, context):
        context.driver.implicitly_wait(10)
        self.context = context.driver
        self.page_header = self.context.find_element_by_xpath('//*[@id="sc-active-cart"]/div/div/div/h1')
        self.items_list = self.context.find_elements_by_xpath(
            "//*/form[@id='activeCartViewForm']/*/*/div[@class='sc-list-item-content']")
        self.subtotal = self.context.find_element_by_id('sc-subtotal-amount-activecart')
        self.proceed_button = self.context.find_element_by_name('proceedToRetailCheckout')

    def get_sum_of_items(self):
        sum_items = 0
        for item in self.items_list:
            # need to remove currency before the price
            sum_items += float(item.find_element_by_xpath('./div/div[2]/p/span').text[1:])
        return sum_items

    def get_subtotal(self):
        # need to remove space and currency before the price
        return float(self.subtotal.text.strip()[1:])

