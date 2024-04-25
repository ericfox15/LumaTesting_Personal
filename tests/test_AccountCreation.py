
import pytest
from selenium.webdriver.common.by import By
from TestData.AccountData import AccountData
from pageObjects.HomePage import HomePage
from utilites.BaseClass import BaseClass


class TestAccountCreation(BaseClass):

    def test_AccountCreation(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        createAccountPage = homePage.getCreateAccount()
        log.info("Multiple accounts can not be created with the same email: " + getData["email"])
        createAccountPage.getFirstName().send_keys(getData["firstname"])
        createAccountPage.getLastName().send_keys(getData["lastname"])
        createAccountPage.getEmail().send_keys(getData["email"])
        createAccountPage.getPassword().send_keys(getData["password"])
        createAccountPage.getConfirmPassword().send_keys(getData["password"])
        createAccountPage.getCreateButton().click()
        alertText =  createAccountPage.getInvalidAlert().text
        assert "already an account" in alertText

    @pytest.fixture(params=AccountData.test_account_data)
    def getData(self, request):
        return request.param
