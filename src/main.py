import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.CompanyPage import CompanyPage


class PythonOrgSearch(unittest.TestCase):
    """Simple data mining solution"""

    # Setup chrome
    def setUp(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=options, executable_path='/home/nisa/chromedriver')
        self.driver.get("https://medex.com.bd/companies")

    # start seach in medex
    def test_search_in_medex(self):
        company_page = CompanyPage(self.driver)
        company_page.get_all_companies()

    # driver down
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
