from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def openBrowser(browserType, driverPath):
    if browserType == 'chrome':
        return webdriver.Chrome(driverPath)
    elif browserType == 'firefox':
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browserType == 'edge':
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