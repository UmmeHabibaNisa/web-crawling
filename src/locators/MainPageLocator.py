from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    NEXT_BUTTON = (By.LINK_TEXT, "›")
    COMPANY_URL = (By.XPATH, '/html/body/main/section/div/div[2]/div/div/div[1]/a')
