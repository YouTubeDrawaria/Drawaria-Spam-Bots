from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import threading

# WebDriver configuration
chrome_driver_path = r'C:\SeleniumDrivers\chromedriver.exe'
service = Service(chrome_driver_path)

# URL of the page
url = 'https://drawaria.online/'

# Function to set up the browser
def setup_browser():
    options = webdriver.ChromeOptions()
    # Disable headless mode for debugging
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=500,500")  # Custom window size
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    return driver

# Function to change the bot's name using JavaScript
def change_name(driver):
    try:
        script = """
        var nameInput = document.getElementById('playername');
        nameInput.value = '𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫';  # You will manually set the name here
        var event = new Event('input', { bubbles: true });
        nameInput.dispatchEvent(event);
        """
        driver.execute_script(script)
        print("Name changed successfully.")
    except Exception as e:
        print(f"Error changing name: {e}")

# Function to join the room using JavaScript
def join_room(driver):
    try:
        script = """
        var joinButton = document.getElementById('quickplay');
        joinButton.click();
        """
        driver.execute_script(script)
        print("Joined the room successfully.")
    except Exception as e:
        print(f"Error joining the room: {e}")

# Function to send messages in the chat using JavaScript
def send_messages(driver):
    while True:
        try:
            script = """
            var chatInput = document.getElementById('chatbox_textinput');
            chatInput.value = '𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫';  # You will manually set the message here
            var event = new Event('input', { bubbles: true });
            chatInput.dispatchEvent(event);
            chatInput.dispatchEvent(new KeyboardEvent('keydown', {'key': 'Enter', 'code': 'Enter', 'keyCode': 13, 'bubbles': true}));
            """
            driver.execute_script(script)
            print("Message sent.")
            time.sleep(1.2)  # Interval of 800ms
        except Exception as e:
            print(f"Error sending message: {e}")
            time.sleep(1)  # Wait one second before retrying

# Function to execute the bot's actions
def run_bot():
    driver = setup_browser()
    change_name(driver)
    join_room(driver)
    send_messages(driver)

# Create threads to run the bots
num_bots = 3
threads = []
for _ in range(num_bots):
    thread = threading.Thread(target=run_bot)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish (although in this case they won't finish)
for thread in threads:
    thread.join()
