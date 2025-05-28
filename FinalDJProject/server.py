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
    with open("FinalDJProject/Data/borough_data.json","r") as f:
        raw_data = json.load(f)
    
    all_data = {}
    for date_entry in raw_data:
        date_name = date_entry["Date"]
        date_data = {
            year: float(value)
            for year, value in date_entry.items()
            if year.isdigit()
        }
        all_data[date_name] = date_data

    years = sorted(list(all_data["03/02/2020"].keys()), key= int)
        

    return render_template("index.html",years=years)

@app.route('/borough')
def micro_page():
    selected_borough = request.args.get('borough', 'Unknown Borough')
    return render_template("borough.html", borough=selected_borough)

app.run(debug=True)


