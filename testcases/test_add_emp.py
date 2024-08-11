import time
from pageobject import Login_Page, Add_emp
from pageobject.Add_emp import Add_EMP_Class
from utilities import readconfig
from utilities.loggerfile import Log_Generator
from utilities.readconfig import Read_config_class


class Test_Add_Emp:
    Photo_File_Path = r"C:\Users\Windows 10\Pictures\82a08970d41cd6cc040bb75f7f6ae75f.jpg"
    log = Log_Generator.loggen()

    # Create an instance of Read_config_class
    config = Read_config_class()
    username = config.getUsername()
    password = config.getPassword()

    def test_add_emp(self, setup):
        self.driver = setup
        self.log.info("Opening browser")

        self.lp = Login_Page.Login_Page_Class(self.driver)
        time.sleep(2)
        self.log.info("Entering Username")
        self.lp.Username(self.username)
        self.log.info("Entering password")
        self.lp.Password(self.password)
        time.sleep(2)
        self.log.info("Clicking on login button")
        self.lp.click_login_button()
        time.sleep(2)

        self.ae = Add_EMP_Class(self.driver)
        self.ae.click_Pim_xpath()
        time.sleep(2)
        self.log.info("Entering first name")
        self.ae.Firstname("credence")
        time.sleep(2)
        self.log.info("Entering middle name")
        self.ae.Middlename("IT")
        time.sleep(2)
        self.log.info("Entering last name")
        self.ae.Lastname("Institute")
        time.sleep(2)
        self.log.info("Uploading photo")
        self.ae.Photo_file_xpath(self.Photo_File_Path)
        time.sleep(2)
        self.log.info("Clicking on save button")
        self.ae.click_save_button()
        self.log.info("Validating success message")
        time.sleep(2)
        if self.ae.validate_success_msg() == "Successfully Saved":
            self.log.info("test_add_emp is passed")
            self.driver.save_screenshot(".\\test_add_emp_pass.png")
            assert True
        else:
            self.log.info("test_add_emp is failed")
            self.driver.save_screenshot(".\\test_add_emp_fail.png")
            assert False

        self.driver.quit()
        self.log.info("test_add_emp testcase is completed")
