from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
import random
import sys
from datetime import datetime

caps = {
    "platformName": "Android",
    "platformVersion": "12",
    "deviceName": "8BWX1GLZ0",
    "automationName": "UiAutomator2",
    "appPackage": "com.huanuage.skytube",
    "appActivity": ".MainActivity",
    "noReset": True,
}

options = UiAutomator2Options().load_capabilities(caps)

# Check command line argument for random delay
add_random_delay = False
if len(sys.argv) > 1:
    delay_arg = sys.argv[1].lower().strip()
    if delay_arg in ['y', 'yes', '1', 'true']:
        add_random_delay = True

if add_random_delay:
    # Random delay between 0-500 seconds
    random_delay = random.randint(0, 500)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ⏰ Will wait {random_delay} seconds before starting...")
    time.sleep(random_delay)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✅ Wait completed, starting script execution!")

print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 🚀 Connecting to Appium...")
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✅ Opened Android HR app!")

# delay 7 seconds
time.sleep(7)

# starting check in
el = driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().className("android.widget.ImageView").index(5)'
)
el.click()

# delay 3 seconds
time.sleep(3)

el = driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().className("android.widget.EditText").index(1)'
)
el.click()
el.clear()
el.send_keys("wfh")

driver.hide_keyboard()

# delay 3 seconds
time.sleep(3)

def safe_click(by, value):
    try:
        el = driver.find_element(by, value)
        el.click()
        return True
    except:
        return False

safe_click("accessibility id", "上班")
safe_click("accessibility id", "下班")

print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✅ Successfully checked in!")

# delay 5 seconds
time.sleep(5)

driver.quit()
