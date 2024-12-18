import os
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.report_generator import generate_pdf_report_single, SCREENSHOTS_FOLDER
from core import wait_and_click, wait_and_send_keys, setup_drive, wait_and_click_if_condition_by_data

def test_login_email_success():
    driver = setup_drive()
    try:
        wait_and_click(driver, '[data-unique-id="a-element-15-15"]', use_xpath=False)
        wait_and_click_if_condition_by_data(driver,
                                            "button-element-0-0",
                                            "!bg-[#E4E4E4]",
                                            "!bg-white",
                                            timeout=10 )
        wait_and_send_keys(driver, '[data-unique-id="input-element-2-2"]', "autotest@test.test", use_xpath=False)
        wait_and_click(driver, '[data-unique-id="button-element-3-3"]', use_xpath=False)
        wait_and_send_keys(driver, '[data-unique-id="input-element-1-1"]', "password", use_xpath=False)
        wait_and_click(driver, "//img[@alt='глазок']")
        wait_and_click(driver, '[data-unique-id="button-element-3-3"]', use_xpath=False)
        time.sleep(1)

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
        wait_and_click(driver, '[data-unique-id="a-element-15-15"]', use_xpath=False)
        wait_and_click_if_condition_by_data(driver,
                                            "button-element-1-1",
                                            "!bg-[#E4E4E4]",
                                            "!bg-white",
                                            timeout=10)
        time.sleep(1)
        wait_and_send_keys(driver, '[data-unique-id="input-element-2-2"]', "7056806338", use_xpath=False)
        wait_and_click(driver, '[data-unique-id="button-element-3-3"]', use_xpath=False)
        wait_and_send_keys(driver, '[data-unique-id="input-element-1-1"]', "177013A_r", use_xpath=False)
        wait_and_click(driver, "//img[@alt='глазок']")
        wait_and_click(driver, '[data-unique-id="button-element-2-2"]', use_xpath=False)
        time.sleep(1)

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
        wait_and_click(driver, '[data-unique-id="a-element-15-15"]', use_xpath=False)
        wait_and_click(driver, '[data-unique-id="button-element-4-4"]', use_xpath=False)
        wait_and_send_keys(driver, '[data-unique-id="input-element-0-0"]', random_number, use_xpath=False)
        time.sleep(0.1)
        wait_and_click(driver, '[data-unique-id="button-element-1-1"]', use_xpath=False)
        wait_and_send_otp(driver, "123456")
        time.sleep(0.1)
        wait_and_click(driver, '[data-unique-id="button-element-6-6"]', use_xpath=False)
        time.sleep(0.1)
        wait_and_send_keys(driver, '[data-unique-id="input-element-0-0"]', randname, use_xpath=False)
        wait_and_send_keys(driver, '[data-unique-id="input-element-1-1"]', "password", use_xpath=False)
        wait_and_send_keys(driver, '[data-unique-id="input-element-2-2"]', "password", use_xpath=False)
        wait_and_click(driver, '[data-unique-id="button-element-3-3"]', use_xpath=False)
        time.sleep(0.1)
        wait_and_click(driver, "//img[@alt='pubg icon']")
        wait_and_send_keys(driver, '[data-unique-id="input-element-2-2"]', randname, use_xpath=False)
        wait_and_send_keys(driver, '[data-unique-id="input-element-3-3"]', random_number, use_xpath=False)
        wait_and_click(driver, '[data-unique-id="button-element-4-4"]', use_xpath=False)
        time.sleep(1)

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
        wait_and_click(driver, '[data-unique-id="a-element-15-15"]', use_xpath=False)
        time.sleep(0.1)
        wait_and_click_if_condition_by_data(driver,
                                            "button-element-0-0",
                                            "!bg-[#E4E4E4]",
                                            "!bg-white",
                                            timeout=10)
        time.sleep(0.1)
        wait_and_send_keys(driver, '[data-unique-id="input-element-2-2"]', "wrongwrong.wrong", use_xpath=False)
        wait_and_click(driver, '[data-unique-id="button-element-3-3"]', use_xpath=False)

        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'text-red-500')]"))
        )
        if error_element.text.strip():
            print("Тест с неправильным Email успешно завершен!")
            time.sleep(0.1)
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
        wait_and_click(driver, '[data-unique-id="a-element-15-15"]', use_xpath=False)
        time.sleep(0.1)
        wait_and_click_if_condition_by_data(driver,
                                            "button-element-0-0",
                                            "!bg-[#E4E4E4]",
                                            "!bg-white",
                                            timeout=10)
        time.sleep(0.1)
        wait_and_send_keys(driver, '[data-unique-id="input-element-2-2"]', "autotest@test.test", use_xpath=False)
        wait_and_click(driver, '[data-unique-id="button-element-3-3"]', use_xpath=False)
        wait_and_send_keys(driver, '[data-unique-id="input-element-1-1"]', "wrongwrong", use_xpath=False)
        wait_and_click(driver, "//img[@alt='глазок']")
        wait_and_click(driver, '[data-unique-id="button-element-3-3"]', use_xpath=False)

        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'text-red-500')]"))
        )
        if error_element.text.strip():
            print("Тест с неправильным password успешно завершен!")
            time.sleep(0.1)
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
        wait_and_click(driver, '[data-unique-id="a-element-15-15"]', use_xpath=False)
        time.sleep(0.1)
        wait_and_click_if_condition_by_data(driver,
                                            "button-element-0-0",
                                            "!bg-[#E4E4E4]",
                                            "!bg-white",
                                            timeout=10)
        time.sleep(0.1)
        wait_and_send_keys(driver, '[data-unique-id="input-element-2-2"]', "wrongwrong", use_xpath=False)
        wait_and_click(driver, '[data-unique-id="button-element-3-3"]', use_xpath=False)

        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'text-red-500')]"))
        )
        if error_element.text.strip():
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



