import time
from selenium.webdriver.common.by import By

from core import (
    wait_and_click,
    setup_drive,
    login_in_system,
    wait_and_send_keys
)

def test_create_stream():
    driver = setup_drive()
    login_in_system(driver)
    time.sleep(4)
    try:
        wait_and_click(driver, "//*[text()='Кастомные игры']")
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Создать стрим']")
        time.sleep(2)

        specific_xpath = "//div[contains(@class, 'tab-buttons')]//button[span[text()='Кастомные игры']]"
        wait_and_click(driver, specific_xpath)
        time.sleep(2)

        wait_and_send_keys(driver, "//label[contains(text(), 'Название стрима')]",
                           "Тестовый стрим",
                           find_by_label=True)
        wait_and_send_keys(driver, "//label[contains(text(), 'Описание стрима')]",
                           "Тестовое описание для стрима",
                           find_by_label=True)
        wait_and_send_keys(driver, "//label[contains(text(), 'Ссылка на стрим')]",
                           "https://www.youtube.com/watch?v=-CNymheDE3M&ab_channel=jeremytodd1",
                           find_by_label=True)
        wait_and_send_keys(driver, "//label[contains(text(), 'Номер вашего лобби')]",
                           "123123",
                           find_by_label=True)
        wait_and_send_keys(driver, "//label[contains(text(), 'Пароль лобби')]",
                           "123123",
                           find_by_label=True)
        wait_and_send_keys(driver, "//label[contains(text(), 'Приз')]",
                           "1000",
                           find_by_label=True)
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[text()='Создать стрим']").click()
        time.sleep(4)

        stream_elements = driver.find_elements(By.XPATH,
                                               "//div[@class='stream-card']//p[contains(text(), 'Тестовый стрим')]")
        if stream_elements:
            print("Тест прошел успешно: Стрим найден на странице.")
        else:
            print("Ошибка: Стрим не найден на странице.")

    except Exception as e:
        print(f"Ошибка во время теста по 'Создать стрим': {e}")
    finally:
        driver.quit()

def test_show_stream():
    driver = setup_drive()
    login_in_system(driver)
    time.sleep(4)
    try:
        wait_and_click(driver, "//*[text()='Кастомные игры']")
        time.sleep(2)

        specific_xpath = "//div[@class='stream-card']//p[contains(text(), 'Тестовый стрим')]"
        wait_and_click(driver, specific_xpath)
        time.sleep(2)

        expected_url = "https://client.bigplay.gg/ru/user/60729"
        current_url = driver.current_url

        if current_url == expected_url:
            print("Тест прошел успешно: Переход по правильной ссылке.")
        else:
            print(f"Ошибка: Ожидался переход на {expected_url}, но текущий URL: {current_url}")

    except Exception as e:
        print(f"Ошибка во время теста по 'Посмотреть стрим': {e}")
    finally:
        driver.quit()

def test_end_stream():
    driver = setup_drive()
    login_in_system(driver)
    time.sleep(4)
    try:
        wait_and_click(driver, "//*[text()='Кастомные игры']")
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Создать стрим']")
        time.sleep(2)

        specific_xpath = "//div[contains(@class, 'tab-buttons')]//button[span[text()='Кастомные игры']]"
        wait_and_click(driver, specific_xpath)
        time.sleep(2)

        wait_and_click(driver, "//*[text()='Завершить']")
        wait_and_click(driver, "//*[text()='Да, завершить']")
        time.sleep(2)

        stream_elements = driver.find_elements(By.XPATH,
                                               "//div[@class='stream-card']//p[contains(text(), 'Тестовый стрим')]")
        if not stream_elements:
            print("Тест прошел успешно: Стрим был завершен.")
        else:
            print("Ошибка: Стрим не был завершен.")

    except Exception as e:
        print(f"Ошибка во время теста по 'Завершить стрим': {e}")
    finally:
        driver.quit()

