from utils import Database
from services.scraper.codashop import CodashopService
from services.scraper.codashop import LogService as CodashopLogService

from services.scraper.jollymax import JollymaxService
from services.scraper.jollymax import LogService as JollymaxLogService

from services.scraper.midasbuy import MidasbuyService
from services.scraper.midasbuy import LogService as MidasbuyLogService

from services.game import PipelineService
from services.game import AdditionalFieldService
from services.game import ServerService

def GetEmailSource():
	return "user@root.co"

def GetGameDetail(gameSlug):
	query = 'SELECT id, "name", "hasCodashop", "hasJollymax", "hasMidasbuy" FROM "MTGame" WHERE slug = \'' + gameSlug +  '\''
	dbResult = Database.FetchFromQuery(query)
	firstRow = dbResult[0]
	response = {
		"id": firstRow[0],
		"name": firstRow[1],
		"hasCodashop": firstRow[2],
		"hasJollymax": firstRow[3],
		"hasMidasbuy": firstRow[4]
	}

	return response

def Crawl(emailSource, userId, gameSlug, provider, textualServerId=None, fieldType=None):
	def Callback():
		CrawlerCtrl = None
		LogCtrl = None
		if provider == "codashop":
			CrawlerCtrl = CodashopService
			LogCtrl = CodashopLogService
		elif provider == "midasbuy":
			CrawlerCtrl = MidasbuyService
			LogCtrl = MidasbuyLogService
		elif provider == "jollymax":
			CrawlerCtrl = JollymaxService
			LogCtrl = JollymaxLogService

		LogCtrl.LogForInitiating(emailSource=emailSource, gameSlug=gameSlug, userGameId=userId);
		response = None

		try:
			response = CrawlerCtrl.GetUsernameAvailability(userId, gameSlug, textualServerId=textualServerId, fieldType=fieldType)
		except:
			LogCtrl.LogForFail(emailSource=emailSource, gameSlug=gameSlug, userGameId=userId)
			response = {"isAvailable": False} 

		if(response is not None):
			if response["isAvailable"] == True:
				LogCtrl.LogForFound(emailSource=emailSource, gameSlug=gameSlug, userGameId=userId);

			elif response["isAvailable"] == False:
				LogCtrl.LogForNotFound(emailSource=emailSource, gameSlug=gameSlug, userGameId=userId);

		return response

	return Callback


def GetUsernameAvailability(userId, gameSlug, textualServerId=None, fieldType=None):
	gameDetail = GetGameDetail(gameSlug)
	userId = userId.strip()
	hasCodashop = gameDetail["hasCodashop"]
	hasJollymax = gameDetail["hasJollymax"]
	hasMidasbuy = gameDetail["hasMidasbuy"]
	emailSource = GetEmailSource()
	response = None

	pipelineController = PipelineService.PipelineService()

	pipelineController.Push(
		key="codashop", 
		isAllowed=hasCodashop, 
		function=Crawl(emailSource, userId, gameSlug, "codashop", textualServerId, fieldType)
	)

	pipelineController.Push(
		key="midasbuy", 
		isAllowed=hasMidasbuy, 
		function=Crawl(emailSource, userId, gameSlug, "midasbuy", textualServerId, fieldType)
	)
	pipelineController.Push(
		key="jollymax", 
		isAllowed=hasJollymax, 
		function=Crawl(emailSource, userId, gameSlug, "jollymax", textualServerId)
	)
	try:
		response = pipelineController.Run()
	except Exception as e:
		raise Exception(e)


	return response

def GetGameAvailability(gameSlug):
	result = False
	query = 'SELECT COUNT(id) AS amount FROM "MTGame" WHERE slug = \'' + gameSlug + '\''
	dbResult = Database.FetchFromQuery(query)
	amount = dbResult[0][0]
	if amount > 0:
		result = True

	elif amount == 0:
		result = False
	else:
		result = False

	return result

def GetGameAttribute(gameSlug):
	response = {
		"additionalField": None,
		"additionalFieldType": None,
		"additionalFieldLabel": None,
		"servers": None
	}
	field = AdditionalFieldService.GetAdditionalField(gameSlug)
	if field is not None:
		response["additionalField"] = field["additionalField"]
		response["additionalFieldType"] = field["additionalFieldType"]
		response["additionalFieldLabel"] = field["additionalFieldLabel"]

	response["servers"] = ServerService.GetServer(gameSlug)
	return response