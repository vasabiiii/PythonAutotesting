import re
import time

from core import (
    wait_and_click,
    setup_drive,
    login_in_system,
    click_random_blog
)

def test_blog_filter():
    driver = setup_drive()
    try:
        wait_and_click(driver, "//*[text()='Блог']")
        time.sleep(2)

        wait_and_click(driver, "//*[text()='Популярное']")
        time.sleep(2)

        wait_and_click(driver, "//*[text()='Интервью']")
        time.sleep(2)

        wait_and_click(driver, "//*[text()='Обучающие гайды']")
        time.sleep(2)

        wait_and_click(driver, "//*[text()='Справочник платформы BIGPLAY']")
        time.sleep(2)

        wait_and_click(driver, "//*[text()='Свежее']")
        time.sleep(2)
        print("Тест по фильтрам прошло успешно")
    except Exception as e:
        print(f"Ошибка во время теста по 'Фильтр блогов': {e}")
    finally:
        driver.quit()

def test_click_random_block():
    driver = setup_drive()
    try:
        wait_and_click(driver, "//*[text()='Блог']")
        time.sleep(2)
        click_random_blog(driver)
        time.sleep(4)
        current_url = driver.current_url
        expected_base_url = "https://client.bigplay.gg/ru/news/"
        if re.match(f"^{re.escape(expected_base_url)}.*", current_url):
            print("Тест успешно завершен: Страница блога открылась.")
        else:
            raise Exception("Ошибка: Страница блога не открылась. URL не соответствует ожиданиям")
    except Exception as e:
        print(f"Ошибка во время теста по 'Открыть страницу блога': {e}")
    finally:
        driver.quit()