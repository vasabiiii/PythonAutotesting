import os
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.report_generator import generate_pdf_report_single, SCREENSHOTS_FOLDER
from core import wait_and_click, wait_and_send_keys, setup_drive, wait_and_click_if_condition

def test_login_email_success():
    driver = setup_drive()
    try:
        wait_and_click(driver, "//*[text()='Войти']")
        wait_and_click_if_condition(driver, "//*[text()=' Почта ']", "!bg-[#E4E4E4]", "!bg-white")
        wait_and_send_keys(driver, "//input[@placeholder='Введите свою почту']", "autotest@test.test")
        wait_and_click(driver, "//*[text()=' Продолжить ']")
        wait_and_send_keys(driver, "//input[@placeholder='Введите пароль']", "password")
        wait_and_click(driver, "//img[@alt='глазок']")
        wait_and_click(driver, "//*[text()=' Войти ']")
        time.sleep(4)

        screenshot_path = os.path.join(SCREENSHOTS_FOLDER, "login_success.png")
        driver.save_screenshot(screenshot_path)

        generate_pdf_report_single("Login Email Success",
                                   "Passed",
                                   "The test with correct data has been successfully completed!",
                                   screenshot_path)

        print("Тест с правильными данными успешно завершен!")
    except Exception as e:
        print(f"Ошибка во время теста с правильными данными: {e}")
    finally:
        driver.quit()

def test_login_phone_success():
    driver = setup_drive()
    try:
        wait_and_click(driver, "//*[text()='Войти']")
        wait_and_click_if_condition(driver, "//*[text()=' Телефон ']", "!bg-[#E4E4E4]", "!bg-white")
        wait_and_send_keys(driver, "//input[@placeholder='Введите номер телефона']", "7056806338")
        wait_and_click(driver, "//*[text()=' Продолжить ']")
        wait_and_send_keys(driver, "//input[@placeholder='Введите пароль']", "177013A_r")
        wait_and_click(driver, "//img[@alt='глазок']")
        wait_and_click(driver, "//*[text()=' Войти ']")
        time.sleep(4)

        screenshot_path = os.path.join(SCREENSHOTS_FOLDER, "login_phone_success.png")
        driver.save_screenshot(screenshot_path)

        generate_pdf_report_single("Login Phone Success",
                                   "Passed",
                                   "The test with correct phone has been successfully completed!",
                                   screenshot_path)

        print("Тест с правильными данными успешно завершен!")
    except Exception as e:
        print(f"Ошибка во время теста с правильными данными: {e}")
    finally:
        driver.quit()

def test_registration_phone():
    driver = setup_drive()
    random_number = random.randint(1000000000, 99999999999)
    randname = f"test{random_number}"

    try:
        wait_and_click(driver, "//*[text()='Войти']")
        wait_and_click(driver, "//*[text()=' Создать аккаунт ']")
        wait_and_send_keys(driver, "//input[@placeholder='Введите номер телефона']", random_number)
        wait_and_click(driver, "//*[text()=' Продолжить ']")
        wait_and_send_otp(driver, "123456")
        wait_and_click(driver, "//*[text()=' Отправить ']")
        wait_and_send_keys(driver, "//input[@placeholder='Введите username']", randname)
        wait_and_send_keys(driver, "//input[@placeholder='Придумай пароль']", "password")
        wait_and_send_keys(driver, "//input[@placeholder='Повтори пароль']", "password")
        wait_and_click(driver, "//*[text()=' Продолжить ']")
        wait_and_click(driver, "//img[@alt='pubg icon']")
        wait_and_send_keys(driver, "//input[@placeholder='Введи свой никнейм']", randname)
        wait_and_send_keys(driver, "//input[@placeholder='Введи свой ID']", random_number)
        wait_and_click(driver, "//*[text()=' Завершить ']")
        time.sleep(4)

        screenshot_path = os.path.join(SCREENSHOTS_FOLDER, "registration_phone_success.png")
        driver.save_screenshot(screenshot_path)

        generate_pdf_report_single("Registration Phone Success",
                                   "Passed",
                                   "The registration with correct phone has been successfully completed!",
                                   screenshot_path)

        current_url = driver.current_url
        if "https://client.bigplay.gg/ru/" in current_url:
            print("Тест успешно завершен: Регистрация выполнена.")
        else:
            raise Exception("Ошибка: Регистрация не выполнена, URL не соответствует ожидаемому.")
    except Exception as e:
        print(f"Ошибка во время теста регистрации: {e}")
    finally:
        driver.quit()

