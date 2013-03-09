# IMPORT STUFF!!

# python standard libraries
import random, json

# flask
import flask

# pymongo
import pymongo
from bson import ObjectId

# creating new Flask instance
app = flask.Flask(__name__)

# open database connection!
connection = pymongo.Connection()
db = connection.whenthesisisover

app.secret_key = '''nTi!"2Oq#j2WdnUsQziTn52y8xGfZl:"MH*H|`yVClNLA4UG'GIvq1qc%Gk}vu<'''


# --------------------------------------------

@app.route('/')
def index():
	
	# grab a random idea from the db
	
	totalIdeas = db.ideas.count()
	randomNum = random.randint(0, totalIdeas - 1)
	
	idea = db.ideas.find_one({}, skip=randomNum)
	
	return flask.render_template("index.html", idea=idea)
	

# --------------------------------------------

@app.route('/fetchNewIdea')
def fetchNewIdea():
	
	# grab a random idea from the db
	
	totalIdeas = db.ideas.count()
	randomNum = random.randint(0, totalIdeas - 1)
	
	idea = db.ideas.find_one({}, skip=randomNum)
	
	return idea['idea']


	
# --------------------------------------------

@app.route('/add')
def add():
	
	return flask.render_template("form.html")


@app.route('/postNewIdea', methods=['POST'])
def postNewIdea():
	
	data = flask.request.form;
	
	idea = {
		'name' : data['name'],
		'email' : data['email'],
		'idea' : data['idea']
	}
	
	db.ideas.insert(idea)
	
	flask.flash('idea posted!')
	
	return flask.redirect(flask.url_for('index'))


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=2012, debug=True)