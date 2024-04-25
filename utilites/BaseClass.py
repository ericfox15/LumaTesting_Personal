import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CartDropDown import CartDropDown


@pytest.mark.usefixtures("setup")

class BaseClass:
    showCart = (By.CSS_SELECTOR, ".action.showcart")

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByIndex(self, locator, index):
        sel = Select(locator)
        sel.select_by_index(0)

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def openCart(self):
        self.driver.find_element(*BaseClass.showCart).click()
        cartDropDown = CartDropDown(self.driver)
        return cartDropDown





