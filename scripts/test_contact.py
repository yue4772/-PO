import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestContact:
    def setup(self):
        self.driver= init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize(("name", "phone"),analyze_file("contact_data", "test_add_contact"))
    def test_contact(self, name, phone):
        self.page.all_contact_page.click_add_contact()

        self.page.add_contact_page.send_name(name)
        self.page.add_contact_page.send_phone(phone)
