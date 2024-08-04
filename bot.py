import undetected_chromedriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, os

chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Allows access to microphone/camera
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--headless")  # Run headless if you don't need a UI

driver_path = os.getcwd() + "\chromedriver.exe"

meet_url = "https://meet.google.com/orv-yoce-cpj"

print(driver_path)

driver = webdriver.Chrome(chrome_options=chrome_options)
continue_without_mic_and_cam_xpath = "/html/body/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[2]/button"
input_name_xpath = "/html/body/div/c-wiz/div/div/div[27]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[1]/div[3]/label/span[2]/input"


try:
    # Open Google Meet
    driver.get(meet_url)

    # Wait for the page to load (adjust as needed)
    time.sleep(5)

    # Click the 'Continue without mic and camera' button
    permission_button = driver.find_element(By.XPATH, continue_without_mic_and_cam_xpath)
    permission_button.click()

    time.sleep(5)
    # Enter Name as participant
    name_input = driver.find_element(By.XPATH, input_name_xpath)
    name_input.send_keys("")
    # time.sleep(2)
    print("entering name")
    name_input.send_keys("Recordify")
    name_input.send_keys(Keys.RETURN)

    # Click the 'Join now' button
    # join_button = driver.find_element_by_css_selector("button[aria-label='Join now']")
    # join_button.click()

    # Wait in the meeting (or perform other actions)
    time.sleep(3600)  # Stay for 1 hour
finally:
    driver.quit()