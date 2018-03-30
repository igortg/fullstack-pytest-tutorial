from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_heroes_page(browser):
    browser.navigate_to('/heroes')

    html_input = browser.find_by_css('#hero-name-input')
    for hero_name in ['Batman', 'Robin', 'Catwoman']:
        html_input.send_keys(hero_name)
        button_input = browser.find_by_css('#add-button')
        sleep(0.5)
        button_input.click()
        sleep(0.5)

    heroes_list = browser.find_by_css('ul.heroes').text
    assert 'Batman' in heroes_list
    assert 'Robin' in heroes_list
    assert 'Catwoman' in heroes_list


def test_dashboard_page(browser):
    browser.navigate_to('/dashboard')
    search_input = browser.find_by_css('#search-box')
    search_input.send_keys('Wolv')
    browser.wait_for(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, 'ul.search-result'),
            'Wolverine'
        )
    )
    search_list = browser.find_by_css('ul.search-result')
    sleep(3)
    search_list
