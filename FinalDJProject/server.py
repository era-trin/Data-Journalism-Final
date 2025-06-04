from flask import Flask
from flask import request
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

def hospitalized_to_hsl(life):
    legend = [
        (50,  "hsl(0, 100%, 80%)"),   
        (100, "hsl(0, 100%, 70%)"),   
        (200, "hsl(0, 100%, 50%)"),   
        (300, "hsl(0, 100%, 15%)"),  
        (400, "hsl(0, 100%, 10%)"),   
        (500, "hsl(0, 100%, 5%)")    
    ]
    for val, hsl in reversed(legend):
        if life >= val:
            return hsl
    return "hsl(0, 100%, 95%)"  


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
        selected_date = all_dates[0]  

    selected_data = next((entry for entry in raw_data if entry["Date"] == selected_date), None)

    borough_colors = {
        "manhattan": hospitalized_to_hsl(int(selected_data["MN_HOSPITALIZED_COUNT"])), 
        "brooklyn": hospitalized_to_hsl(int(selected_data["BK_HOSPITALIZED_COUNT"])),
        "statenisland": hospitalized_to_hsl(int(selected_data["SI_HOSPITALIZED_COUNT"])),
        "queens": hospitalized_to_hsl(int(selected_data["QN_HOSPITALIZED_COUNT"])),
        "bronx": hospitalized_to_hsl(int(selected_data["BX_HOSPITALIZED_COUNT"]))
    }
    total = []
    dates = []
    for entry in raw_data:
        if all(k in entry for k in ["MN_HOSPITALIZED_COUNT", "BK_HOSPITALIZED_COUNT", "QN_HOSPITALIZED_COUNT", "BX_HOSPITALIZED_COUNT", "SI_HOSPITALIZED_COUNT"]):
            dates.append(entry["Date"])
            total.append(int(entry["MN_HOSPITALIZED_COUNT"]) +
                int(entry["BK_HOSPITALIZED_COUNT"]) +
                int(entry["QN_HOSPITALIZED_COUNT"]) +
                int(entry["BX_HOSPITALIZED_COUNT"]) +
                int(entry["SI_HOSPITALIZED_COUNT"]))
    total_peak_value = max(total)
    total_peak_date = dates[total.index(total_peak_value)]
   
    return render_template(
        "index.html",
        dates=all_dates,
        borough_colors=borough_colors,
        selected_date=selected_date,
        total_peak_value=total_peak_value,
        total_peak_date=total_peak_date
    )

@app.route('/borough')
def micro_page():
    import json
    with open("FinalDJProject/Data/borough_data.json", "r") as f:
        raw_data = json.load(f)
    all_dates = [entry["Date"] for entry in raw_data]
    selected_date = request.args.get('date')
    if not selected_date or selected_date not in all_dates:
        selected_date = all_dates[0]

    
    dates = []
    manhattan = []
    brooklyn = []
    staten_island = []
    queens = []
    bronx = []
    total = []
    for entry in raw_data:
        if all(k in entry for k in ["MN_HOSPITALIZED_COUNT", "BK_HOSPITALIZED_COUNT", "QN_HOSPITALIZED_COUNT", "BX_HOSPITALIZED_COUNT", "SI_HOSPITALIZED_COUNT"]):
            dates.append(entry["Date"])
            manhattan.append(int(entry["MN_HOSPITALIZED_COUNT"]))
            brooklyn.append(int(entry["BK_HOSPITALIZED_COUNT"]))
            staten_island.append(int(entry["SI_HOSPITALIZED_COUNT"]))
            queens.append(int(entry["QN_HOSPITALIZED_COUNT"]))
            bronx.append(int(entry["BX_HOSPITALIZED_COUNT"]))
            total.append(int(entry["MN_HOSPITALIZED_COUNT"]) +
                int(entry["BK_HOSPITALIZED_COUNT"]) +
                int(entry["QN_HOSPITALIZED_COUNT"]) +
                int(entry["BX_HOSPITALIZED_COUNT"]) +
                int(entry["SI_HOSPITALIZED_COUNT"]))
        
    manhattan_peak_value = max(manhattan)
    manhattan_peak_date = dates[manhattan.index(manhattan_peak_value)]
    manhattan_min_value = min(manhattan)
    manhattan_min_date = dates[manhattan.index(manhattan_min_value)]
    manhattan_total = sum(manhattan)


    brooklyn_peak_value = max(brooklyn)
    brooklyn_peak_date = dates[brooklyn.index(brooklyn_peak_value)]
    brooklyn_min_value = min(brooklyn)
    brooklyn_min_date = dates[brooklyn.index(brooklyn_min_value)]
    brooklyn_total = sum(brooklyn)


    queens_peak_value = max(queens)
    queens_peak_date = dates[queens.index(queens_peak_value)]
    queens_min_value = min(queens)
    queens_min_date = dates[queens.index(queens_min_value)]
    queens_total = sum(queens)


    bronx_peak_value = max(bronx)
    bronx_peak_date = dates[bronx.index(bronx_peak_value)]
    bronx_min_value = min(bronx)
    bronx_min_date = dates[bronx.index(bronx_min_value)]
    bronx_total = sum(bronx)


    statenisland_peak_value = max(staten_island)
    statenisland_peak_date = dates[staten_island.index(statenisland_peak_value)]
    statenisland_min_value = min(staten_island)
    statenisland_min_date = dates[staten_island.index(statenisland_min_value)]
    statenisland_total = sum(staten_island)
    
   
 
    selected_borough = request.args.get('borough', 'Unknown Borough')
    return render_template(
        "borough.html",
        borough=selected_borough,
        dates=all_dates,
        graph_dates=dates,
        graph_manhattan=manhattan,
        graph_brooklyn=brooklyn,
        graph_statenisland=staten_island,
        graph_queens=queens,
        graph_bronx=bronx,
        total=sum(total),
        selected_date=selected_date,
        max=max,
       
        manhattan_peak_date=manhattan_peak_date,
        manhattan_peak_value=manhattan_peak_value,
        manhattan_min_date=manhattan_min_date,
        manhattan_min_value=manhattan_min_value,
        manhattan_total=manhattan_total,
       
        brooklyn_peak_date=brooklyn_peak_date,
        brooklyn_peak_value=brooklyn_peak_value,
        brooklyn_min_date=brooklyn_min_date,
        brooklyn_min_value=brooklyn_min_value,
        brooklyn_total=brooklyn_total,
     
        queens_peak_date=queens_peak_date,
        queens_peak_value=queens_peak_value,
        queens_min_date=queens_min_date,
        queens_min_value=queens_min_value,
        queens_total=queens_total,
        
        bronx_peak_date=bronx_peak_date,
        bronx_peak_value=bronx_peak_value,
        bronx_min_date=bronx_min_date,
        bronx_min_value=bronx_min_value,
        bronx_total=bronx_total,
       
        statenisland_peak_date=statenisland_peak_date,
        statenisland_peak_value=statenisland_peak_value,
        statenisland_min_date=statenisland_min_date,
        statenisland_min_value=statenisland_min_value,
        statenisland_total=statenisland_total
    )

app.run(debug=True)


