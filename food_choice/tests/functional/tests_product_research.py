from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from pur_beurre.settings import BASE_DIR


firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True


class ProductResearchTest(StaticLiveServerTestCase):
    """Functional tests using the Firefox web browser in headless mode."""

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

    def test_research_product_with_home_buttom(self):
        self.driver.get("%s%s" % (self.live_server_url, "/"))
        research_input = self.driver.find_element_by_id("home_search")
        research_input.send_keys("Nutella")
        self.driver.find_element_by_class_name("btn").click()
