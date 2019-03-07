from page.add_contact_page import AddcontactPage
from page.all_cantact_page import AllcontactPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def all_contact_page(self):
        return AllcontactPage(self.driver)

    @property
    def add_contact_page(self):
        return AddcontactPage(self.driver)