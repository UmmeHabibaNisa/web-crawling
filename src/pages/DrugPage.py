import csv

from selenium.common.exceptions import NoSuchElementException

from .BasePage import BasePage
from writter.WriteCsv import WriteCsv

from locators.MainPageLocator import MainPageLocators


class DrugPage(BasePage):
    has_next = True

    def get_companies(self):
        with open('output.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                self.has_next = True
                line_count += 1
                if len(row) > 0:
                    self.driver.get(row[1])
                print(self)
                self.__get_all_drugs()
            print(f'Processed {line_count} lines.')

    def __go_next_page(self):
        try:
            element = self.driver.find_element(*MainPageLocators.NEXT_BUTTON)
            self.driver.get(element.get_attribute('href'))
            print(f'{self.has_next}')
        except NoSuchElementException:
            self.has_next = False
            print(f' We are eng of the pagination, Getting back to another company')

    def __get_all_drugs(self):
        WriteCsv.write_drugs(self)
        if self.has_next:
            self.__go_next_page()
            self.__get_all_drugs()
