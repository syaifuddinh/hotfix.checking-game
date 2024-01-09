from utils import Database
from utils import String
from utils import Bcrypt

def GetDetailByEmail(email):
	query = f'''
		SELECT id, fullname, password, "apiKey" 
		FROM "MTUser"
		WHERE email = '{email}'  
	'''
	dbResult = Database.FirstFromQuery(query)
	result = None
	if dbResult is not None:
		result = {
			"id": dbResult[0],
			"fullname": dbResult[1],
			"password": dbResult[2],
			"apiKey": dbResult[3]
		}

	return result

def Get(keyword = None):
	query = f'''
		SELECT id, fullname, email, "isActive", "transactionNumber"
		FROM "MTUser" WHERE 1=1 
	'''
	if keyword is not None:
		query += " AND (email ILIKE '%" + keyword +"%' OR fullname ILIKE '%" + keyword + "%')"

	dbResult = Database.FetchFromQuery(query)
	result = []
	if dbResult is not None:
		result = [{
			"id": item[0], 
			"fullname": item[1], 
			"email": item[2],
			"isActive": item[3],
			"transactionNumber": item[4]
		} for item in dbResult] 

	return result