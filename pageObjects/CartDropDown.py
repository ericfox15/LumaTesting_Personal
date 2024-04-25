from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class CartDropDown:

    def __init__(self, driver):
        self.driver = driver

    cart = (By.CSS_SELECTOR,".block-minicart")
    proceedButton = (By.CSS_SELECTOR,".action.primary.checkout")
    def accessCart(self):
        return self.driver.find_element(*CartDropDown.cart)

    def proceedToCheckout(self):
        self.driver.find_element(*CartDropDown.proceedButton).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
