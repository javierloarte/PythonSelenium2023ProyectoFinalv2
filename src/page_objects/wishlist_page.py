import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage



class WishlistPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(WishlistPage, self).__init__(driver, wait_driver)

    def wishlist_logim(self, mail: str, password: str):
        self.element("mail_input").wait_clickable().send_keys(mail)
        self.element("pass_input").wait_clickable().send_keys(password)
        self.element("login_btn").wait_clickable().click()

    def wishlist_remove(self, value: str):
        self.element("wish_btn").wait_clickable().click()
        self.element("item_canon").wait_visible()
        self.element("remove_btn").wait_clickable().click()
        self.element("continue_btn").wait_clickable().click()



