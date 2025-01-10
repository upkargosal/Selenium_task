from selenium.webdriver.common.by import By

class output_page:
    output_value = (By.ID,'result')

    def result(self,driver):
        return driver.find_element(*self.output_value).text
    