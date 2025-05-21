import json


f1 = open("Data/data_cleansed.csv", "r")
lines = f1.readlines()

dates = lines[0].split(",")[1:]
borough_lines= lines[1:11]  
formatted_data = []

for line in borough_lines:
    values = line.strip().split(",")
    borough_name = values[0]
    WeekAvgs = values[1:]

   
    boroughs_dict = {}

    for i in range(len(dates)):
        date = dates[i].strip()
        value = WeekAvgs[i]
        boroughs_dict[date] = value

    boroughs_dict["Borough Name"] = borough_name
    formatted_data.append(boroughs_dict)



f1.close()


#Save the json object to a file
f2 = open("borough_data.json", "w")
json.dump(formatted_data, f2, indent = 4)

f2.close()