from selenium.webdriver.common.by import By


class HomePageLocators:
    SINGIN_LINK = (By.ID, "signin2")
    USERNAME_LOC = (By.ID, "sign-username")
    PASSWORD_LOC = (By.ID, "sign-password")


class SetLanguageLocators:
    lang_menu = (By.XPATH, "//a[@id='dropdownLangauge']")
    russian_lang = (By.XPATH, "//a[@id='ru']")
    farsi_lang = (By.XPATH, "//a[@id='fa']")
    german_lang = (By.XPATH, "//a[@id='de']")
    vietnamese_lang = (By.XPATH, "//a[@id='vi']")
    french_lang = (By.XPATH, "//a[@id='fr']")
    turkish_lang = (By.XPATH, "//a[@id='tr']")
    arabic_lang = (By.XPATH, "//a[@id='ar']")
    spanish_lang = (By.XPATH, "//a[@id='es']")
    english_lang = (By.XPATH, "//a[@id='en']")

