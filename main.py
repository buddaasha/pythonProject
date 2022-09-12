from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
element = driver.find_element(By.NAME, "q")
element.clear()
element.send.keys("pycon")
element.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()



