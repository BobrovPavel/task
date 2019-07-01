from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from reports import logger

logger = logger.get_logger()


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 15)

    COMPUTERS_LINK = (By.XPATH, "//a[@href='/kompyutery/']")
    NOTEBOOK_DROPDOWN_ITEM = (By.XPATH, "//div[@class='owl-carousel']//a[@href='/noutbuki/']")
    TOP_BANNER_IFRAME = (By.XPATH, "//div[@id='top-banner']//iframe")
    TOP_BANNER = (By.XPATH, "//canvas[@id='canvas']")

    def get_element(self, locator, condition):
        result = None
        if condition == "clickable":
            result = self.wait.until(EC.element_to_be_clickable(locator))
        elif condition == "visibility":
            logger.info("Wait for element [%s] visibility" % str(locator))
            result = self.wait.until(EC.visibility_of_element_located(locator))
        elif condition == "invisibility":
            logger.info("Wait for element [%s] invisibility" % str(locator))
            result = self.wait.until(EC.invisibility_of_element_located(locator))
        return result

    def click(self, locator):
        logger.info("Click on [%s]" % str(locator))
        self.get_element(locator, "clickable").click()

    def move_to_and_click(self, locator):
        logger.info("Move to and click on [%s]" % str(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def swith_to_frame(self, frame_locator):
        logger.info("Switch to iframe [%s]" % str(frame_locator))
        self.driver.switch_to.frame(self.driver.find_element(*frame_locator))

    def type_value(self, locator, value):
        element = self.get_element(locator, "clickable")
        element.clear()
        element.send_keys(value)

    def number_of_elements(self, locator):
        return len(self.driver.find_elements(*locator))

    def wait_banner(self):
        if self.number_of_elements(self.TOP_BANNER_IFRAME) > 0:
            self.swith_to_frame(self.TOP_BANNER_IFRAME)
            self.wait.until(EC.presence_of_all_elements_located(self.TOP_BANNER))
            self.driver.switch_to.default_content()

    def remove_header(self):
        self.driver.execute_script("document.querySelector('header').style.position = 'static';")

    def open_notebook_page(self):
        self.click(self.COMPUTERS_LINK)
        self.click(self.NOTEBOOK_DROPDOWN_ITEM)
