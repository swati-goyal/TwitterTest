from selenium.webdriver import Chrome


class Base:

    def __init__(self):
        self.url = "https://twitter.com/login"
        self.driver = Chrome('/Users/swati/PycharmProjects/TwitterTest/webdrivers/chromedriver')

    def get_driver(self):
        self.driver.implicitly_wait(10)
        return self.driver

    def get_url(self):
        return self.url
