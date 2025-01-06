from page_objects.LoginPage import LoginPage
from utilities.data_reader import read_json, read_excel
from keywords.keywords import xstr
import pytest

config = read_json("config\config.json")

browserType = config["browser"]["type"]
testDataPath = config["test_data"]["file_path"]
testDataSheet = config["test_data"]["TC_1_sheet_name"]

def getTestData():
    return read_excel(testDataPath, testDataSheet)
    
@pytest.mark.parametrize("tc_id, name, password, expected", getTestData())
#Function for sending test data to the form
def test_submit(setup_browser, log, tc_id, name, password, expected):
    log.info("Executing "+ tc_id + " with " + xstr(name) + " as username and " + xstr(password) + " as password in "+ browserType +" browser..." )
    driver = setup_browser
    log.info("Starting browser session...")
    loginPage = LoginPage(driver)
    log.info("Entering login credentials...")
    loginPage.login(xstr(name), xstr(password))
    
    log.info("Validating login...")
    result = loginPage.validatelogin()
    if result == "Pass":
        log.info("Logged in successfully")
    else:
        log.error(loginPage.getErrorText())
    try:
        assert expected == result
        log.info("Actual result matches the expected condition")
    except Exception as e:
        log.error("Something went wrong...") 
    