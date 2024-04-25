import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from utilites.BaseClass import BaseClass


class TestCart(BaseClass):

    def test_Cart(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("Item successfully added to cart")
        productsPage = homePage.getMensItems()
        productsPage.getHoodiesAndSweatshirts()
        products = productsPage.getProducts()
        for product in products:
            productName = product.find_element(By.XPATH, "div/strong/a")
            if "Hero" in productName.text:
                productName.click()
                break
        productsPage.getSizeAttribute().click()
        productsPage.getColorAttribute().click()
        productsPage.getAddToCart()
        wait = WebDriverWait(self.driver, 4)
        wait.until(expected_conditions.invisibility_of_element((By.CSS_SELECTOR, ".action.primary.tocart.disabled")))
        alertText = productsPage.getConfirmationText().text
        assert "You added", "to your shopping cart." in alertText
