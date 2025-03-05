from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium_flutter_finder import FlutterFinder

# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
options = UiAutomator2Options().load_capabilities({
    # Specify device and os_version for testing
    "platformName" : "android",
    "platformVersion" : "9.0",
    "deviceName" : "Google Pixel 3"

    # Add your caps here
})

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

# Test case for the BrowserStack sample Android app.
# If you have uploaded your app, update the test case here.
finder = FlutterFinder()

driver.execute_script('flutter:clearTimeline')
driver.execute_script('flutter:forceGC')
assert driver.execute_script('flutter:checkHealth') == 'ok'

driver.execute_script(
    'browserstack_executor: {"action": "cameraImageInjection", "arguments": {"imageUrl":"media://14fe3b03ca2bf608b1325b2b8522e7cf8d7dd984"}}'
)
time.sleep(6)

# gesture_detector = finder.by_type("GestureDetector")
# container = finder.by_type("Container")
# element = driver.find_element(gesture_detector)
# element.click()
# time.sleep(10)
#
# driver.switch_to.context("NATIVE_APP")
# camera_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@content-desc="CameraBtn"]'))
# )
# camera_button.click()

time.sleep(4)
driver.quit()

