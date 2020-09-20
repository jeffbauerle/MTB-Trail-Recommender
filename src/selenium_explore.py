import time
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

domain = 'https://www.mtbproject.com/trail/'
lst = ['338027']
def get_docs(lst):
        # ds = DirectoryAssistor()
        for value in lst:
            driver = webdriver.Chrome()
            driver.get(domain+value)
            # driver.get('https://www.mtbproject.com/trail/4670265/')
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="user"]/a').click()
            time.sleep(1)
            elem = driver.find_element_by_xpath('//input[@placeholder="Log in with email"]')
            elem.click()
            elem.clear()
            elem.send_keys("jeffbauerle@gmail.com")
            pw = driver.find_element_by_xpath('//input[@placeholder="Password"]')
            pw.click()
            pw.clear()
            pw.send_keys("1L0v3mtb!")
            pw.send_keys(Keys.RETURN)
            time.sleep(1)
            dl = driver.find_element_by_xpath('//*[@id="toolbox"]/a[3]').click() 
            time.sleep(1)
            driver.quit()
get_docs(lst)