

class AllOffersDialogObject:
    def __init__(self, context):
        context.driver.implicitly_wait(10)
        # initialize elements on the page
        self.context = context.driver
        self.dialog_title = self.context.find_element_by_id('aod-container')
        self.offers = self.context.find_elements_by_id('aod-offer-price')
        self.close_dialog_button = self.context.find_element_by_id('aod-close')

    def sort_offer_by_prise(self):
        dict_for_cheapest_offer = {}
        for item in self.offers:
            # prepare current price value
            price = item.find_element_by_xpath('.//*/div/div/div/span').text.replace('\n', '.')[1:]
            # add to dictionary with key=price
            dict_for_cheapest_offer[price] = item

        # get first value from sorted dictionary by key
        return next(iter((dict(sorted(dict_for_cheapest_offer.items()))).values()))

    def get_button_for_the_cheapest_offer(self):
        element = self.sort_offer_by_prise()
        return element.find_element_by_xpath('.//*/span/span/input')


