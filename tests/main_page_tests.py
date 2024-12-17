import re
import time

from core import (
    wait_and_click,
    setup_drive,
    login_in_system,
    click_random_tournament,
    click_random_blog,
    switch_to_new_window
)
#Тут надо на тест стянуть продовую ссылку на кнопку
def test_click_participate():
    driver = setup_drive()
    try:
        wait_and_click(driver, "//*[text()='Участвовать']")
        time.sleep(2)

        current_url = driver.current_url
        if "https://bigplay.gg/ru/tournaments" in current_url:
            print("Тест успешно завершен: Кнопка'Участвовать' работает корректно.")
        else:
            raise Exception("Ошибка: Кнопка 'Участвовать' работает некорректно. URL не соответствует ожиданиям")
    except Exception as e:
        print(f"Ошибка во время теста по 'Участвовать': {e}")
    finally:
        driver.quit()

def test_click_registration():
    driver = setup_drive()
    try:
        wait_and_click(driver, "//*[text()='Регистрируйся']")
        time.sleep(2)

        current_url = driver.current_url
        if "https://client.bigplay.gg/ru/registration" in current_url:
            print("Тест успешно завершен: Кнопка 'Регистрируйся' работает корректно.")
        else:
            raise Exception("Ошибка: Кнопка 'Регистрируйся' работает некорректно. URL не соответствует ожиданиям")
    except Exception as e:
        print(f"Ошибка во время теста по 'Регистрируйся': {e}")
    finally:
        driver.quit()

def test_click_create_team():
    driver = setup_drive()
    login_in_system(driver)
    try:
        time.sleep(4)
        wait_and_click(driver, "//*[text()='Создавай команду']")
        time.sleep(2)

        current_url = driver.current_url
        if "https://client.bigplay.gg/ru/my-teams" in current_url:
            print("Тест успешно завершен: Кнопка 'Создавай команду' работает корректно.")
        else:
            raise Exception("Ошибка: Кнопка 'Создавай команду' работает некорректно. URL не соответствует ожиданиям")
    except Exception as e:
        print(f"Ошибка во время теста по 'Создавай команду': {e}")
    finally:
        driver.quit()

def test_click_win_button():
    driver = setup_drive()
    login_in_system(driver)
    try:
        time.sleep(4)
        wait_and_click(driver, "//*[text()='Побеждай']")
        time.sleep(2)

        current_url = driver.current_url
        if "https://client.bigplay.gg/ru/esports-mobile-tournaments" in current_url:
            print("Тест успешно завершен: Кнопка 'Побеждай' работает корректно.")
        else:
            raise Exception("Ошибка: Кнопка 'Побеждай' работает некорректно. URL не соответствует ожиданиям")
    except Exception as e:
        print(f"Ошибка во время теста по 'Побеждай': {e}")
    finally:
        driver.quit()

def test_click_show_all_tournaments():
    driver = setup_drive()
    try:
        wait_and_click(driver, "//*[text()='Показать все турниры']")
        time.sleep(2)

        current_url = driver.current_url
        if "https://client.bigplay.gg/ru/esports-mobile-tournaments" in current_url:
            print("Тест успешно завершен: Кнопка 'Показать все турниры' работает корректно.")
        else:
            raise Exception("Ошибка: Кнопка 'Показать все турниры' работает некорректно. URL не соответствует ожиданиям")
    except Exception as e:
        print(f"Ошибка во время теста по 'Показать все турниры': {e}")
    finally:
        driver.quit()

#не забыть, тут я должен был править еще
def test_click_show_rand_tournament():
    driver = setup_drive()
    try:
        wait_and_click(driver, "//*[text()='Показать все турниры']")
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

def test_click_show_rand_blog():
    driver = setup_drive()
    try:
        click_random_blog(driver)
        time.sleep(2)
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

def test_click_support_discord():
    driver = setup_drive()
    login_in_system(driver)
    try:
        time.sleep(4)
        wait_and_click(driver, "//*[text()='Поддержка Discord']")
        time.sleep(2)

        switch_to_new_window(driver)

        current_url = driver.current_url

        expected_url = "https://discord.com/invite/qVM4dkCtVF"
        if current_url == expected_url:
            print("Тест успешно завершен: Окно с Discord открылось корректно.")
        else:
            raise Exception(f"Ошибка: Окно Discord открылось с некорректным URL: {current_url}")

    except Exception as e:
        print(f"Ошибка при тестировании поддержки Discord: {e}")
    finally:
        driver.quit()

