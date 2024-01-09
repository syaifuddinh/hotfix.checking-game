from sanic import Sanic
from controllers.user import UserController

def Init(app):
	app.add_url_rule(
		"/user", 
		"list-user",
		UserController.Get, 
		methods=["Get"] 
	)
