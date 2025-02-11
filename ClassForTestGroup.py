import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from authorization import auth

class ExplorePageActions:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_page(self):
        self.driver.get("https://xn--d1acvi.xn--e1aa2afcdic.xn--p1acf/explore/?form_data_key=4c-XKKSpFFmJ2KbQFRS6lK4G9CvSm1oujr7w9kWQb8bEQJBXwx-isC4Pv0Bptc6c&slice_id=2171&clckid=a79b6c9a")

    def authorize(self):
        auth(self.driver)

    def drag_and_drop_element(self, source_by, source_selector, target_by, target_selector):
        try:
            source_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((source_by, source_selector))
            )
            target_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((target_by, target_selector))
            )
            ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()
        except Exception as e:
            pytest.fail(f"Ошибка при перетаскивании элемента: {e}")

    def select_from_dropdown(self, dropdown_by, dropdown_selector, option_text, save_button_by, save_button_selector):
        try:
            dropdown_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((dropdown_by, dropdown_selector))
            )
            dropdown_element.click()

            # Выбор элемента из списка
            ActionChains(self.driver).send_keys(option_text).send_keys(Keys.ENTER).perform()

            save_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((save_button_by, save_button_selector))
            )
            save_button.click()
        except Exception as e:
            pytest.fail(f"Ошибка при работе с выпадающим списком: {e}")

    def reload_graph(self, reload_button_by, reload_button_selector):
        try:
            reload_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((reload_button_by, reload_button_selector)))
            reload_button.click()
        except Exception as e:
            pytest.fail(f"Ошибка при обновлении графика: {e}")

