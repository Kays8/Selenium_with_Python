import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestCustomerForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
        self.driver.get("http://localhost/customer/form.html")

    def test_case1(self):
        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canonc")
        ageInput.send_keys("2")

        submitButton.click()

        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnjohn", result)

        # Save screenshot
        self.driver.save_screenshot("test_case1_screenshot.png")

    # ตัวอย่างเทสอื่น ๆ อาจมีการใส่โค้ดเพิ่มเติมในที่นี้

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
