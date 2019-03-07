from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddcontactPage(BaseAction):
    name = By.XPATH, "//*[@text='姓名']"
    phone = By.XPATH, "//*[@text='电话']"


    def send_name(self, text):
        self.input(self.name, text)

    def send_phone(self, text):
        self.input(self.phone, text)



