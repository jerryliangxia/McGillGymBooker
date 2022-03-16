# from selenium import webdriver
from curses.ascii import NUL
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
actions = ActionChains(driver)


url = 'https://hnd-p-ols.spectrumng.net/mcgill/Login.aspx?isKiosk=False'
USERNAME = '260917329'
PASSWORD = 'bsb92245'
# driver downloaded from https://chromedriver.chromium.org/
DRIVER_PATH = '~/devtools/chromedriver'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(url)

try:
    login = driver.find_element_by_xpath('//*[@id="ctl00_pageContentHolder_loginControl_UserName"]').send_keys(USERNAME)
    password = driver.find_element_by_xpath('//*[@id="ctl00_pageContentHolder_loginControl_Password"]').send_keys(PASSWORD)
    submit = driver.find_element_by_xpath('//*[@id="ctl00_pageContentHolder_loginControl_Login"]').click()
except:
    print('log in unsuccessful')

time.sleep(5)
# couldn't find the XPath (For some reason)
actions.move_by_offset(245, 443).click().perform()
time.sleep(2000)


# except:
    # print("nope 3")

# driver.save_screenshot('mcgill_gym_booking.png')