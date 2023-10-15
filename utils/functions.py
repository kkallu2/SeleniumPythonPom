
def get_datestamp(driver, form_loc, params: list):
    datestamps = driver.find_elements(*getattr(form_loc, params[0]))
    for datestamp in datestamps:
        if datestamp.is_displayed():
            current_datestamp = datestamp.text
            return current_datestamp
