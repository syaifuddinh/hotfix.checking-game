from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import os

def OpendAndGetPage(pageUrl, testingSelector = None, timeout = 2):
	options = Options()
	options.add_argument("start-maximized") 
	options.add_argument("--mute-audio")

	environment = os.environ.get('SELENIUM_ENVIRONMENT')
	if environment == "production":
		options.add_argument('--headless=new')
		options.add_argument('--disable-gpu')
		options.add_argument("--no-sandbox") 
		options.add_argument("--disable-extensions") 

	if timeout > 7:
		raise Exception("Can't crawl through " + pageUrl)


	if environment == "production":
		chromePath = os.getcwd() + "/chromedriver"
		driver = webdriver.Chrome(options=options)
	else:
		driver = webdriver.Chrome(options=options)


	driver.get(pageUrl)
	time.sleep(timeout)
	if testingSelector is not None:
		testingElements = driver.find_elements(By.CSS_SELECTOR, testingSelector)
		if len(testingElements) == 0:
			return OpendAndGetPage(pageUrl, testingSelector, timeout=timeout + 1.5)

	return driver
