import os

from appium import webdriver

IMPLICIT_TIMEOUT = 10


def test_bug_demo():
    desired_caps = {}
    desired_caps["app"] = os.path.realpath("../tested_app/dist/demo/demo.exe")  # use real path to handle even relative paths
    desired_caps["ms:experimental-webdriver"] = False
    desired_caps["ms:waitForAppLaunch"] = 20
    desired_caps["createSessionTimeout"] = 50000
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        desired_capabilities=desired_caps)
    driver.implicitly_wait(IMPLICIT_TIMEOUT)
    driver.save_screenshot(f"app_screenshot.png")
    elms = driver.find_elements_by_xpath("//*")
    with open("elements_report.txt", 'w', encoding='utf-8') as f:
        f.write(f"Window handles: {driver.window_handles}\n")
        f.write(f"Amount of elements found: {len(elms)}\n")
        for elm in elms:
            f.write(f'Element name: {elm.get_attribute("Name")} |  automation id: {elm.get_attribute("AutomationId")}\n')
        f.write("Page_source:\n")
        f.write(driver.page_source)
    driver.find_element_by_accessibility_id("MainWindow.centralwidget.pushButton").click()
    driver.close_app()
    driver.quit()
