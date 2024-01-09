from sanic.response import json
from services.log import LogService
from utils import Date
from services.scraper.codashop import CodashopService
from services.scraper.jollymax import JollymaxService
from services.scraper import CrawlerService
from services.game import AdditionalFieldService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from services.auth import RegistrationService
from services.scraper.midasbuy import MidasbuyService
from flask import Flask, jsonify, request
import os

def AutofillAction():
	url = "https://www.codashop.com/id-id/scroll-of-onmyoji-sakura--sword"
	driver = CrawlerService.OpendAndGetPage(url, "div")
	spectator = ActionChains(driver)

	optionEl = driver.find_element(By.CSS_SELECTOR, ".dropdown-select__search")
	spectator.move_to_element(optionEl).click().perform()
	spectator.send_keys("Ketiadaan")
	spectator.perform()
	time.sleep(2)
	itemEl = driver.find_element(By.CSS_SELECTOR, ".dropdown-select__result-list .result")
	itemEl.click()

def Get():

	# MidasbuyService.GetUsernameAvailability("6129021", "goddess-of-victory-nikke", "sea", "OPTIONS")
	# CodashopService.CrawlByUI("3509794783874", "among-heroes-fantasy-samkok", textualServerId=None, serverIndex="6", fieldType="OPTIONS")
	data = MidasbuyService.CrawlByUI("52049159862", "pubgm")
	# data = os.getcwd()

	return jsonify({
		"status": 200,
		"data": data
	})
