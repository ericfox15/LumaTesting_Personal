from selenium.webdriver.common.by import By




class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.CSS_SELECTOR, "#customer-email")
    firstName = (By.NAME,"firstname")
    lastName = (By.NAME,"lastname")
    streetAddress = (By.XPATH, "(//input[@id='Q1OPD0N'])[1]")
    city = (By.NAME, "city")
    states = (By.NAME, "region_id")
    zip = (By.NAME, "postcode")
    countries = (By.NAME, "country_id")
    phoneNumber = (By.NAME, "telephone")
    shippingMethod = (By.CSS_SELECTOR, ".radio")
    next = (By.CSS_SELECTOR, ".continue.primary")
    alertText = (By.XPATH, "//span[text()='This is a required field.']")

    def getEmail(self):
        return self.driver.find_element(*CheckOutPage.email)
    def getFirstName(self):
        return self.driver.find_element(*CheckOutPage.firstName)

    def getLastName(self):
        return self.driver.find_element(*CheckOutPage.lastName)

    def getAddress(self):
        return self.driver.find_element(*CheckOutPage.streetAddress)

    def getCity(self):
        return self.driver.find_element(*CheckOutPage.city)

    def getStates(self):
        return self.driver.find_element(*CheckOutPage.states)

    def getZip(self):
        return self.driver.find_element(*CheckOutPage.zip)

    def getCountryList(self):
        return self.driver.find_element(*CheckOutPage.countries)

    def getPhoneNumber(self):
        return self.driver.find_element(*CheckOutPage.phoneNumber)

    def getShippingMethods(self):
        return self.driver.find_element(*CheckOutPage.shippingMethod)

    def getNext(self):
        return self.driver.find_element(*CheckOutPage.next)

    def getAlertText(self):
        return self.driver.find_element(*CheckOutPage.alertText)







