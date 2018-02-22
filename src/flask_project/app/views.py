from systeminfo1 import main
from flask import render_template
from app import app


@app.route('/')
def index():
    returnDict = {}
    returnDict['user'] = 'Tejaswi'
    returnDict['systeminf'] = systeminfo1.main()
    returnDict['title'] = 'Home'
    return render_template("index.html", **returnDict)
