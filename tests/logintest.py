import unittest
from pages.login import Login
from pages.dashboard import Dashboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TwitterLoginTest(unittest.TestCase):
    login_obj = Login()
    dash_obj = Dashboard()
    # uname = input("Enter username: ")
    # pswd = input("Enter password: ")

    def setUp(self):
        self.login_obj.open_url()

    def test(self):
        # Login to Twitter
        try:
            self.login_obj.login("testing_robot_", "Beijing@123")
            WebDriverWait(self.login_obj.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.dash_obj.profile)))
        except:
            self.login_obj.driver.save_screenshot("screenshots/Screenshot-{}.png".format("Login Unsuccessful"))
        finally:
            print("Login Successful")

        # Search for POTUS
        self.dash_obj.search("POTUS")

        # follow POTUS
        self.dash_obj.follow()
        self.dash_obj.driver.save_screenshot("screenshots/Screenshot-Potus-Page.png")

        # Validate follow
        try:
            self.dash_obj.validate_follow("testing_robot_", "POTUS")
            print("Validation Success")
        except:
            print("Validation failed!")

        # Logout of Twitter
        try:
            self.dash_obj.logout()
            print("Logout Successful")
        except:
            print("Logout Failed!")

    def tearDown(self):
        self.login_obj.close_driver_session()