from flask import Flask
from flask import request
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

def hospitalized_to_hsl(life):
 
    legend = [
        (0, "hsl(0, 100%, 85%)"),
        (20, "hsl(0, 100%, 85%)"),
        (35, "hsl(0, 100%, 85%)"),
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
    return legend[0][1]  


@app.route('/about')
def home():
    return render_template("about.html")

@app.route('/')
def macro_page():
    with open("FinalDJProject/Data/borough_data.json","r") as f:
        raw_data = json.load(f)
    
    all_dates = [entry["Date"] for entry in raw_data]
    # manhattan = (all_dates['MN_HOSPITALIZED_COUNT'][selected_date])
    
    return render_template("index.html",dates=all_dates)

@app.route('/borough')
def micro_page():
    selected_borough = request.args.get('borough', 'Unknown Borough')
    return render_template("borough.html", borough=selected_borough)

app.run(debug=True)


