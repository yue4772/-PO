from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AllcontactPage(BaseAction):
    allcontact_button = By.ID, "com.android.contacts:id/floating_action_button"


    def click_add_contact(self):
        self.click(self.allcontact_button)

