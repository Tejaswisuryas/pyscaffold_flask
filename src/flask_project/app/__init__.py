from flask import Flask
app = Flask(__name__)
from flask import render_template
from app import app
from systeminfo1 import main
#from app import views

@app.route('/')
def index():
    returnDict = {}
    returnDict['title'] = 'Home'
    returnDict['systeminf'] = main.main()
    returnDict['user'] = 'Tejaswi'
    return render_template("index.html", **returnDict)
