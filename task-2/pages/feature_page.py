from .base_page import BasePage
from .locators import FeaturePageLocators
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.keys import Keys


class FeaturePage(BasePage):

    def should_be_subway_field(self):
        assert self.is_element_present(*FeaturePageLocators.SUBWAY_CHOOSER_FIELD), \
            "Subway chooser is not presented, but it should be"

    def should_be_filter_screen(self):
        assert self.is_element_present(*FeaturePageLocators.STATIONS_ALPHABET_LIST_FIELD), \
            "Filter screen is not presented, but it should be"

    def open_filter_screen(self):
        self.browser.find_element(*FeaturePageLocators.SUBWAY_CHOOSER_FIELD).click()

    def should_not_be_subway_field(self):
        assert self.is_not_element_present(*FeaturePageLocators.SUBWAY_CHOOSER_FIELD), \
            "Subway chooser is presented, but it should not be"

    def one_random_station_should_be_chosen_from_alphabet_list(self):
        return self.choose_one_random_element_from_checkboxes(*FeaturePageLocators.STATIONS_ALPHABET_LIST)

    def some_random_stations_should_be_chosen_from_alphabet_list(self):
        return self.choose_random_elements_from_checkboxes(*FeaturePageLocators.STATIONS_ALPHABET_LIST)

    def switching_tabs_should_save_checkboxes(self):
        lst2 = self.some_random_stations_should_be_chosen_from_alphabet_list()
        self.scroll_up()
        if self.is_element_present(*FeaturePageLocators.MORE_BUTTON):
            self.browser.find_element(*FeaturePageLocators.MORE_BUTTON).click()
        lst = self.browser.find_elements(*FeaturePageLocators.LINES_CHOSEN)
        for i in range(len(lst)):
            self.browser.execute_script("arguments[0];", lst[i])
            assert lst[i].text == lst2[i]
        self.switch_tab(*FeaturePageLocators.LINE_CHOOSER_TAB)
        self.scroll_up()
        lst3 = self.browser.find_elements(*FeaturePageLocators.LINES_CHOSEN)
        for i in range(len(lst3)):
            self.browser.execute_script("arguments[0];", lst[i])
            assert lst[i].text == lst3[i].text

    def should_be_floating_button_after_choosing_station(self):
        self.one_random_station_should_be_chosen_from_alphabet_list()
        assert self.is_appeared(*FeaturePageLocators.FLOATING_BUTTON)

    def choice_should_repeat_line_tab_lines_should_not_extend(self):
        choice = self.one_random_station_should_be_chosen_from_alphabet_list()
        self.scroll_up()
        self.switch_tab(*FeaturePageLocators.LINE_CHOOSER_TAB)
        choice2 = self.browser.find_element(*FeaturePageLocators.STATION_LINES_LIST_WITH_CHECKBOXES).get_attribute('textContent')
        assert len(self.browser.find_elements(*FeaturePageLocators.LIST_EXTENDED)) == 0 and choice == choice2

    def reset_button_should_be_disabled(self):
        self.is_element_disabled(*FeaturePageLocators.RESET_BUTTON_DISABLED)

    def reset_button_should_be_enabled(self):
        self.is_element_enabled(*FeaturePageLocators.RESET_BUTTON_ENABLED)

    def stations_list_should_be_closed_while_searching_in_search_box(self):
        self.browser.find_element(*FeaturePageLocators.SUBWAY_SEARCH_BOX).send_keys(' ')
        assert self.is_disappeared(*FeaturePageLocators.TABS_GROUP)

    def correct_words_should_be_on_choice_button(self):
        lst = self.some_random_stations_should_be_chosen_from_alphabet_list()
        button = self.browser.find_element(*FeaturePageLocators.FLOATING_BUTTON).text
        if len(lst) % 10 in (0, 5, 6, 7, 8, 9) or len(lst) in (11, 12, 13, 14):
            assert button == (f"Выбрать {len(lst)} станций")
        elif len(lst) % 10 in (2, 3, 4):
            assert button == (f"Выбрать {len(lst)} станции")
        elif len(lst) % 10 == 1:
            assert button == (f"Выбрать 1 станцию")

    def subway_field_should_be_in_subway_cities(self, city):
        self.fill_field_and_choose_suggest(*FeaturePageLocators.CITY_CHOOSER_FIELD,\
                *FeaturePageLocators.CITY_SEARCH_BOX, *FeaturePageLocators.CITY_SUGGESTED, city)
        time.sleep(2)
        assert self.is_element_present(*FeaturePageLocators.SUBWAY_CHOOSER_FIELD)

    def subway_field_should_not_be_in_other_cities(self, city):
        self.fill_field_and_choose_suggest(*FeaturePageLocators.CITY_CHOOSER_FIELD, \
                        *FeaturePageLocators.CITY_SEARCH_BOX, *FeaturePageLocators.CITY_SUGGESTED, city)
        time.sleep(2)
        assert self.is_not_element_present(*FeaturePageLocators.SUBWAY_CHOOSER_FIELD)

    def search_results_should_contain_letter(self):
        upper_letter, lower_letter = self.choose_random_letter()
        self.browser.find_element(*FeaturePageLocators.CITY_CHOOSER_FIELD).click()
        self.browser.find_element(*FeaturePageLocators.CITY_SEARCH_BOX).send_keys(upper_letter)
        suggested_list = self.browser.find_elements(*FeaturePageLocators.CITY_SUGGESTED)
        for i in range(len(suggested_list)):
            suggest = suggested_list[i].get_attribute('textContent')
            assert upper_letter in suggest or 'Россия' in suggest or lower_letter in suggest


