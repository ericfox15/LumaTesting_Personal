from selenium.webdriver.common.by import By

from pageObjects.CreateAccountPage import CreateAccountPage
from pageObjects.ProductsPage import ProductsPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    mensLink = (By.ID, "ui-id-5")
    createAccountLink = (By.CSS_SELECTOR, "header[class='page-header'] li:nth-child(3) a:nth-child(1)")

    def getCreateAccount(self):
        self.driver.find_element(*HomePage.createAccountLink).click()
        createAccountPage = CreateAccountPage(self.driver)
        return createAccountPage

    def getMensItems(self):
        self.driver.find_element(*HomePage.mensLink).click()
        productsPage = ProductsPage(self.driver)
        return productsPage