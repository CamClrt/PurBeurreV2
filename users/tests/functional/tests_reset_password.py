from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from pur_beurre.settings import BASE_DIR


firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True


class ResetPasswordTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Firefox(
            executable_path=f"{BASE_DIR}/webdrivers/geckodriver",
            options=firefox_options,
        )
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()

    def test_user_reset_password(self):
        self.driver.get("%s%s" % (self.live_server_url, "/login/"))
        self.driver.find_element_by_link_text("Mot de passe oublié ?").click()
        email_input = self.driver.find_element_by_id("id_email")
        email_input.send_keys("fake_user@gmail.com")
        self.driver.find_element_by_class_name("btn").click()
