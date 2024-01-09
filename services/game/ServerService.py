from utils import Database

def GetServerDetail(gameSlug, serverId):
	response = None
	query = f'''
	SELECT "codashopIndex", "serverName", "midasbuyIndex" FROM "MTServer" 
	WHERE "gameSlug" = '{gameSlug}' AND "serverSlug"='{serverId}'
	'''
	dbResult = Database.FirstFromQuery(query)
	if dbResult is not None:
		response = {
			"codashopIndex": dbResult[0],
			"serverName": dbResult[1],
			"midasbuyIndex": dbResult[2]
		}

	return response

def GetServer(gameSlug):
	query = f'''
		SELECT "id", "serverSlug", "serverName" 
		FROM "MTServer"
		WHERE "gameSlug" = '{gameSlug}'
	'''
	dbResult = Database.FetchFromQuery(query)
	response = None
	if len(dbResult) > 0:
		response = [{
			"id": item[0], 
			"slug": item[1], 
			"name": item[2]
		} for item in dbResult] 

	return response