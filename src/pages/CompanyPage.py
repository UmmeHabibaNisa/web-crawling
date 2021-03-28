from selenium.common.exceptions import NoSuchElementException

from .BasePage import BasePage
from .DrugPage import DrugPage
from writter.WriteCsv import WriteCsv

from locators.MainPageLocator import MainPageLocators


class CompanyPage(BasePage):
    has_next = True

    def __go_next_page(self):
        try:
            element = self.driver.find_element(*MainPageLocators.NEXT_BUTTON)
            element.click()
        except NoSuchElementException:
            self.has_next = False
            print(f'Element not found, moving to drug collection')
            drug_page = DrugPage(self.driver)
            drug_page.get_companies()

    def get_all_companies(self):
        WriteCsv.write_company(self)
        if self.has_next:
            self.__go_next_page()
            self.get_all_companies()
