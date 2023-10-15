from selenium import webdriver
from helpers.webdriver_listener import WebDriverListener
from extensions.webdriver_extended import WebDriverExtended


class DriverFactory:
    @staticmethod
    def get_driver(config) -> WebDriverExtended:
        if config["browser"] == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            if config["headless_mode"] is True:
                options.add_argument("--headless")
            driver = WebDriverExtended(
                webdriver.Chrome(),
                WebDriverListener(), config
            )
            return driver
        elif config["browser"] == "firefox":
            options = webdriver.FirefoxOptions()
            if config["headless_mode"] is True:
                options.headless = True
            driver = WebDriverExtended(
                webdriver.Firefox(options=options),
                WebDriverListener(), config
            )
            return driver
        raise Exception("Provide valid driver name")
