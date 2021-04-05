from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from pur_beurre.settings import BASE_DIR


firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True


class AuthenticationTests(StaticLiveServerTestCase):
    fixtures = ["diet.json"]
    # https://docs.djangoproject.com/fr/3.1/topics/settings/
    # https://docs.djangoproject.com/fr/3.1/ref/django-admin/#django-admin-dumpdata
    # https://docs.djangoproject.com/fr/3.1/topics/testing/tools/

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

    def test_register_then_login_with_new_account(self):
        # register
        self.driver.get("%s%s" % (self.live_server_url, "/register/"))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys("Fake User")
        email_input = self.driver.find_element_by_name("email")
        email_input.send_keys("fake.user@email.com")
        password1_input = self.driver.find_element_by_name("password1")
        password1_input.send_keys("fakeUserPassword")
        password2_input = self.driver.find_element_by_name("password2")
        password2_input.send_keys("fakeUserPassword")
        self.driver.find_element_by_class_name("btn").click()

        # the loggin
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys("fake.user@email.com")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("fakeUserPassword")
        self.driver.find_element_by_class_name("btn").click()
