from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 

class AnimeOwlExtractor:
    def __init__(self, url):
        driver_s = Service("/home/mesch/prog/SeleniumDrivers/chromedriver")
        driver_s = Service("/home/mesch/programming/SeleniumDrivers/chromedriver")
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")

        driver = webdriver.Chrome(service=driver_s, options=options)
        stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
        
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-play"))).click()
        video_player = driver.find_element(By.XPATH, "//video[@contains(@src, 'monkey-d-luffy.site')]")

        

    def videoSource(self):
        return self.video_sources[-1]["manifest_url"]

    def subtitleSource(self, lang="en-US"):
        return None