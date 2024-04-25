from selenium.webdriver.common.by import By


class CreateAccountPage:
    def __init__(self, driver):
        self.driver = driver

    firstName = (By.XPATH,"//input[@id='firstname']")
    lastName = (By.ID,"lastname")
    email = (By.NAME,"email")
    password = (By.CSS_SELECTOR,"#password")
    confirmPassword = (By.CSS_SELECTOR,"#password-confirmation")
    createButton = (By.XPATH,"//button[@title='Create an Account']")
    invalidAlert = (By.CSS_SELECTOR, ".message-error")

    def getFirstName(self):
        return self.driver.find_element(*CreateAccountPage.firstName)

    def getLastName(self):
        return self.driver.find_element(*CreateAccountPage.lastName)

    def getEmail(self):
        return self.driver.find_element(*CreateAccountPage.email)

    def getPassword(self):
        return self.driver.find_element(*CreateAccountPage.confirmPassword)

    def getConfirmPassword(self):
        return self.driver.find_element(*CreateAccountPage.password)

    def getCreateButton(self):
        return self.driver.find_element(*CreateAccountPage.createButton)

    def getInvalidAlert(self):
        return self.driver.find_element(*CreateAccountPage.invalidAlert)



