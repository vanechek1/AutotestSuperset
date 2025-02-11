import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from authorization import auth
from ClassForTestGroup import ExplorePageActions

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

def test_only_book_indicator_COUNT(driver):
    actions = ExplorePageActions(driver)
    actions.navigate_to_page()
    actions.authorize()
    # actions.check_element_presence(By.CLASS_NAME, "css-vq8zbz")
    actions.drag_and_drop_element(
        By.XPATH, "//*[@id='explore-container']/div[1]/div[2]/div[2]/div/div/div/div[7]/div/div",
        By.XPATH, "//*[@id='controlSections-panel-query']/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div"
    )
    actions.select_from_dropdown(
        By.XPATH, "//*[@id='adhoc-metric-edit-tabs-panel-SIMPLE']/div[2]/div[2]/div/div/div/div/div[1]/span[2]",
        "COUNT",
        By.XPATH, "//*[@id='metrics-edit-popover']/div[2]/button[2]"
    )
    actions.reload_graph(By.XPATH, "//*[@id='explore-container']/div[2]/div[1]/div[2]/button")
    # error = driver.find_element(By.XPATH, "//*[@id='explore-container']/div[3]/div/div/div[1]/div[2]/div/div[1]/div/strong")
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='chart-id-2171']/div/div/canvas"))
        )
    except Exception as e:
        print(f"Element not found: {e}")

def test_only_book_indicator_SUM(driver):
    actions = ExplorePageActions(driver)
    actions.navigate_to_page()
    actions.authorize()
    # actions.check_element_presence(By.CLASS_NAME, "css-vq8zbz")
    actions.drag_and_drop_element(
        By.XPATH, "//*[@id='explore-container']/div[1]/div[2]/div[2]/div/div/div/div[7]/div/div",
        By.XPATH, "//*[@id='controlSections-panel-query']/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div"
    )
    actions.select_from_dropdown(
        By.XPATH, "//*[@id='adhoc-metric-edit-tabs-panel-SIMPLE']/div[2]/div[2]/div/div/div/div/div[1]/span[2]",
        "SUM",
        By.XPATH, "//*[@id='metrics-edit-popover']/div[2]/button[2]"
    )
    actions.reload_graph(By.XPATH, "//*[@id='explore-container']/div[2]/div[1]/div[2]/button")
    error = driver.find_element(By.XPATH, "//*[@id='explore-container']/div[3]/div/div/div[1]/div[2]/div/div[1]/div/strong")
    assert error.text == "Непредвиденная ошибка"

def test_only_genre_indicator(driver):
    actions = ExplorePageActions(driver)
    actions.navigate_to_page()
    actions.authorize()
    # actions.check_element_presence(By.CLASS_NAME, "css-vq8zbz")
    actions.drag_and_drop_element(
        By.XPATH, "//*[@id='explore-container']/div[1]/div[2]/div[2]/div/div/div/div[8]/div/div",
        By.XPATH, "//*[@id='controlSections-panel-query']/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div"
    )
    actions.select_from_dropdown(
        By.XPATH, "//*[@id='adhoc-metric-edit-tabs-panel-SIMPLE']/div[2]/div[2]/div/div/div/div/div[1]/span[2]",
        "SUM",
        By.XPATH, "//*[@id='metrics-edit-popover']/div[2]/button[2]"
    )
    actions.reload_graph(By.XPATH, "//*[@id='explore-container']/div[2]/div[1]/div[2]/button")
    error = driver.find_element(By.XPATH, "//*[@id='explore-container']/div[3]/div/div/div[1]/div[2]/div/div[1]/div/strong")
    assert error.text == "Непредвиденная ошибка"

if __name__ == "__main__":
    pytest.main()

    # book = driver.find_element(By.XPATH, "//*[@id='explore-container']/div[1]/div[2]/div[2]/div/div/div/div[7]/div/div")
    # genre = driver.find_element(By.XPATH, "//*[@id='explore-container']/div[1]/div[2]/div[2]/div/div/div/div[8]/div/div")
    # pages = driver.find_element(By.XPATH, "//*[@id='explore-container']/div[1]/div[2]/div[2]/div/div/div/div[9]/div/div")
