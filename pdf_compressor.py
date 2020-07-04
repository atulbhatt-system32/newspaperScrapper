from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\System32\Downloads\Compressed\chromedriver_win32_2\chromedriver')
driver.get("https://www.ilovepdf.com/compress_pdf")

input_tag = "//input[starts-with(@id,'html5_')]"
inputtag1 = "//input[starts-with(@id,'uploadfiles')]"

driver.find_element_by_xpath(input_tag).send_keys(r"C:\Users\System32\Downloads\Documents\Epaper.pdf")
time.sleep(5)
print("done")   
driver.find_element_by_id('uploadfiles').click()