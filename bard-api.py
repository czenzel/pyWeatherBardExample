from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
import time

def generate_prompt(city, state):
    return "Be sarcastic like the Carrot Weather App. Provide me the current weather conditions, 5 day forecast for " + city + ", " + state + ". Gather the data from the National Weather Service for creating the sarcastic language. Do not include images, but please use emoji."

def search_bard(web_driver, wait_driver, search_string):
    search_bar = web_driver.find_element(By.CLASS_NAME, "textarea")
    search_bar.clear()
    search_bar.send_keys(search_string)
    search_bar.send_keys(Keys.ENTER)
    wait_driver.until_not(
        EC.presence_of_element_located((By.XPATH, '//img[contains(@src, "sparkle_thinking")]'))
    )
    return web_driver.find_element(By.CLASS_NAME, "model-response-text").text

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:/Users/Christopher/AppData/Local/Google/Chrome/User Data")
options.add_argument("--headless")

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) 
wait_object = WebDriverWait(browser, 25)
browser.get("https://bard.google.com")

response = search_bard(browser, wait_object, generate_prompt("Perkasie", "PA"))

f = open("weather.txt", "w", encoding="utf8")
f.write(response)
f.close()
