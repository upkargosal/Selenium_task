from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class homepage:
    input_textbox = (By.NAME,'text')
    submit_button = (By.ID,'button')

    def enter_input(self,driver,input_chr):
        driver.find_element(*self.input_textbox).send_keys(input_chr)

    def click_submit(self,driver):
        driver.find_element(*self.submit_button).click()