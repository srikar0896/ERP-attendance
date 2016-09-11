from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import argparse
import sys
import itertools
from queue import Queue
import threading
import os
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-u" , help = "Please Enter the username")
parser.add_argument("-p" , help = "Please enter the name hints separated by comma")
args = parser.parse_args()
userId = args.u
password = args.p

driver = webdriver.PhantomJS()
start_time = time.time()
driver.get("https://nucleus.niituniversity.in")
emailFieldID = ".//*[@id='SchSel_txtUserName']"
passFieldID = ".//*[@id='SchSel_txtPassword']"
loginButtonXPath = ".//*[@id='SchSel_btnLogin']"
attendance = ".//a[@id='hyplnkProfile']"
#flLogoXpath = ".//*[@id='divUpper']/table/tbody/tr/td/table/tbody/tr[1]/td/u"
emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(emailFieldID))
passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(passFieldID))
loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXPath))
try:
    emailFieldElement.click()
    emailFieldElement.clear()
    emailFieldElement.send_keys(userId)
    passFieldElement.click()
    passFieldElement.clear()
    passFieldElement.send_keys(password)
    loginButtonElement.click()
    #time.sleep(2)
    driver.get("https://nucleus.niituniversity.in/WebApp/StudParentDashBoard/Attendance.aspx")
    #time.sleep(5)
    sessionElement = driver.find_element_by_xpath(".//*[@id='ddlSession']")
    for option in sessionElement.find_elements_by_tag_name('option'):
        if option.text == '2016-2017':
            option.click() # select() in earlier versions of webdriver
            break
    fromDateElement = driver.find_element_by_xpath(".//*[@id='ctl00_ContentPlaceHolder1_wdcFromDate_img']")
    fromDateElement.click()
    sideArrow = driver.find_element_by_xpath(".//*[@id='ctl00_ContentPlaceHolder1_wdcFromDate_DrpPnl1_DP_CAL_ID_1_500']")
    sideArrow.click()
    selectDateElement = driver.find_element_by_xpath(".//*[@calid='ctl00_ContentPlaceHolder1_wdcFromDate_DrpPnl1_DP_CAL_ID_1']/tbody/tr[2]/td/table/tbody/tr[2]/td[2]")
    selectDateElement.click()
    patternElement = driver.find_element_by_xpath(".//*[@id='ddlPattern']")
    patternElement.click()
    driver.find_element_by_xpath(".//*[@id='ddlPattern']/option[2]").click()
    driver.find_element_by_xpath(".//*[@id='ctl00_ContentPlaceHolder1_Button1']").click()
    #rows = driver.find_element_by_xpath("//*[contains(@id,'oReportCell')]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td[1]")
    resultSet = {}
    for i in range(3,9):
        for j in range(1,9):
            if (j == 1 or j == 8):
                    print(str(driver.find_element_by_xpath("//*[contains(@id,'oReportCell')]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr["+ str(i) +"]/td[" + str(j) + "]").text))

    driver.save_screenshot("log.png")

    print("\n    Time Executed - " + str(time.time() - start_time))
except Exception as e:
    print(str(e))
    print("Please Check the password!!")
driver.quit()
