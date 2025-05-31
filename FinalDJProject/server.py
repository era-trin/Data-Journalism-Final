from flask import Flask
from flask import request
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

def hospitalized_to_hsl(life):
 
    legend = [
        (50, "hsl(0, 100%, 70%)"),
        (100, "hsl(0, 100%, 55%)"),
        (200, "hsl(0, 100%, 40%)"),
        (300, "hsl(0, 100%, 25%)"),
        (400, "hsl(0, 100%, 15%)"),
        (500, "hsl(0, 100%, 5%)")

    ]
    
    for val, hsl in reversed(legend):
        if life >= val:
            return hsl
    return "hsl(0,100%,5%)"


@app.route('/about')
def home():
    return render_template("about.html")


@app.route('/')
def macro_page():
    selected_date = request.args.get('date', '02/29/2020')
    with open("FinalDJProject/Data/borough_data.json","r") as f:
        raw_data = json.load(f)

    selected_data = None
    for entry in raw_data:
        if entry["Date"] == selected_date:
            selected_data = entry
    
    all_dates = [entry["Date"] for entry in raw_data]

    borough_colors = {
    "manhattan":hospitalized_to_hsl(int(selected_data["MN_HOSPITALIZED_COUNT"])), 
    "brooklyn":hospitalized_to_hsl(int(selected_data["BK_HOSPITALIZED_COUNT"])),
    "statenisland":hospitalized_to_hsl(int(selected_data["SI_HOSPITALIZED_COUNT"])),
    "queens":hospitalized_to_hsl(int(selected_data["QN_HOSPITALIZED_COUNT"])),
    "bronx":hospitalized_to_hsl(int(selected_data["BX_HOSPITALIZED_COUNT"]))
    }
   
    
    return render_template("index.html",dates=all_dates, borough_colors=borough_colors)

    






@app.route('/borough')
def micro_page():
    selected_borough = request.args.get('borough', 'Unknown Borough')
    return render_template("borough.html", borough=selected_borough)

app.run(debug=True)


