from flask import Flask
from flask import request
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

def hospitalized_to_hsl(life):
 
    legend = [
        (50, "hsl(0, 100%, 85%)"),
        (100, "hsl(0, 100%, 55%)"),
        (200, "hsl(0, 100%, 40%)"),
        (300, "hsl(0, 100%, 25%)"),
        (400, "hsl(0, 100%, 15%)"),
        (500, "hsl(0, 100%, 5%)")

    ]
    
    for val, hsl in reversed(legend):
        if life >= val:
            return hsl
    return "hsl(0,100%,85%)"


@app.route('/about')
def home():
    return render_template("about.html")


@app.route('/')
def macro_page():
    with open("FinalDJProject/Data/borough_data.json","r") as f:
        raw_data = json.load(f)

    all_dates = [entry["Date"] for entry in raw_data]
    selected_date = request.args.get('date')
    if not selected_date or selected_date not in all_dates:
        selected_date = all_dates[0]  # Use the first date in your data

    selected_data = next((entry for entry in raw_data if entry["Date"] == selected_date), None)

    borough_colors = {
        "manhattan": hospitalized_to_hsl(int(selected_data["MN_HOSPITALIZED_COUNT"])), 
        "brooklyn": hospitalized_to_hsl(int(selected_data["BK_HOSPITALIZED_COUNT"])),
        "statenisland": hospitalized_to_hsl(int(selected_data["SI_HOSPITALIZED_COUNT"])),
        "queens": hospitalized_to_hsl(int(selected_data["QN_HOSPITALIZED_COUNT"])),
        "bronx": hospitalized_to_hsl(int(selected_data["BX_HOSPITALIZED_COUNT"]))
    }
   
    return render_template(
        "index.html",
        dates=all_dates,
        borough_colors=borough_colors,
        selected_date=selected_date
    )

@app.route('/borough')
def micro_page():
    selected_borough = request.args.get('borough', 'Unknown Borough')
    return render_template("borough.html", borough=selected_borough)

app.run(debug=True)


