from services.scraper import CrawlerService
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import Database
import re
from selenium.webdriver.common.action_chains import ActionChains
from services.game import ServerService

midasbuyUrl = "https://www.midasbuy.com/id-id/mobile-legends"

def SelectServer(driver, serverIndex):
	serverInput = driver.find_element(By.CSS_SELECTOR, "[class^='BindLoginPop_select_area']")
	serverInput.click()
	time.sleep(0.5)

	serverItemInput = driver.find_element(By.CSS_SELECTOR, "[class^='SelectAreaPop_pop_mess'] [class^='SelectAreaPop'] div:nth-child(" + serverIndex + ")")
	serverItemInput.click()

def WhenShowingModal(driver):
	closeButtonEl = driver.find_elements(By.CSS_SELECTOR, ".close-btn")

	if len(closeButtonEl) > 0:
		closeButton = closeButtonEl[0]
		closeButton.click()
	
def CrawlByUI(userGameId, midasbuySlug, serverIndex=None, count=0):
	if count > 2:
		return ""
	label = None
	baseUrl = "https://www.midasbuy.com/midasbuy/id/buy"
	targetUrl = baseUrl + "/" + midasbuySlug
	driver = CrawlerService.OpendAndGetPage(targetUrl, "[class^='UserTabBox_login_text']")
	time.sleep(3)
	loginButton = driver.find_element(By.CSS_SELECTOR, "[class^='UserTabBox_login_text']")
	WhenShowingModal(driver)
	spectator = ActionChains(driver)
	spectator.move_to_element(loginButton).click().perform()
	# loginButton.click()
	time.sleep(0.5)

	textInput = driver.find_element(By.CSS_SELECTOR, "[class^='Input_input'] input")
	tempSubmitButton = driver.find_elements(By.CSS_SELECTOR, "[class^='PlayerIdEnterPop_btn_wrap'] [class^='Button_btn']") 
	if len(tempSubmitButton) == 0:
		tempSubmitButton = driver.find_elements(By.CSS_SELECTOR, "[class^='BindLoginPop_btn_wrap'] [class^='Button_btn']") 

	submitButton = tempSubmitButton[0]
	spectator = ActionChains(driver)
	spectator.move_to_element(submitButton).click().perform()


	textInput.send_keys(userGameId)
	time.sleep(0.5)

	if serverIndex is not None:
		SelectServer(driver, serverIndex)

	submitButton.click()

	time.sleep(0.5)
	errorMessageEl = driver.find_elements(By.CSS_SELECTOR, "[class^='Input_error_text'] p") 
	if len(errorMessageEl) > 0:
		errorMessage = errorMessageEl[0]
		label = errorMessage.text
	else:
		label = "success"
	

	return label

def GetIdentifiedUsername(userGameId, midasbuySlug, serverIndex = None):
	resultLabel = CrawlByUI(userGameId, midasbuySlug, serverIndex=serverIndex)

	response = { "userGameId": userGameId }
	if resultLabel == "success":
		response["isAvailable"] = True
	else:
		response["isAvailable"] = False

	return response

def GetMidasbuyDetail(gameSlug):
	query = 'SELECT id, "midasbuySlug" FROM "MTMidasbuyGame" WHERE "gameSlug" = \'' + gameSlug +  '\''
	dbResult = Database.FetchFromQuery(query)
	firstRow = dbResult[0]
	response = {
		"id": firstRow[0],
		"midasbuySlug": firstRow[1]
	}

	return response


def GetUsernameAvailability(userId, gameSlug, textualServerId=None, fieldType=None):
	print("midasbuy get username")
	midasbuyDetail = GetMidasbuyDetail(gameSlug)
	midasbuySlug = midasbuyDetail["midasbuySlug"]
	midasbuyIndex = None

	if fieldType == "OPTIONS":
		serverDetail = ServerService.GetServerDetail(gameSlug, textualServerId)
		midasbuyIndex = serverDetail["midasbuyIndex"]
			
	data = GetIdentifiedUsername(userId, midasbuySlug, serverIndex=midasbuyIndex)
	return data




