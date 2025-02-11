from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import user_name, password


def auth(driver):
    user_name_input = driver.find_element(By.XPATH, "//*[@id='username']")
    user_name_input.send_keys(user_name)
    password_input = driver.find_element(By.XPATH, "//*[@id='password']")
    password_input.send_keys(password)
    entrance = driver.find_element(By.XPATH, "//*[@id='loginbox']/div/div[2]/form/div[3]/div/div/input")
    entrance.click()

