from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import speechconfig as speechtext

import pathlib

import glob
import os

download_path = str(pathlib.Path().absolute()) + "\sound"
# print(download_path)

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
# options.add_argument("download.default_directory=D:/aaa")
browser = webdriver.Chrome(options=options)

browser.get(('https://eu.battle.net/account/creation/flow/create-full'))

time.sleep(3)
date =browser.find_element(By.NAME, "dob-plain")
date.click()

dob_month = browser.find_element(By.NAME, "dob-month")
dob_day = browser.find_element(By.NAME, 'dob-day')
dob_year = browser.find_element(By.NAME,'dob-year')

dob_month.send_keys(12)
dob_day.send_keys(23)
dob_year.send_keys(2000)

nextButton = browser.find_element_by_id("flow-form-submit-btn")
nextButton.click()

time.sleep(1)
firstname = browser.find_element(By.NAME, "first-name")
firstname.click()
firstname.send_keys("aaaaad")
time.sleep(3)
lastname = browser.find_element(By.NAME, 'last-name')
lastname.click()
lastname.send_keys("bbbbb")

continueButton = browser.find_element_by_id('flow-form-submit-btn')
continueButton.click()

# email = WebDriverWait(browser, 10).until(
     # EC.presence_of_element_located((By.NAME, "email")))
time.sleep(2)
email = browser.find_element(By.NAME, 'email')
email.click()
email.send_keys("elastic_chandra@xitroo.com")

continueButton = browser.find_element_by_id('flow-form-submit-btn')
continueButton.click()
time.sleep(4)
# checkboxOne = WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/form/label')))
checkboxOne = browser.find_element(By.XPATH,'//*[@id="flow-form"]/label/span[2]')
checkboxOne.click()

# checkboxTwo = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.XPATH, '//*[@id="legal-checkboxes"]')))
checkboxTwo = browser.find_element(By.XPATH,'//*[@id="legal-checkboxes"]/label/span[2]')
checkboxTwo.click()

time.sleep(2)
continueButton1 = browser.find_element_by_id('flow-form-submit-btn')
continueButton1.click()
time.sleep(4)
# iframe1 = browser.find_element_by_xpath("/html/body/div[6]/iframe")
# browser.switch_to.frame(iframe1)

# iframe2 = browser.find_element_by_id("fc-iframe-wrap")
# browser.switch_to.frame(iframe2)

# iframe3 = browser.find_element_by_id("CaptchaFrame")
# browser.switch_to.frame(iframe3)
# verifybutton = browser.find_element_by_id("home_children_button")
# verifybutton.click()

browser.switch_to.default_content()

iframe1 = browser.find_element_by_xpath("/html/body/div[6]/iframe")
browser.switch_to.frame(iframe1)
time.sleep(5)
iframe2 = browser.find_element_by_id("fc-iframe-wrap")
browser.switch_to.frame(iframe2)
time.sleep(5)

musicbutton = browser.find_element_by_css_selector("span.fc_meta_audio_btn")
musicbutton.click()

time.sleep(2)
while True:
     download_sound_btn = browser.find_element_by_id("audio_download")
     download_sound_btn.click()
     # cookies = browser.get_cookies()
     # print(cookies)
     time.sleep(4)
     list_of_files = glob.glob(download_path + '/*') # * means all if need specific format then *.csv
     latest_file = max(list_of_files, key=os.path.getctime)
     print(latest_file)
     result_text = speechtext.from_file(latest_file)
     print(result_text)
     if len(result_text)>6:
          break

print (result_text)
# time.sleep(1)
sound_text_input = browser.find_element_by_id("audio_response_field")
sound_text_input.click()
sound_text_input.send_keys(result_text)
time.sleep(1)
verifybtn = browser.find_element_by_id("audio_submit")
verifybtn.click()
time.sleep(3)
browser.switch_to.default_content()

iframe1 = browser.find_element_by_xpath("/html/body/div[6]/iframe")
browser.switch_to.frame(iframe1)
# time.sleep(4)
iframe2 = browser.find_element_by_id("fc-iframe-wrap")
print(iframe2)
# time.sleep(4)
# if iframe2:
     # change_btn = browser.find_element_by_css_selector("span.fc_meta_changeback")
change_btn = browser.find_element_by_xpath('/html/body/div[4]/span/a[3]')
change_btn.click()  

browser.switch_to.default_content()
iframe1 = browser.find_element_by_xpath("/html/body/div[6]/iframe")
browser.switch_to.frame(iframe1)

iframe2 = browser.find_element_by_id("fc-iframe-wrap")
browser.switch_to.frame(iframe2)

iframe3 = browser.find_element_by_id("CaptchaFrame")
browser.switch_to.frame(iframe3)

verifybutton = browser.find_element_by_id("home_children_button")
verifybutton.click()


        