# Selenium Web Driver
# This helps us to perform anything a normal human being can do in the browser
# Automation of filling in forms
# Best use Chrome browser
from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome()
driver.get(
    "https://www.amazon.com/Dreo-Portable-Overheating-Protection-Oscillating/dp/B096ZZS5HL/ref=sr_1_1_sspa?crid"
    "=5SUBSAMP4GEK&keywords=fan%2Bthat%2Bblows%2Bcold%2Bair%2Blike%2Bac&qid=1672300605&refinements=p_72%3A1248915011"
    "&rnid=1248913011&s=home-garden&sprefix=ac%2Blike%2Bfan%2Caps%2C583&sr=1-1-spons&spLa"
    "=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNE5OWDczTjJXTDI2JmVuY3J5cHRlZElkPUEwNzA4NjExM0pORFYxM1VKMVZCSSZlbmNyeXB0ZWRBZElkPUEwNDM5Mzg3Mlk4NERNWjlLTTdLTSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1")
pric = driver.find_elements(By.CLASS_NAME, "a-price-fraction");

for p in pric:
    print(p.get_attribute("name"))

print("hello")
# driver.close()
# driver.quit()
