from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which

chrome_path = which("chromedriver")

chorme_options = Options()
chorme_options.add_argument("--headlines")



driver = webdriver.Chrome(executable_path=chrome_path,options=chorme_options)
driver.get("https://duckduckgo.com")

search_inp = driver.find_element_by_id("searchbox_input")
search_inp.send_keys("imdb rating for article 370 2024 film")

# search_btn = driver.find_element_by_class_name("searchbox_searchButton__F5Bwq")
# search_btn.click()

search_inp.send_keys(Keys.ENTER)

print(driver.page_source)

driver.close()