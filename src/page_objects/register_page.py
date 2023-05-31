import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage



class RegisterPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(RegisterPage, self).__init__(driver, wait_driver)

    def register(self, name: str, last: str, mail: str, phone: str, password: str, confirmpass: str):
        self.element("register_btn").wait_clickable()
        self.element("name_input").wait_visible().send_keys(name)
        self.element("last_input").wait_visible().send_keys(last)
        self.element("mail_input").wait_visible().send_keys(mail)
        self.element("phone_input").wait_visible().send_keys(phone)
        self.element("password_input").wait_visible().send_keys(password)
        self.element("confirm_input").wait_visible().send_keys(confirmpass)
        self.element("news_select").find_element().is_selected()
        self.element("news_select").wait_visible().click()
        self.element("policy_option").find_element().is_selected()
        self.element("policy_option").wait_visible().click()
        self.element("register_btn").wait_clickable().click()

    def confirm_register(self, ):
        return self.element("success_msg").wait_visible().text

    def continue_register(self):
        self.element("agree_btn").wait_clickable().click()