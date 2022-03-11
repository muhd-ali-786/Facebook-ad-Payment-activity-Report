import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import pandas as pd
from pathlib import Path
import requests
import shutil
import math
import csv
import re
import datetime
import sys

def get_profile_path(profile):
    FF_PROFILE_PATH = os.path.join(os.environ['APPDATA'],'Mozilla', 'Firefox', 'Profiles')

    try:
        profiles = os.listdir(FF_PROFILE_PATH)
    except WindowsError:
        print("Could not find profiles directory.")
        sys.exit(1)
    try:
        for folder in profiles:
            print(folder)
            if folder.endswith(profile):
                loc = folder
    except StopIteration:
        print("Firefox profile not found.")
        sys.exit(1)
    return os.path.join(FF_PROFILE_PATH, loc)



url="https://business.facebook.com/ads/manager/billing_history/summary/?act=1414159818809635&pid=p1&business_id=154450331977816&global_scope_id=154450331977816&page=billing_history";
download_path_root = # Report Download Root Path Here


file_path= # Report Folder Name

prof = # Firefox Profile name i.e: abcxyz.default-release

mime_types = "text/csv,text/html"
profile = webdriver.FirefoxProfile(get_profile_path(prof))
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", os.path.join(download_path_root, file_path))
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
profile.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)


driver = webdriver.Firefox(firefox_profile=profile)
driver.get(url)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div[3]/div").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/label[8]/div/div").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/div").click()
time.sleep(2)


try:
    dwn_btn =driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[3]/div/a")

    for root, dirs, files in os.walk(download_path_root+"\\"+file_path):
        for file in files:
            os.remove(os.path.join(root, file))

    dwn_btn.click()
    time.sleep(10)
    driver.quit()

except:
    print("excepted part")
    driver.quit()
