from sanic.response import json
from utils import Database
from services.game import GameService 
from exceptions import ValidationError 
from services.game import AdditionalFieldService
from flask import Flask, jsonify, request
from services.game import ServerService

def GetUsernameAvailability(gameSlug):
	isAvailable = GameService.GetGameAvailability(gameSlug)
	data = None

	if isAvailable == False:
		return jsonify({
			"status": 404,
			"message": None 
		})

	body = request.get_json()
	try:
		if "userId" not in body:
			raise Exception("User ID / Game ID is required")
			
		userId = body["userId"]
		if(userId is None):
			raise Exception("User ID / Game ID is required")

		meta = AdditionalFieldService.GetAdditionalField(gameSlug)
		additionalFieldRequest = None
		additionalFieldType = None
		if meta is not None:
			additionalField = meta["additionalField"]
			additionalFieldLabel = meta["additionalFieldLabel"]
			additionalFieldType = meta["additionalFieldType"]
			
			if additionalField not in body:
				raise Exception(additionalFieldLabel + " is required")
				
			additionalFieldRequest = body[additionalField]
			if additionalFieldRequest is None:
				raise Exception(additionalFieldLabel + " is required")

			if additionalFieldType is not None and (additionalFieldType == "OPTIONS" or additionalFieldType == "AUTOFILL"):
				serverDetail = ServerService.GetServerDetail(gameSlug, additionalFieldRequest)
				if serverDetail is None:
					raise Exception("Server is not found")

		data = GameService.GetUsernameAvailability(userId, gameSlug, textualServerId=additionalFieldRequest, fieldType=additionalFieldType)
	except Exception as e:
		print("there is an error in checking game")
		return jsonify({
			"status": 400,
			"message": f'{e}',
			"data": None
		})		

	return jsonify({
		"status": 200,
		"message": None,
		"data": data
	})
