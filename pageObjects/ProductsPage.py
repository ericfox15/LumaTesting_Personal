from selenium.webdriver.common.by import By

from pageObjects.CartDropDown import CartDropDown


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    hoodiesAndSweatshirts = (By.XPATH, "//a[contains(text(),'Hoodies & Sweatshirts')]")
    products = (By.XPATH, "//div/ol/li/div")
    addToCart = (By.CSS_SELECTOR, ".action.primary.tocart")
    confirmationText = (By.XPATH, "/html/body/div[2]/main/div[1]/div[2]/div/div/div")
    sizeAttribute = (By.CSS_SELECTOR, "#option-label-size-143-item-167")
    colorAttribute = (By.CSS_SELECTOR, "#option-label-color-93-item-49")
    def getHoodiesAndSweatshirts(self):
        return self.driver.find_element(*ProductsPage.hoodiesAndSweatshirts).click()

    def getProducts(self):
        return self.driver.find_elements(*ProductsPage.products)

    def getAddToCart(self):
        self.driver.find_element(*ProductsPage.addToCart).click()
        cartDropDown = CartDropDown(self.driver)
        return cartDropDown

    def getConfirmationText(self):
        return self.driver.find_element(*ProductsPage.confirmationText)

    def getSizeAttribute(self):
        return self.driver.find_element(*ProductsPage.sizeAttribute)

    def getColorAttribute(self):
        return self.driver.find_element(*ProductsPage.colorAttribute)
