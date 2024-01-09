import os
from utils import Database
from utils import Bcrypt
from utils import JWT
from utils import String
from services.auth import UserService
from google.auth.transport import requests
from google.oauth2 import id_token
from services.auth import RegistrationService
from services.auth import UserService

errorMessage = "Email or password is wrong"

def IsRegistered(email, password):
	userDetail = UserService.GetDetailByEmail(email)
	if userDetail is None:
		return False

	storedPassword = userDetail["password"]
	isValid = Bcrypt.GetValidity(password, storedPassword)
	return isValid 

def Login(email, password):
	isRegistered = IsRegistered(email, password)
	if isRegistered == False:
		raise Exception(errorMessage)

	user = UserService.GetDetailByEmail(email)
	userFullname = user["fullname"]
	data = JWT.Generate(email, name=userFullname)

	return data

def LoginByGoogle(token):
	CLIENTID = os.environ.get('GOOGLE_CLIENT_ID')

	try:
		# Verify the ID token
		id_info = id_token.verify_oauth2_token(token, requests.Request(), CLIENTID)

		# Print user information
		email = id_info['email']
		newPassword = String.Random(16)
		try:
			RegistrationService.Register(email, password=newPassword, fullname=email)
		except Exception as e:
			print("account is exist")

		user = UserService.GetDetailByEmail(email)
		userFullname = user["fullname"]
		data = JWT.Generate(email, name=userFullname)
		# You can perform additional checks and actions here based on the user information.

		return data
	except ValueError as e:
		# Invalid token
		raise Exception(e)

def GetApiKey(email):
	query = f'''
		SELECT "apiKey" FROM "MTUser" WHERE email='{email}'
	'''
	dbResult = Database.FirstFromQuery(query)
	if dbResult is None:
		raise Exception("Email is not valid")
	response = {
		"apiKey": dbResult[0]
	};
	return response