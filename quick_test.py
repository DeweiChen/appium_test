from appium import webdriver
from appium.options.android import UiAutomator2Options

caps = {
    "platformName": "Android",
    "platformVersion": "12",
    "deviceName": "8BWX1GLZ0",
    "automationName": "UiAutomator2",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings"
}

options = UiAutomator2Options().load_capabilities(caps)

print("🚀 Connecting to Appium...")
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

print("✅ Opened Android Settings app!")
driver.quit()
