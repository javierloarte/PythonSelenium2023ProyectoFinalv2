import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage



class SearchPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(SearchPage, self).__init__(driver, wait_driver)

    def search(self, value: str):
        self.element("search_input").wait_clickable().send_keys(value)
        self.element("search_btn").wait_clickable().click()
        self.element("liked_product").wait_clickable().click()
        self.element("liked_success").wait_visible()

    def total_search(self,):
        return self.element("total_like").wait_visible().text


