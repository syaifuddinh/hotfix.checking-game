from flask import jsonify, request
from services.game import ServerService

def Get(gameSlug):
	listData = ServerService.GetServer(gameSlug)
	data = {"list": listData}
	if listData is None:
		data["list"] = []

	return jsonify({
		"status": 200,
		"message": None,
		"data": data
	})
