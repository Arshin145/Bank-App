import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Add_EMP_Class:
    click_Pim_xpath = (By.XPATH, "//a[@class='oxd-main-menu-item active']")
    add_button_xpath = (By.XPATH, "//button[normalize-space()='Add']")
    firstname_xpath = (By.XPATH, "//input[@placeholder='First Name']")
    middlename_xpath = (By.XPATH, "//input[@placeholder='Middle Name']")
    lastname_xpath = (By.XPATH, "//input[@placeholder='Last Name']")
    Photo_file_xpath = (By.XPATH, "//img[@class='employee-image']")
    click_save_button_xpath = (By.XPATH, "//button[@type='submit']")
    save_msg_xpath = (By.XPATH, "//div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def pim(self):
        self.driver.find_element(*Add_EMP_Class.click_Pim_xpath).click()

    def Firstname(self, firstname):
        self.driver.find_element(*Add_EMP_Class.firstname_xpath).send_keys(firstname)

    def Middlename(self, middlename):
        self.driver.find_element(*Add_EMP_Class.middlename_xpath).send_keys(middlename)

    def Lastname(self, lastname):
        self.driver.find_element(*Add_EMP_Class.lastname_xpath).send_keys(lastname)

    def click_save_button(self):
        self.driver.find_element(*Add_EMP_Class.click_save_button_xpath).click()

    def validate_success_msg(self):
        try:
            self.wait.until(
             expected_conditions.visibility_of_element_located(By.XPATH, "//div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']"))

            self.driver.find_element(self.save_msg_xpath)
            save_msg = self.driver.find_element(self.save_msg_xpath).text
            return save_msg
        except:
            pass



