import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from TestData import AccountData
from pageObjects.HomePage import HomePage
from utilites.BaseClass import BaseClass


class TestCheckout(BaseClass):

    def test_Checkout(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("All required fields must be filled out to place order")
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
        cartDropDown = productsPage.getAddToCart()
        wait = WebDriverWait(self.driver, 4)
        wait.until(expected_conditions.invisibility_of_element((By.CSS_SELECTOR, ".action.primary.tocart.disabled")))
        self.openCart()
        checkOutPage = cartDropDown.proceedToCheckout()
        time.sleep(5)
        checkOutPage.getEmail().send_keys(getData["email"])
        checkOutPage.getFirstName().send_keys(getData["firstname"])
        checkOutPage.getLastName().send_keys(getData["lastname"])
        checkOutPage.getCity().send_keys(getData["city"])
        checkOutPage.getZip().send_keys(getData["zip"])
        checkOutPage.getPhoneNumber().send_keys(getData["phonenumber"])
        checkOutPage.getShippingMethods().click()
        checkOutPage.getNext().click()
        alert = checkOutPage.getAlertText().text
        assert "This is a required field." in alert

    @pytest.fixture(params=AccountData.AccountData.test_account_data)
    def getData(self, request):
        return request.param
