from sanic.response import json
from utils import Database
from utils import JWT
from services.auth import UserService
from flask import Flask, jsonify, request

def Get():
	keyword = request.args.get("keyword")
	listData = UserService.Get(keyword=keyword)
	data = {"list": listData}
	return jsonify({
		"status": 200,
		"message": None,
		"data": data
	})