from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# To not prevent the window from closing
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # article_count.click()
# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# # all_portals.click()
search = driver.find_element(By.NAME, 'search')

search.send_keys('Python')
search.send_keys(Keys.ENTER)