import time

from selenium import webdriver

from pageobject.Login_Page import Login_Page_Class
from utilities.loggerfile import Log_Generator
from utilities.readconfig import Read_config_class
from utilities import Excel_utility


class Test_Login_DDT:
    log = Log_Generator.loggen()
    File_Path = ".\\testcases\\Test_data\\~$Test_Data.xlsx"

    def test_OrangeHRM_Login_DDT__4(self, setup, getDataForLogin):
        self.log.info("test_login_params_3 is started")
        self.driver = setup
        self.log.info("Opening browser")
        time.sleep(2)

        self.lp = Login_Page_Class(self.driver)
        self.rows = Excel_utility.get_rowcount(self.File_Path, "Login_Data")
        self.log.info("print no. of rows in excel Test_Data" ' ' + str(self.rows))
        List = []
        Test_Result_Col_no = 5
        for r in range(2, self.rows + 1):
            self.username = Excel_utility.read_data(self.File_Path, "Login_Data", r, 2)
            self.password = Excel_utility.read_data(self.File_Path, "Login_Data", r, 3)
            self.username = Excel_utility.read_data(self.File_Path, "Login_Data", r, 4)
            time.sleep(2)
            self.log.info("Entering username=" " " + getDataForLogin[0])
            self.lp.Username(getDataForLogin[0])
            time.sleep(2)
            self.log.info("Entering Password=" " " + getDataForLogin[1])
            time.sleep(2)
            self.lp.Password(getDataForLogin[1])
            self.log.info("clicking on login button")
            time.sleep(2)
            self.lp.click_login_button()
            self.log.info("Validating login")
            if self.lp.validate_login() == "Login Pass" and self.Excel_Result == "Login_Pass":
                List.append("Pass")
                self.log.info("test_OrangeHRM_Login_params_003 is passed")
                self.log.info("Taking screenshot ")
                self.driver.save_screenshot(".\\screenshot\\test_login_params_3.pass.png")
                self.log.info("Click on menu button")
                self.lp.click_menu_button()
                self.log.info("Clicking on logoutbutton")
                time.sleep(2)
                self.lp.click_logout_button()
                time.sleep(2)


            elif self.lp.validate_login() == "Login Pass" and self.Excel_Result == "Login_Fail":
                List.append("Fail")
                self.log.info("test_OrangeHRM_Login_params_003 is failed")
                self.log.info("Taking screenshot ")
                self.driver.save_screenshot(".\\screenshot\\test_login_params_3.fail.png")
                self.log.info("Click on menu button")
                self.lp.click_menu_button()
                self.log.info("Clicking on logoutbutton")
                self.lp.click_logout_button()



            elif self.lp.validate_login() == "Login Pass" and self.Excel_Result == "Login_Fail":
                self.log.info("test_OrangeHRM_Login_params_003 is Failed")
                List.append("Fail")
                self.log.info("Taking screenshot ")
                self.driver.save_screenshot(".\\screenshot\\test_login_params_3.fail.png")
                self.log.info("Click on menu button")
                self.lp.click_menu_button()
                self.log.info("Clicking on logoutbutton")
                self.lp.click_logout_button()



            elif self.lp.validate_login() == "Login Fail" and self.Exp_Result == "Login_Fail":
                self.log.info("test_OrangeHRM_Login_params_003 is passed")
                List.append("Pass")
                self.log.info("Taking screenshot ")
                self.driver.save_screenshot(".\\screenshot\\test_login_params_3.fail.png")
                self.log.info("Click on menu button")
                self.lp.click_menu_button()
                self.log.info("Clicking on logoutbutton")
                self.lp.click_logout_button()

        print(List)
        if "Fail" not in List:
            self.log.info("test_OrangeHRM_Login_DDT_004 is passed")
            assert True
        else:
            self.log.info("test_OrangeHRM_Login_DDT_004 is failed")
            assert False

        self.driver.quit()
        self.log.info("Closing Browser")
        self.log.info("Test test_OrangeHRM_Login_params_003 is completed")
