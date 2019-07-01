from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from reports import logger

logger = logger.get_logger()


class CatalogPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    SHOW_MORE_MARKS = (By.XPATH, "//span[@data-idgroup='prof_1000' and not(contains(@class, 'hidden'))]")
    SHOW_MORE_DIAG = (By.XPATH, "//span[@data-idgroup='prof_5828' and not(contains(@class, 'hidden'))]")
    ALL_DIAG = (By.XPATH, "//div[@id='Attr_prof_5828']//label")
    PRICE_BEFORE = (By.XPATH, "//input[@name='price_before']")
    PRICE_AFTER = (By.XPATH, "//input[@name='price_after']")
    SHOW_RESULT_BUTTON = (By.XPATH, "//div[contains(@class,'ModelFilter__ParamListBtnSel')]")
    SHOW_RESULT_BUTTON_TEXT = (By.XPATH, "//span[@class='ModelFilter__CountItems']")
    PRODUCT_LIST_ELEMENT = (By.XPATH, "//div[@itemprop='itemListElement']")
    SORT_SELECT = (By.XPATH, "//div[contains(@class,'SortBlock')]")
    SORT_WITH_CHEAP = (By.XPATH, "//li[contains(@id,'chzn_o_1')]")
    SORT_WITH_DEAR = (By.XPATH, "//li[contains(@id,'chzn_o_2')]")
    NOTEBOOK_NAME = (By.XPATH, "//div[@class='ModelList']//span[@itemprop='name']")

    marks = ["Lenovo", "HP", "Dell"]

    def select_marks(self, *args):
        self.wait_banner()
        self.move_to_and_click(self.SHOW_MORE_MARKS)
        self.remove_header()
        for arg in args:
            self.move_to_and_click((By.XPATH, "//label[contains(text(),'" + arg + "')][not(preceding-sibling::input[@disabled='disabled'])]"))

    def set_price(self, before, after):
        self.type_value(self.PRICE_BEFORE, str(before))
        self.type_value(self.PRICE_AFTER, str(after))

    def get_all_diag(self):
        all_diag = self.driver.find_elements(*self.ALL_DIAG)
        all_diag_text = []
        for i in all_diag:
            all_diag_text.append(i.get_attribute("innerHTML"))
        return all_diag_text

    def set_diag(self, before, after):
        self.move_to_and_click(self.SHOW_MORE_DIAG)
        for i in range(before, after, 1):
            if str(i / 10.0) in self.get_all_diag():
                self.move_to_and_click((By.XPATH, "//div[@id='Attr_prof_5828']//label[text()='" + str(i / 10.0) + "']"))

    def apply_filters(self):
        self.select_marks(*self.marks)
        self.set_diag(120, 134)
        self.set_price(700, 1200)

    def show_result(self):
        self.wait.until(EC.presence_of_element_located(self.SHOW_RESULT_BUTTON))
        self.click(self.SHOW_RESULT_BUTTON)

    def compare_product_list_size(self):
        products_on_page = len(self.driver.find_elements(*self.PRODUCT_LIST_ELEMENT))
        button_text = self.driver.find_element(*self.SHOW_RESULT_BUTTON_TEXT).text
        logger.info("Total products found - %s" % products_on_page)
        return True if str(products_on_page) in button_text else False

    def sort_by_price_up(self):
        self.click(self.SORT_SELECT)
        self.click(self.SORT_WITH_CHEAP)

    def sort_by_price_down(self):
        self.click(self.SORT_SELECT)
        self.click(self.SORT_WITH_DEAR)

    def get_first_book_name_on_page(self):
        books = self.driver.find_elements(*self.NOTEBOOK_NAME)
        book_name = books[0].text
        logger.info("First notebook name is [%s]" % book_name)
        return book_name

    def get_last_book_name_on_page(self):
        books = self.driver.find_elements(*self.NOTEBOOK_NAME)
        book_name = books[-1].text
        logger.info("Last notebook name is [%s]" % book_name)
        return book_name