def test_click_support_telegram():
    driver = setup_drive()
    login_in_system(driver)
    try:
        time.sleep(4)
        wait_and_click(driver, "//*[text()='Поддержка Телеграм']")
        time.sleep(2)

        switch_to_new_window(driver)

        current_url = driver.current_url

        expected_url = "https://t.me/bigplayesportchat"
        if current_url == expected_url:
            print("Тест успешно завершен: Окно с Telegram открылось корректно.")
        else:
            raise Exception(f"Ошибка: Окно Telegram открылось с некорректным URL: {current_url}")

    except Exception as e:
        print(f"Ошибка при тестировании поддержки Telegram: {e}")
    finally:
        driver.quit()

def test_click_header_tournaments():
    driver = setup_drive()
    try:
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Турниры']")
        time.sleep(2)

        current_url = driver.current_url
        if "https://client.bigplay.gg/ru/esports-mobile-tournaments" in current_url:
            print("Тест успешно завершен: Кнопка 'Турниры' работает корректно.")
        else:
            raise Exception("Ошибка: Кнопка 'Турниры' работает некорректно. URL не соответствует ожиданиям")
    except Exception as e:
        print(f"Ошибка во время теста по 'Турниры': {e}")
    finally:
        driver.quit()

def test_click_header_custom_games():
    driver = setup_drive()
    try:
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Кастомные игры']")
        time.sleep(2)

        current_url = driver.current_url
        if "https://client.bigplay.gg/ru/custom-games" in current_url:
            print("Тест успешно завершен: Кнопка 'Кастомные игры' работает корректно.")
        else:
            raise Exception("Ошибка: Кнопка 'Кастомные игры' работает некорректно. URL не соответствует ожиданиям")
    except Exception as e:
        print(f"Ошибка во время теста по 'Кастомные игры': {e}")
    finally:
        driver.quit()

def test_click_header_media():
    driver = setup_drive()
    try:
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Медиа']")
        time.sleep(2)

        current_url = driver.current_url
        if "https://client.bigplay.gg/ru/watch" in current_url:
            print("Тест успешно завершен: Кнопка 'Медиа' работает корректно.")
        else:
            raise Exception("Ошибка: Кнопка 'Медиа' работает некорректно. URL не соответствует ожиданиям")
    except Exception as e:
        print(f"Ошибка во время теста по 'Медиа': {e}")
    finally:
        driver.quit()

def test_click_header_helpdesc():
    driver = setup_drive()
    try:
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Помощь']")
        time.sleep(2)

        current_url = driver.current_url
        if "https://client.bigplay.gg/ru/help" in current_url:
            print("Тест успешно завершен: Кнопка 'Помощь' работает корректно.")
        else:
            raise Exception("Ошибка: Кнопка 'Помощь' работает некорректно. URL не соответствует ожиданиям")
    except Exception as e:
        print(f"Ошибка во время теста по 'Помощь': {e}")
    finally:
        driver.quit()

def test_click_header_blog():
    driver = setup_drive()
    try:
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Блог']")
        time.sleep(2)

        current_url = driver.current_url
        if "https://client.bigplay.gg/ru/news" in current_url:
            print("Тест успешно завершен: Кнопка 'Блог' работает корректно.")
        else:
            raise Exception("Ошибка: Кнопка 'Блог' работает некорректно. URL не соответствует ожиданиям")
    except Exception as e:
        print(f"Ошибка во время теста по 'Блог': {e}")
    finally:
        driver.quit()

def test_click_header_rating():
    driver = setup_drive()
    try:
        time.sleep(2)
        wait_and_click(driver, "//*[text()='Рейтинг']")
        time.sleep(2)

        current_url = driver.current_url
        expected_base_url = "https://client.bigplay.gg/ru/rating/"
        if re.match(f"^{re.escape(expected_base_url)}.*", current_url):
            print("Тест успешно завершен: Кнопка 'Рейтинг' работает корректно.")
        else:
            raise Exception("Ошибка: Кнопка 'Рейтинг' работает некорректно. URL не соответствует ожиданиям")
    except Exception as e:
        print(f"Ошибка во время теста по 'Рейтинг': {e}")
    finally:
        driver.quit()
