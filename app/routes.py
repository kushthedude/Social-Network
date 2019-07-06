from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Prince Vegeta'}
	posts = [
	{
	'author' : {'username': 'Vegeta'},
	'body' : 'Saiyans are a true warriors race'
	},
	{
	'author' : {'username' : 'Loda'},
	'body' : 'Teri maa ko chodu kya bhen ke lode'
	}

	]
	return render_template('index.html', title='Home', user=user, posts=posts)