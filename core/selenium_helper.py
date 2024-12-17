import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_drive():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-extensions")
    #если хочешь увидеть как у тебя открывается chrome, то отключи headless
    #chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://client.bigplay.gg")
    return driver

def wait_and_click(driver, xpath, retries=5):
    attempt = 0
    while attempt < retries:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
            return
        except Exception as e:
            print(f"Попытка {attempt + 1} не удалась: {e}")
            time.sleep(1)
            attempt += 1
    raise Exception(f"Не удалось кликнуть на элемент: {xpath}")

def wait_and_send_keys(driver, xpath, keys, find_by_label=False):
    if find_by_label:
        label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        input_element = label.find_element(By.XPATH, ".//following::input[1] | .//following::textarea[1]")
    else:
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    input_element.send_keys(keys)
    driver.execute_script("arguments[0].blur();", input_element)

def switch_to_new_window(driver, timeout=10):
    main_window = driver.current_window_handle

    WebDriverWait(driver, timeout).until(EC.new_window_is_opened)

    all_windows = driver.window_handles
    new_window = [window for window in all_windows if window != main_window][0]
    driver.switch_to.window(new_window)

def login_in_system(driver):
    try:
        wait_and_click(driver, "//*[text()='Войти']")
        wait_and_click_if_condition(driver, "//*[text()=' Почта ']", "!bg-[#E4E4E4]", "!bg-white")
        wait_and_send_keys(driver, "//input[@placeholder='Введите свою почту']", "autotest@test.test")
        wait_and_click(driver, "//*[text()=' Продолжить ']")
        wait_and_send_keys(driver, "//input[@placeholder='Введите пароль']", "password")
        wait_and_click(driver, "//*[text()=' Войти ']")
    except Exception as e:
        print(f"Ошибка во время авторизации: {e}")

def click_random_tournament(driver):
    try:
        tournaments = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//*[contains(text(), 'Дисциплина')]")
            )
        )
        if tournaments:
            random_tournament = random.choice(tournaments)

            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", random_tournament)
            driver.execute_script("arguments[0].click();", random_tournament)
            time.sleep(4)
        else:
            raise Exception(f"Не найдено турниров с дисциплиной.")
    except Exception as e:
        print(f"Ошибка при клике на случайный турнир: {e}")

def click_random_blog(driver):
    try:
        blogs = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[contains(@class, 'content-wrapper') and .//img[contains(@src, '/post-like.svg')]]")
            )
        )
    except:
        print("Не удалось найти блоги по 'content-wrapper'. Пробуем искать только по 'post-like.svg'.")
        blogs = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//img[contains(@src, '/post-like.svg')]")
            )
        )

    if blogs:
        random_blog = random.choice(blogs)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", random_blog)
        driver.execute_script("arguments[0].click();", random_blog)
        time.sleep(4)
        print("Успешно кликнул по блогу.")
    else:
        print("Не найдено блогов.")

def wait_and_click_if_condition(driver, xpath, check_class, target_class):
    try:
        element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element_class = element.get_attribute("class")
        if check_class not in element_class and target_class in element_class:
            element.click()
    except Exception as e:
        print(f"Ошибка при проверке и клике элемента: {e}")



