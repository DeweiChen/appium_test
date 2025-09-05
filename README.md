# Appium Android Automation Testing Project

This is a project for Android application automation testing using Appium, with main features including automatic check-in and basic testing.

## 📋 Project Overview

- **Main Features**: Android application automation testing
- **Core Script**: Automatic check-in functionality (`auto_check_in.py`)
- **Test Script**: Quick connection test (`quick_test.py`)
- **Environment Setup**: Automated installation script (`setup_appium.sh`)

## 🛠️ Environment Requirements

### Required Software
- **Python 3.x** - Execute test scripts
- **Node.js** - Install Appium
- **Android SDK Platform Tools** - Includes adb tool
- **Java Development Kit (JDK)** - Appium runtime requirement

### Hardware Requirements
- **Android Device** - Connected and USB debugging enabled
- **USB Cable** - Connect Android device to computer

## 📱 Android Device Setup

### 1. Enable Developer Options
1. Go to `Settings` > `About Phone`
2. Tap `Build Number` 7 times continuously
3. Return to settings homepage, find `Developer Options`

### 2. Enable USB Debugging
1. Enter `Developer Options`
2. Turn on `USB Debugging`
3. Turn on `USB Installation` (optional, for APK installation)

### 3. Connect Device
1. Connect Android device to computer using USB cable
2. Allow USB debugging authorization on device
3. Confirm device is properly connected:
   ```bash
   adb devices
   ```

## 🚀 Quick Start

### Method 1: Using Automated Installation Script (Recommended)

```bash
# Grant execution permission
chmod +x setup_appium.sh

# Execute installation script
./setup_appium.sh
```

This script will automatically:
- Check if required tools are installed
- Install Appium and UiAutomator2 driver
- Install Python Appium client
- Detect Android device
- Start Appium server
- Execute quick test

### Method 2: Manual Installation

#### 1. Install Appium
```bash
# Install Appium
npm install -g appium@latest

# Install UiAutomator2 driver
appium driver install uiautomator2
```

#### 2. Install Python Dependencies
```bash
pip install --upgrade Appium-Python-Client
```

#### 3. Start Appium Server
```bash
appium --base-path /wd/hub --port 4723
```

## 📝 Usage Instructions

### Quick Test
```bash
python3 quick_test.py
```
This script will open the Android Settings application to verify Appium connection is working properly.

### Automatic Check-in
```bash
# Basic execution
python3 auto_check_in.py

# Execute with random delay (0-500 seconds)
python3 auto_check_in.py yes
```

**Note**: Before use, please confirm:
- Target application (`com.huanuage.skytube`) is installed on device
- Device is properly connected and authorized
- Appium server is running

## ⚙️ Configuration Instructions

### Device Configuration
Modify the following parameters in the script to match your device:

```python
caps = {
    "platformName": "Android",
    "platformVersion": "12",        # Your Android version
    "deviceName": "xxxxxxxxxx",      # Your device ID
    "automationName": "UiAutomator2",
    "appPackage": "com.huanuage.skytube",  # Target application package name
    "appActivity": ".MainActivity",         # Main activity
    "noReset": True,
}
```

## 🔧 Troubleshooting

### Common Issues

1. **Device Not Found**
   - Confirm USB debugging is enabled
   - Reconnect USB cable
   - Check device authorization status

2. **Appium Connection Failed**
   - Confirm Appium server is running
   - Check if port 4723 is occupied
   - Restart Appium server

3. **Application Cannot Open**
   - Confirm application is installed
   - Check if package name and activity name are correct
   - Try opening application manually

### Log Files
- `appium.log` - Appium server logs
- `log.txt` - Test execution logs

## 📁 Project Structure

```
appium-test/
├── README.md              # Project documentation
├── setup_appium.sh        # Automated installation script
├── auto_check_in.py       # Automatic check-in script
├── quick_test.py          # Quick test script
├── appium.log            # Appium server logs
└── log.txt               # Test execution logs
```

## 🤝 Contributing

Welcome to submit Issues and Pull Requests to improve this project.

## 📄 License

This project is licensed under the MIT License.

### MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.