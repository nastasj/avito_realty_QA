from selenium.webdriver.common.by import By


class FeaturePageLocators:

    CITY_CHOOSER_FIELD = (By.CSS_SELECTOR, '[data-marker="location-chooser/value"]')
    CITY_SEARCH_BOX = (By.CSS_SELECTOR, '[data-marker="region-search-bar/search"]')
    SUBWAY_CHOOSER_FIELD = (By.CSS_SELECTOR, '[data-marker="metro-select/withoutValue"]')
    ALPHABET_CHOOSER_TAB = (By.CSS_SELECTOR, '[class ="css-17syd5g"][tabindex="0"]')
    LINE_CHOOSER_TAB = (By.CSS_SELECTOR, '[class ="css-17syd5g"][tabindex="-1"]')
    STATIONS_ALPHABET_LIST_FIELD = (By.CLASS_NAME, "css-1nm6007")
    STATIONS_ALPHABET_LIST = (By.CLASS_NAME, "css-1suadfl")
    STATIONS_LINES_LIST_FIELD = (By.CLASS_NAME, "css-1nm6007")
    STATIONS_LINES_LIST = (By.CLASS_NAME, "css-1suadfl")
    STATION_LINES_LIST_WITH_CHECKBOXES = (By.CSS_SELECTOR, '[class="css-1suadfl"][aria-checked="true"] [class="_2Jon7"]')
    ALL_LINES = (By.CSS_SELECTOR, '[class="bX_gx css-13meolr"]')
    LINES_CHOSEN = (By.CLASS_NAME, "css-1j6zceg")
    FLOATING_BUTTON = (By.CSS_SELECTOR, '[data-marker="metro-select-dialog/apply"]')
    ALL_STATIONS_CHECKBOX = (By.CSS_SELECTOR, '[aria-checked="true"][data-marker="metro-select-dialog/lines/all"]')
    LIST_EXTENDED = (By.CSS_SELECTOR, '[data-marker="metro-select-dialog/lines/expanded"]')
    RESET_BUTTON_DISABLED = (By.CLASS_NAME, 'css-yz1jyo')
    RESET_BUTTON_ENABLED = (By.CLASS_NAME, 'css-1b0dh4z')
    TABS_GROUP = (By.CSS_SELECTOR, '[data-marker="metro-select-dialog/tabs"]')
    SUBWAY_SEARCH_BOX = (By.CSS_SELECTOR, '[data-marker="metro-select-dialog/search"]')
    CITY_SUGGESTED = (By.CLASS_NAME, "_3z8Zi")
    MORE_BUTTON = (By.CSS_SELECTOR, '[data-marker="metro-select-dialog/chips/more"]') 