def test_login_wrong_email():
    driver = setup_drive()
    try:
        wait_and_click(driver, "//*[text()='Войти']")
        wait_and_click_if_condition(driver, "//*[text()=' Почта ']", "!bg-[#E4E4E4]", "!bg-white")
        wait_and_send_keys(driver, "//input[@placeholder='Введите свою почту']", "wrongtest.test")
        wait_and_click(driver, "//*[text()=' Продолжить ']")

        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[text()='Введите верную почту']"))
        )
        if error_element.text == "Введите верную почту":
            print("Тест с неправильным Email успешно завершен!")
            time.sleep(2)
            screenshot_path = os.path.join(SCREENSHOTS_FOLDER, "login_wrong_email_success.png")
            driver.save_screenshot(screenshot_path)

            generate_pdf_report_single("Login Wrong Email Success",
                                       "Passed",
                                       "The login with wrong email has been successfully completed!",
                                       screenshot_path)
        else:
            print(f"Неверное сообщение об ошибке: {error_element.text}")
    except Exception as e:
        print(f"Ошибка во время теста с неправильным Email: {e}")
    finally:
        driver.quit()

def test_login_wrong_password():
    driver = setup_drive()
    try:
        wait_and_click(driver, "//*[text()='Войти']")
        wait_and_click_if_condition(driver, "//*[text()=' Почта ']", "!bg-[#E4E4E4]", "!bg-white")
        wait_and_send_keys(driver, "//input[@placeholder='Введите свою почту']", "autotest@test.test")
        wait_and_click(driver, "//*[text()=' Продолжить ']")
        wait_and_send_keys(driver, "//input[@placeholder='Введите пароль']", "wrongpassword")
        wait_and_click(driver, "//img[@alt='глазок']")
        wait_and_click(driver, "//*[text()=' Войти ']")

        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[text()='Неверный логин или пароль']"))
        )
        if error_element.text == "Неверный логин или пароль":
            print("Тест с неправильным password успешно завершен!")
            time.sleep(2)
            screenshot_path = os.path.join(SCREENSHOTS_FOLDER, "login_wrong_password_success.png")
            driver.save_screenshot(screenshot_path)

            generate_pdf_report_single("Login Wrong Password Success",
                                       "Passed",
                                       "The login with wrong password has been successfully completed!",
                                       screenshot_path)
        else:
            print(f"Неверное сообщение об ошибке: {error_element.text}")
    except Exception as e:
        print(f"Ошибка во время теста с неправильным Email: {e}")
    finally:
        driver.quit()

def test_login_wrong_phone():
    driver = setup_drive()
    try:
        wait_and_click(driver, "//*[text()='Войти']")
        wait_and_click_if_condition(driver, "//*[text()=' Телефон ']", "!bg-[#E4E4E4]", "!bg-white")
        wait_and_send_keys(driver, "//input[@placeholder='Введите номер телефона']", "000000000")
        wait_and_click(driver, "//*[text()=' Продолжить ']")

        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[text()='Некорректный номер телефона']"))
        )
        if error_element.text == "Некорректный номер телефона":
            print("Тест с неправильным phone_number успешно завершен!")
            time.sleep(2)
            screenshot_path = os.path.join(SCREENSHOTS_FOLDER, "login_wrong_phone_success.png")
            driver.save_screenshot(screenshot_path)

            generate_pdf_report_single("Login Wrong Phone Success",
                                       "Passed",
                                       "The login with wrong phone has been successfully completed!",
                                       screenshot_path)
        else:
            print(f"Неверное сообщение об ошибке: {error_element.text}")
    except Exception as e:
        print(f"Ошибка во время теста с неправильным Email: {e}")
    finally:
        driver.quit()

def wait_and_send_otp(driver, otp):
    input_classes = ["one", "two", "three", "four", "five", "six"]

    try:
        for i, digit in enumerate(otp):
            input_xpath = f"//input[@class='otp-input {input_classes[i]}']"
            input_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, input_xpath))
            )
            input_element.send_keys(digit)

    except Exception as e:
        print(f"Ошибка при отправке OTP: {e}")



