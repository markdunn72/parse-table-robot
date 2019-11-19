from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import pandas as pd


# Start fresh browser (used for testing purposes) 
options = Options()
options.add_argument("--headless")
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# unix binaries: /usr/bin/google-chrome /usr/bin/chromedriver
chrome_driver_binary = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, options=options)

def get_table_contents():
  # Use robot framework browser
  # from robot.libraries.BuiltIn import BuiltIn
  # seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
  # driver = seleniumlib.driver

  driver.get("https://www.w3schools.com/html/html_tables.asp")

  tbl = driver.find_element_by_xpath('//table[@id="customers"]').get_attribute('outerHTML')

  df  = pd.read_html(tbl)
  tbl_data = df[0].values.tolist() 
  print([row[0] for row in tbl_data])
  return df

if __name__ == "__main__":
  get_table_contents()

# Integrate Into Robot Framework:
'''
*** Settings ***
Library parsehtmltable
# Library  ./parsehtml.py

*** Test Cases ***
Parse Table
    ${table_contents}=  Get Table Contents
    Log To Console  \n\n\t\t table_contents\n
'''
