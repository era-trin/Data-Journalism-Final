from flask import Flask
from flask import request
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/about')
def home():
    return render_template("about.html")

@app.route('/')
def macro_page():
    return render_template("index.html")

@app.route('/borough')
def micro_page():
    selected_borough = request.args.get('borough', 'Unknown Borough')
    return render_template("borough.html", borough=selected_borough)

app.run(debug=True)


