from selenium import webdriver

from pageobject.Login_Page import Login_Page_Class
from utilities.loggerfile import Log_Generator
from utilities.readconfig import Read_config_class


class Test_Login_Params:
    log = Log_Generator.loggen()

    def test_login_params_3(self, setup, getDataForLogin):
        self.log.info("test_login_params_3 is started")
        self.driver = setup
        self.log.info("Opening browser")

        self.lp = Login_Page_Class(self.driver)

        self.log.info("Entering username=" " " + getDataForLogin[0])
        self.lp.Username(getDataForLogin[0])
        self.log.info("Entering Password=" " " + getDataForLogin[1])
        self.lp.Password(getDataForLogin[1])
        self.log.info("clicking on login button")
        self.lp.click_login_button()
        self.log.info("Validating login")
        if self.lp.validate_login() == "Login Pass" and getDataForLogin[1] == "Login_Pass":
            self.log.info("test_OrangeHRM_Login_params_003 is passed")
            self.log.info("Taking screenshot ")
            self.driver.save_screenshot(".\\screenshot\\test_login_params_3.pass.png")
            self.log.info("Click on menu button")
            self.lp.click_menu_button()
            self.log.info("Clicking on logoutbutton")
            self.lp.click_logout_button()
            assert True
        elif self.lp.validate_login() == "Login Pass" and getDataForLogin[1] == "Login_Fail":
            self.log.info("test_OrangeHRM_Login_params_003 is failed")
            self.log.info("Taking screenshot ")
            self.driver.save_screenshot(".\\screenshot\\test_login_params_3.fail.png")
            self.log.info("Click on menu button")
            self.lp.click_menu_button()
            self.log.info("Clicking on logoutbutton")
            self.lp.click_logout_button()
            assert False


        elif self.lp.validate_login() == "Login Fail" and getDataForLogin[1] == "Login_Pass":
            self.log.info("test_OrangeHRM_Login_params_003 is failed")
            self.log.info("Taking screenshot ")
            self.driver.save_screenshot(".\\screenshot\\test_login_params_3.fail.png")
            self.log.info("Click on menu button")
            self.lp.click_menu_button()
            self.log.info("Clicking on logoutbutton")
            self.lp.click_logout_button()
            assert False


        elif self.lp.validate_login() == "Login Fail" and getDataForLogin[1] == "Login_Fail":
            self.log.info("test_OrangeHRM_Login_params_003 is passed")
            self.log.info("Taking screenshot ")
            self.driver.save_screenshot(".\\screenshot\\test_login_params_3.fail.png")
            self.log.info("Click on menu button")
            self.lp.click_menu_button()
            self.log.info("Clicking on logoutbutton")
            self.lp.click_logout_button()
            assert True

            self.log.info("Closing browser")
            self.driver.quit()
            self.log.info("Test test_OrangeHRM_Login_params_003 is completed ")
