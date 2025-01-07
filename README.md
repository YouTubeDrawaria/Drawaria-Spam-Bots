# Drawaria Spam Bots

This project is a collection of automated bots designed to interact with the online drawing and guessing game [Drawaria](https://drawaria.online/). The bots can automatically join rooms, change their names, and spam messages in the chat. This project is intended for educational purposes and fun experimentation.

---

## Features
- **Automated Room Joining:** Bots can automatically join a room in Drawaria.
- **Custom Name:** Bots can change their displayed name using special characters.
- **Chat Spamming:** Bots can send repeated messages in the chat at a specified interval.
- **Multi-Bot Support:** Run multiple bots simultaneously using threading.

---

## Requirements
- Python 3.x
- Selenium
- ChromeDriver (matching your Chrome browser version)

---

## Installation
1. **Install Python:** Ensure Python 3.x is installed on your system.
2. **Install Selenium:** Install the Selenium package using pip:
   ```bash
   pip install selenium
   ```
3. **Download ChromeDriver:** Download the appropriate version of ChromeDriver from [here](https://sites.google.com/chromium.org/driver/) and place it in a known directory (e.g., `C:\SeleniumDrivers\chromedriver.exe`).

---

## Usage
1. Clone this repository or download the script.
2. Update the `chrome_driver_path` variable in the script to point to your ChromeDriver location.
3. Run the script:
   ```bash
   python drawaria_spam_bots.py
   ```
4. The bots will automatically open Chrome windows, join a Drawaria room, and start spamming messages.

---

## Configuration
- **Number of Bots:** Adjust the `num_bots` variable to control how many bots are running simultaneously.
- **Message Interval:** Modify the `time.sleep(1.2)` value in the `send_messages` function to change the delay between messages.
- **Custom Name/Message:** Update the JavaScript scripts in the `change_name` and `send_messages` functions to set custom names and messages.

---

## Example
```python
# Change the bot's name
script = """
var nameInput = document.getElementById('playername');
nameInput.value = '𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫';
var event = new Event('input', { bubbles: true });
nameInput.dispatchEvent(event);
"""
driver.execute_script(script)
```

---

## Notes
- **Headless Mode:** To run the bots without opening browser windows, uncomment the `options.add_argument("--headless")` line in the `setup_browser` function.
- **Error Handling:** The script includes basic error handling to ensure the bots continue running even if an error occurs.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

**Use responsibly and have fun!** 🎨🤖