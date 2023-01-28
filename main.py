# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import os
import whisper
import warnings
warnings.filterwarnings("ignore")

model = whisper.load_model("base")

def transcribe(url):
    with open('.temp', 'wb') as f:
        f.write(requests.get(url).content)
    result = model.transcribe('.temp')
    return result["text"].strip()

def click_checkbox(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']"))
    driver.find_element(By.ID, "recaptcha-anchor-label").click()
    driver.switch_to.default_content()

def request_audio_version(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='recaptcha challenge expires in two minutes']"))
    driver.find_element(By.ID, "recaptcha-audio-button").click()

def solve_audio_captcha(driver):
    text = transcribe(driver.find_element(By.ID, "audio-source").get_attribute('src'))
    driver.find_element(By.ID, "audio-response").send_keys(text)
    driver.find_element(By.ID, "recaptcha-verify-button").click()
    time.sleep(2)
    driver.find_element_by_link_text(" Claim Now").click()

def logic(driver):
    user = "FajarTM"
    passe = "@Santuy16"
    driver.get('https://cryptowin.io/login')
    driver.find_element(By.ID, "username").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(passe)
    time.sleep(3)
    driver.find_element_by_link_text("Faucet").click()
    time.sleep(3)
    driver.find_element_by_link_text(" Get Reward").click()
    driver.find_element_by_link_text("Change CAPTCHA ").click()
    driver.find_element_by_link_text("reCAPTCHA").click()

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
    )

    logic(driver)
    time.sleep(2)
    click_checkbox(driver)
    time.sleep(2)
    request_audio_version(driver)
    time.sleep(2)
    solve_audio_captcha(driver)
    time.sleep(15)
