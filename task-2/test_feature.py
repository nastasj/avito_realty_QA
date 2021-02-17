from pages.feature_page import FeaturePage
from pages.base_page import BasePage
import pytest
import time

link = "https://m.avito.ru/moskva/kommercheskaya_nedvizhimost?cd=1&searchForm=true"


class TestFirst:

    @pytest.mark.skip
    def test_switching_tabs_saves_checkboxes(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.open_filter_screen()
        page.switching_tabs_should_save_checkboxes()

    @pytest.mark.skip
    def test_floating_button_appear_after_choosing_station(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.open_filter_screen()
        page.should_be_floating_button_after_choosing_station()

    @pytest.mark.skip
    def test_choice_repeats_line_tab_lines_dont_extend(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.open_filter_screen()
        page.choice_should_repeat_line_tab_lines_should_not_extend()

    @pytest.mark.skip
    def test_reset_button_is_disabled(self,  browser):
        page = FeaturePage(browser, link)
        page.open()
        page.open_filter_screen()
        page.reset_button_should_be_disabled()
        page.one_random_station_should_be_chosen_from_alphabet_list()
        page.scroll_up()
        page.reset_button_should_be_enabled()

    @pytest.mark.skip
    def test_stations_list_closed_while_searching_in_search_box(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.open_filter_screen()
        page.stations_list_should_be_closed_while_searching_in_search_box()

    @pytest.mark.skip
    def test_correct_words_on_choice_button(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.open_filter_screen()
        page.correct_words_should_be_on_choice_button()

    @pytest.mark.skip
    @pytest.mark.parametrize('city', ['Москва', 'Москва и МО', 'Санкт-Петербург', \
                                      'Санкт-Петербург и ЛО', 'Казань', 'Екатеринбург', \
                                      'Нижний Новгород', 'Новосибирск', 'Самара'])
    def test_subway_field_in_subway_cities(self, browser, city):
        page = FeaturePage(browser, link)
        page.open()
        page.subway_field_should_be_in_subway_cities(city)


    @pytest.mark.parametrize('city', ['Чебоксары', 'Краснодар', 'Тамбов', \
                                      'Московская область', 'Ленинградская область'])
    def test_subway_field_not_in_other_cities(self, browser, city):
        page = FeaturePage(browser, link)
        page.open()
        page.subway_field_should_not_be_in_other_cities(city)

    @pytest.mark.skip
    def test_search_results_contain_letter(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.search_results_should_contain_letter()