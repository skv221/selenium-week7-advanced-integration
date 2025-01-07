from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.firefox.options import Options as firefoxOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as edgeService
from selenium.webdriver.edge.options import Options as edgeOptions

def openBrowser(browserType, driverPath, isHeadless):
    if browserType == 'chrome':
        if isHeadless:
            chrome_options = chromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            return webdriver.Chrome(driverPath, options = chrome_options)
        else:
            return webdriver.Chrome(driverPath)
    elif browserType == 'firefox':
        if isHeadless:
            firefox_options = firefoxOptions()
            firefox_options.add_argument("--headless")
            firefox_options.add_argument("--disable-gpu")
            firefox_options.add_argument("--window-size=1920,1080")
            firefox_options.add_argument("--no-sandbox")
            firefox_options.add_argument("--disable-dev-shm-usage")
            return webdriver.Firefox(service = firefoxService(GeckoDriverManager().install()), options = firefox_options)
        else:     
            return webdriver.Firefox(executable_path = GeckoDriverManager().install())
    elif browserType == 'edge':
        if isHeadless:
            edge_options = edgeOptions()
            edge_options.add_argument("--headless")
            edge_options.add_argument("--disable-gpu")
            edge_options.add_argument("--window-size=1920,1080")
            edge_options.add_argument("--no-sandbox")
            edge_options.add_argument("--disable-dev-shm-usage")
            return webdriver.Edge(service = edgeService(EdgeChromiumDriverManager().install()), options = edge_options)
        else:
            return webdriver.Edge(EdgeChromiumDriverManager().install())

def navigateTo(driver, url, waitTime):
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(waitTime)
    
def killBrowser(driver):
    driver.quit()
    
def xstr(s):
    return '' if s is None else str(s)

def buttonId(s):
    return s.lower().replace(" ","-")