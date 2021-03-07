from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class AuthenticationTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_register_then_login_with_new_account(self):
        # register
        self.selenium.get("%s%s" % (self.live_server_url, "/register/"))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("Fake User")
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys("fake.user@email.com")
        password1_input = self.selenium.find_element_by_name("password1")
        password1_input.send_keys("fakeUserPassword")
        password2_input = self.selenium.find_element_by_name("password2")
        password2_input.send_keys("fakeUserPassword")
        self.selenium.find_element_by_class_name("btn").click()

        # the loggin
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("fake.user@email.com")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("fakeUserPassword")
        self.selenium.find_element_by_class_name("btn").click()
