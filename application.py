import time
from selenium import webdriver
from pages.base_page import BasePage
from pages.catalog_page import CatalogPage


class Application:
    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        time.sleep(1.3)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(20)
        self.base = BasePage(self.driver)
        self.catalog = CatalogPage(self.driver)

    def destroy(self):
        self.driver.quit()
