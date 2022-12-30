from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import time





username = "your_username"
password = "your_password"

html5 = "https://elearnity.gr/mod/scorm/view.php?id=12812"

cms = "https://elearnity.gr/mod/scorm/view.php?id=12795"

digimark = "https://elearnity.gr/mod/scorm/view.php?id=12796"

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    driver.get("https://elearnity.gr/course/view.php?id=1115&amp;section=3")

    # ATTENSION! If you finish the lesson you have to change to anothe by changing digimark to html5 or cms in line 35 and 77
    gotolesson(digimark)
    print('30 minutes passed!!')

def gotolesson(lesson):
    driver.get(lesson)
    sleep(1)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='scormviewform']/input[6]"))).click()
    sleep(1)
    WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//*[@id='scorm_object']")))
    sleep(1)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='content']/div/div[3]/div[2]/div[2]/div/button[2]"))).click()
    sleep(1)
    driver.switch_to.default_content()
    countdown(1800)

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://elearnity.gr/")
# driver.maximize_window()

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='CybotCookiebotDialogFooter']//div[@id='CybotCookiebotDialogBodyButtons']//div[@id='CybotCookiebotDialogBodyButtonsWrapper']//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection']"))).click()

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='eupopup-container eupopup-container-bottom eupopup-color-default']//div[@class='eupopup-buttons']//a[@class='eupopup-button eupopup-button_1']"))).click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(username)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#password"))).send_keys(password)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#loginbtn"))).submit()

driver.get("https://elearnity.gr/my")

sleep(1)

driver.get("https://elearnity.gr/course/view.php?id=1115")

sleep(1)

# ATTENSION! If you finish the lesson you have to change to anothe by changing digimark to html5 or cms in line 35 and 76
gotolesson(digimark)