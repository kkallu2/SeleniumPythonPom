import time

from base.page_base import PageBase
import allure
from selenium import webdriver

from locators.locators import HomePageLocators


class HomePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the page")
    def get_page_title(self):
        return self.driver.title

    def clickSignInLink(self):
        self.driver.find_element(*HomePageLocators.SINGIN_LINK).click()

    def enterUserName(self, username):
        self.driver.find_element(*HomePageLocators.USERNAME_LOC).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(*HomePageLocators.PASSWORD_LOC).send_keys(password)
