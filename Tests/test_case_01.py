import unittest
from selenium import webdriver 
from Objects.homepage import homepage
from Objects.output_page import output_page
from Constants.constants import *

class test1(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome(executable_path='path')  
        self.driver.get(URL)
        
        self.homepage = homepage()   
        self.output_page = output_page()  

    def test1(self):
       
        self.homepage.enter_input(self.driver, input_special)
        
        self.homepage.click_submit(self.driver)
        
        result1 = self.output_page.result(self.driver)
        
        self.assertEqual(result1, input_special, f"Expected {input_special}, but got {result1}")
    
    def teardown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
