import platform
from selenium import webdriver


def initialize_browser(context):
    # Initialize WebDriver
    context.driver = webdriver.Chrome(
        executable_path=return_path_chrome_driver_by_os_type())
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def close_browser(context):
    context.driver.close()


def return_path_chrome_driver_by_os_type():
    type_os = platform.system().lower()
    match type_os:
        case "windows":
            return "././Drivers/win32/chromedriver.exe"
        case "linux":
            return "././Drivers/linux/chromedriver"
        case "darwin":
            return "././Drivers/mac64/chromedriver"

