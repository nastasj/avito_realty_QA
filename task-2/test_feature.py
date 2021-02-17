from pages.feature_page import FeaturePage
from pages.base_page import BasePage
import pytest
import time

link = "https://m.avito.ru/moskva/kommercheskaya_nedvizhimost?cd=1&searchForm=true"


class TestFeature:

    # переключение между табами Алфавит/Линия не сбрасывает выбор
    def test_switching_tabs_saves_checkboxes(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.open_filter_screen()
        page.switching_tabs_should_save_checkboxes()

    # при выборе станции снизу выезжает плавающая кнопка "Выбрать N станций"
    def test_floating_button_appear_after_choosing_station(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.open_filter_screen()
        page.should_be_floating_button_after_choosing_station()

    # при выборе любой станции из алфавитного списка, выбор дублируется и внутри линии, при этом линия не разворачивается
    def test_choice_repeats_line_tab_lines_dont_extend(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.open_filter_screen()
        page.choice_should_repeat_line_tab_lines_should_not_extend()

    # кнопка “Сбросить” появляется только при выбранных станциях
    def test_reset_button_is_disabled(self,  browser):
        page = FeaturePage(browser, link)
        page.open()
        page.open_filter_screen()
        page.reset_button_should_be_disabled()
        page.one_random_station_should_be_chosen_from_alphabet_list()
        page.scroll_up()
        page.reset_button_should_be_enabled()

    # при выборе станции метро через поисковую строку, поиск закрывается
    def test_stations_list_closed_while_searching_in_search_box(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.open_filter_screen()
        page.stations_list_should_be_closed_while_searching_in_search_box()

    # на экране “Уточнить”, примененный фильтр по метро отображаем с формулировкой "Выбрано n станций"
    def test_correct_words_on_choice_button(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.open_filter_screen()
        page.correct_words_should_be_on_choice_button()

    # контрол для выбора станций метро есть только в тех городах, где есть метрополитен
    @pytest.mark.parametrize('city', ['Москва', 'Москва и МО', 'Санкт-Петербург', \
                                      'Санкт-Петербург и ЛО', 'Казань', 'Екатеринбург', \
                                      'Нижний Новгород', 'Новосибирск', 'Самара'])
    def test_subway_field_in_subway_cities(self, browser, city):
        page = FeaturePage(browser, link)
        page.open()
        page.subway_field_should_be_in_subway_cities(city)

    # контрола для выбора станций метро нет в тех городах, где нет метрополитена
    @pytest.mark.parametrize('city', ['Краснодар', 'Тамбов', 'Челябинск'])
    def test_subway_field_not_in_other_cities(self, browser, city):
        page = FeaturePage(browser, link)
        page.open()
        page.subway_field_should_not_be_in_other_cities(city)

    # при вводе буквы в поисковую строку в саджестах отображаются только те названия, в которых есть эта буква
    def test_search_results_contain_letter(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.search_results_should_contain_letter()