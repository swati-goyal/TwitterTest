from pages.login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class Dashboard:
    login_obj = Login()
    driver = login_obj.driver

    # Elements
    tweet = '//*[@id="global-new-tweet-button"]/span'
    profile = 'dashboard-profile-prompt'
    profile_id = 'user-dropdown-toggle'
    search_field = '//*[@id="search-query"]'
    search_button = '//*[@id="global-nav-search"]/span/button'
    search_nav = '//*[@class="SearchNavigation-titleText"]'
    follow_button = '//*[@class="user-actions btn-group not-following not-muting "]/span[2]/button[1]'
    following_and_unfollow_button = '.user-actions.btn-group.not-muting.including-following'
    original_tweet_overlay = '//*[@id="permalink-overlay"]/div[1]'
    home_button = '//*[@id="global-nav-home"]/a/span[3]'
    logout_button = '//*[@class="js-signout-button"][@id="signout-button"]'


    def search(self, string):
        wait = WebDriverWait(self.driver, 20)
        self.driver.find_element_by_xpath(self.search_field).send_keys(string)
        self.driver.find_element_by_xpath(self.search_button).click()

        wait.until(EC.title_contains("News about POTUS"))

        all_links = self.driver.find_elements_by_link_text('@'+string)
        all_links[0].click()

        '''
        self.driver.save_screenshot("screenshots/Screenshot-{}.png".format("POTUS-PAGE"))

        wait.until(EC.title_contains(string + 'Twitter'))

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, self.follow_button)))
            self.follow()
        except:
            self.driver.save_screenshot("screenshots/Screenshot-{}.png".format("Following"))
        '''

    def follow(self):
        try:
            follow = self.driver.find_element_by_xpath(self.follow_button)
            self.driver.implicitly_wait(3)
            # wait.until(EC.presence_of_element_located(follow))
            follow.click()
        except:
            self.driver.save_screenshot("screenshots/Screenshot-Already-Following.png")

    def skip_overlay(self):
        try:
            action = ActionChains(self.driver)
            dismiss = self.driver.find_element_by_xpath(self.original_tweet_overlay)
            action.move_to_element(dismiss)
            action.click()
            action.perform()
        except:
            return

    def validate_follow(self, uname, account):
        self.skip_overlay()
        self.driver.get("https://twitter.com/"+uname+"/"+"following")
        # self.driver.find_element_by_xpath(self.following).click()
        self.driver.implicitly_wait(5)
        check = self.driver.find_element_by_link_text('@'+account)
        if check:
            self.driver.save_screenshot("screenshots/Screenshot-{}.png".format("Validation-Success"))
        else:
            self.driver.save_screenshot("screenshots/Screenshot-{}.png".format("Failed"))

    def logout(self):
        self.driver.find_element_by_id(self.profile_id).click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath(self.logout_button).click()


