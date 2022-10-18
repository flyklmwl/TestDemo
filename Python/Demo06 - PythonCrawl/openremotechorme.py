from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = webdriver.ChromeOptions()
# chrome_options.set_capability('browserless:token', 'YOUR-API-TOKEN')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")

driver = webdriver.Remote(
  command_executor='http://localhost:3000/webdriver',
  desired_capabilities=chrome_options.to_capabilities()
)

driver.get("https://www.zhaopin.com/")
# print(driver.page_source)
driver.quit()