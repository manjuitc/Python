from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://www.surveymonkey.com/")
driver.find_element_by_link_text("Sign Up Free").click()
driver.find_element_by_id("username").send_keys("sampleqwe1")
driver.find_element_by_id("password").send_keys("sample123")
driver.find_element_by_id("password_confirm").send_keys("sample123")
driver.find_element_by_id("email").send_keys("sample.test212@gmail.com")
driver.find_element_by_id("submitform").click()
driver.quit()

