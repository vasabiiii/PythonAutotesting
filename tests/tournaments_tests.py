import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core import (
    wait_and_click,
    setup_drive,
    login_in_system,
    click_random_tournament
)

#тут короче надо дата атрибут дать, а то фигня получается
def test_click_pubg_filter():
    driver = setup_drive()
    login_in_system(driver)
    try:
        time.sleep(4)
        wait_and_click(driver, "//*[text()='Турниры']")
        time.sleep(2)
        wait_and_click(driver, "//button[svg[@xmlns='http://www.w3.org/2000/svg']]")
        time.sleep(2)

        discipline_element = driver.find_element_by_xpath("//*[contains(text(), 'Дисциплина:')]")
        discipline_text = discipline_element.text.strip()

        if "Дисциплина: pubg mobile" in discipline_text:
            print("Дисциплина правильно отображается как PUBG Mobile")
        elif "Дисциплина: MLBB" in discipline_text:
            raise Exception("Ошибка: На странице отображаются MLBB, а не pubg mobile")
        else:
            raise Exception("Ошибка: Дисциплина в целом не распознана")
    except Exception as e:
        print(f"Ошибка во время теста по 'Открыть страницу турнира': {e}")
    finally:
        driver.quit()

def test_click_show_rand_tournament():
    driver = setup_drive()
    login_in_system(driver)
    try:
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Турниры']")
        time.sleep(2)
        click_random_tournament(driver)
        time.sleep(2)
        current_url = driver.current_url
        expected_base_url = "https://client.bigplay.gg/ru/esports-mobile-tournaments/"
        if re.match(f"^{re.escape(expected_base_url)}.*", current_url):
            print("Тест успешно завершен: Страница турнира открылась.")
        else:
            raise Exception("Ошибка: Страница турнира не открылась. URL не соответствует ожиданиям")
    except Exception as e:
        print(f"Ошибка во время теста по 'Открыть страницу турнира': {e}")
    finally:
        driver.quit()

def test_click_schedule_tournament():
    driver = setup_drive()
    login_in_system(driver)
    try:
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Турниры']")
        time.sleep(2)
        click_random_tournament(driver)
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Расписание']")
        time.sleep(2)
        schedule_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[span[text()='Расписание']]"))
        )
        if "active" in schedule_element.get_attribute("class"):
            print("Тест успешно завершен: 'Расписание' имеет класс 'active'.")
        else:
            print("Ошибка: 'Расписание' не имеет класса 'active'.")
    except Exception as e:
        print(f"Ошибка во время теста по 'Нажать на Расписание': {e}")
    finally:
        driver.quit()

def test_click_rules_tournament():
    driver = setup_drive()
    login_in_system(driver)
    try:
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Турниры']")
        time.sleep(2)
        click_random_tournament(driver)
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Правила']")
        time.sleep(2)
        schedule_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[span[text()='Правила']]"))
        )
        if "active" in schedule_element.get_attribute("class"):
            print("Тест успешно завершен: 'Правила' имеет класс 'active'.")
        else:
            print("Ошибка: 'Правила' не имеет класса 'active'.")
    except Exception as e:
        print(f"Ошибка во время теста по 'Нажать на Правила': {e}")
    finally:
        driver.quit()

def test_click_bracket_tournament():
    driver = setup_drive()
    login_in_system(driver)
    try:
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Турниры']")
        time.sleep(2)
        click_random_tournament(driver)
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Сетка']")
        time.sleep(2)
        schedule_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[span[text()='Сетка']]"))
        )
        if "active" in schedule_element.get_attribute("class"):
            print("Тест успешно завершен: 'Сетка' имеет класс 'active'.")
        else:
            print("Ошибка: 'Сетка' не имеет класса 'active'.")
    except Exception as e:
        print(f"Ошибка во время теста по 'Нажать на Сетка': {e}")
    finally:
        driver.quit()

def test_click_teams_tournament():
    driver = setup_drive()
    login_in_system(driver)
    try:
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Турниры']")
        time.sleep(2)
        click_random_tournament(driver)
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Команды']")
        time.sleep(2)
        schedule_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[span[text()='Команды']]"))
        )
        if "active" in schedule_element.get_attribute("class"):
            print("Тест успешно завершен: 'Команды' имеет класс 'active'.")
        else:
            print("Ошибка: 'Команды' не имеет класса 'active'.")
    except Exception as e:
        print(f"Ошибка во время теста по 'Нажать на Команды': {e}")
    finally:
        driver.quit()

#он работает, только надо чтоб у турнира обяз был чат
'''
def test_click_chat_tournament():
    driver = setup_drive()
    login_in_system(driver)
    try:
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Турниры']")
        time.sleep(2)
        click_random_tournament(driver)
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Чат']")
        time.sleep(2)
        schedule_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[span[text()='Чат']]"))
        )
        if "active" in schedule_element.get_attribute("class"):
            print("Тест успешно завершен: 'Чат' имеет класс 'active'.")
        else:
            print("Ошибка: 'Чат' не имеет класса 'active'.")
    except Exception as e:
        print(f"Ошибка во время теста по 'Нажать на Чат': {e}")
    finally:
        driver.quit()
'''


