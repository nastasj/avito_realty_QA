import random
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def delete_ticks_from_checkboxes(self, how, what, ):
        checkboxes = self.driver.find_elements(how, what)
        for checkbox in checkboxes:
            if checkbox.is_selected():
                checkbox.click()

    def is_appeared(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_disappeared(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_element_disabled(self, how, what):
        assert self.browser.find_element(how, what).is_enabled() is False

    def is_element_enabled(self, how, what):
        assert self.browser.find_element(how, what).is_enabled()

    def switch_tab(self, how, what):
        element = self.browser.find_element(how, what)
        self.browser.execute_script("arguments[0].click();", element)

    def scroll_up(self):
        self.browser.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
        # self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

    def open(self):
        self.browser.get(self.url)

    def choose_one_random_element_from_checkboxes(self, how, what):
        all_checkbox_list = self.browser.find_elements(how, what)
        number = random.randint(0, len(all_checkbox_list) - 1)
        self.browser.execute_script("arguments[0].click();", all_checkbox_list[number])
        chosen_station_name = all_checkbox_list[number].text
        return chosen_station_name

    def choose_random_elements_from_checkboxes(self, how, what):
        all_checkbox_list = self.browser.find_elements(how, what)
        number = random.randint(1, len(all_checkbox_list))
        lst2 = [random.randint(0, len(all_checkbox_list) - 1) for i in range(number)]
        lst = list(set(lst2))
        lst.sort()
        chosen_checkbox_list = []
        for i in range(len(lst)):
            self.browser.execute_script("arguments[0].click();", all_checkbox_list[lst[i]])
            chosen_checkbox_list.append(all_checkbox_list[lst[i]].text)
        return chosen_checkbox_list

    def choose_random_letter(self):
        upper_letter = chr(random.randint(1040, 1072))
        lower_letter = chr(ord(upper_letter) + 32)
        return upper_letter, lower_letter

    def fill_field_and_choose_suggest(self, how, what, how2, what2, how3, what3, filling):
        self.browser.find_element(how, what).click()
        self.browser.find_element(how2, what2).send_keys(filling)
        time.sleep(2)
        suggested_list = self.browser.find_elements(how3, what3)
        for i in range(len(suggested_list)):
            suggest = suggested_list[i].get_attribute('textContent')
            if suggest == filling:
                print(suggest)
                suggested_list[i].click()
                break











