#!/bin/bash
set -e

echo "=== 🚀 Appium Android Setup Script ==="

### 1. Check Required Tools ###
command -v adb >/dev/null 2>&1 || { echo "❌ adb not found. Please install Android SDK Platform Tools"; exit 1; }
command -v node >/dev/null 2>&1 || { echo "❌ Node.js not found. Please install Node.js"; exit 1; }
command -v pip >/dev/null 2>&1 || { echo "❌ pip not found. Please install Python3"; exit 1; }

### 2. Install Appium and Drivers ###
echo "🔧 Installing Appium..."
npm install -g appium@latest

echo "🔧 Installing UiAutomator2 driver..."
appium driver install uiautomator2

echo "🔧 Installing Python Appium Client..."
pip install --upgrade Appium-Python-Client

### 3. Check Android Device ###
echo "📱 Checking Android device..."
adb start-server
DEVICE_ID=$(adb devices | awk 'NR==2 {print $1}')
if [ -z "$DEVICE_ID" ] || [ "$DEVICE_ID" == "unauthorized" ]; then
    echo "❌ No authorized Android device found. Please enable USB debugging."
    exit 1
fi
echo "✅ Found device: $DEVICE_ID"

### 4. Get Android Version ###
PLATFORM_VERSION=$(adb -s $DEVICE_ID shell getprop ro.build.version.release | tr -d '\r')
echo "✅ Android version: $PLATFORM_VERSION"

### 5. Start Appium Server (Background) ###
echo "🚀 Starting Appium server..."
appium --base-path /wd/hub --port 4723 > appium.log 2>&1 &
APP_PID=$!
sleep 5

### 6. Create Python Test Script ###
cat > quick_test.py <<EOL
from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "platformVersion": "${PLATFORM_VERSION}",
    "deviceName": "${DEVICE_ID}",
    "automationName": "UiAutomator2",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings"
}

print("🚀 Connecting to Appium...")
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

print("✅ Opened Android Settings app!")
driver.quit()
EOL

### 7. Run Test ###
echo "▶️ Running quick test..."
python3 quick_test.py

### 8. Stop Appium Server ###
echo "🛑 Stopping Appium..."
kill $APP_PID
echo "🎉 Done!"
