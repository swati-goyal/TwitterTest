from pages.base import Base


class Login:
    base_obj = Base()
    driver = base_obj.get_driver()
    url = base_obj.get_url()

    # Elements
    username = '//input[@type="text"][@placeholder="Phone, email or username"]'
    password = '.js-password-field'
    login_button = '//*[@id="page-container"]/div/div[1]/form/div[2]/button'
    forgot_password = '//*[@id="page-container"]/div/div[1]/form/div[2]/div/label/a'
    remember_me = '//*[@id="page-container"]/div/div[1]/form/div[2]/div/label/input'
    home = '//*[@id="global-nav-home"]/a/span[2]'
    about = '//*[@id="global-nav-about"]/a/span'
    language = '//*[@id="menu-0"]'
    sign_up_nav = '//*[@id="login-signup-link"]'
    activate_your_account = '//*[@id="page-container"]/div/div[2]/p[2]/a'

    def open_url(self):
        self.driver.get(self.url)

    def login(self, uname, pswd):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.username).send_keys(uname)
        self.driver.find_element_by_css_selector(self.password).send_keys(pswd)
        if self.driver.find_element_by_xpath(self.remember_me).is_selected():
            self.driver.find_element_by_xpath(self.remember_me).click()
        self.driver.find_element_by_xpath(self.login_button).click()

    def close_driver_session(self):
        self.driver.quit()