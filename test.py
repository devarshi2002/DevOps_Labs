from selenium import webdriver
import pytest

def test_google_search():
    driver = webdriver.Chrome()   # needs chromedriver installed in PATH
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
