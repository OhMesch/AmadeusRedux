import json
from time import sleep

from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 

def crunchyrollLogIn():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(driver.find_element(By.CLASS_NAME, "erc-anonymous-user-menu"))).click()
    # https://stackoverflow.com/questions/3655549/xpath-containstext-some-string-doesnt-work-when-used-with-node-with-more
    driver.find_element(By.XPATH, "//*[text()[contains(., 'Log In')]]").click()
    userField = driver.find_element(By.XPATH, "//input[@name='username']")
    passField = driver.find_element(By.XPATH, "//input[@name='password']")
    userField.send_keys("xeno43")
    passField.send_keys("bubbles")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()


driver_s = Service("/home/mesch/prog/SeleniumDrivers/chromedriver")
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation", "disable-default-apps"])
options.add_experimental_option('useAutomationExtension', False)
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
options.add_experimental_option('prefs', prefs)


# options.add_argument('headless')
caps = caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(service=driver_s, options=options, desired_capabilities=caps)
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
)
# driver.get("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi7oNjD1-_8AhVYlYkEHXMyBxQQFnoECAgQAQ&url=https%3A%2F%2Fwww.crunchyroll.com%2Flogin&usg=AOvVaw32-w0UF00XxGHVsSGPReTp")
driver.get("https://www.crunchyroll.com/")
crunchyrollLogIn()
driver.get('https://www.crunchyroll.com/watch/GJWU23994/dream')
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "video-player"))).click()
castAction = ActionChains(driver)
castAction.send_keys(Keys.HOME)
castAction.move_to_element(driver.find_element(By.CLASS_NAME, "video-player"))
castAction.context_click()
castAction.context_click()
castAction.send_keys(Keys.ARROW_DOWN)
castAction.send_keys(Keys.ARROW_DOWN)
castAction.send_keys(Keys.ARROW_DOWN)
castAction.send_keys(Keys.ARROW_DOWN)
castAction.send_keys(Keys.ARROW_DOWN)
castAction.send_keys(Keys.ENTER)
castAction.perform()

browser_log = driver.get_log('performance')
driver.quit()
def process_browser_log_entry(entry):
    response = json.loads(entry['message'])['message']
    return response
events = [process_browser_log_entry(entry) for entry in browser_log]
events = [event for event in events if 'Network.response' in event['method']]
print("done")