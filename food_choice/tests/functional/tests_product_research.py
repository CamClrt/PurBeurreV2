from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class ProductResearchTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_research_product_with_home_buttom(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/"))
        research_input = self.selenium.find_element_by_id("home_search")
        research_input.send_keys("Nutella")
        self.selenium.find_element_by_class_name("btn").click()
