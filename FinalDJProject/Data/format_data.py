import json


f1 = open("FinalDJProject/Data/data_cleansed.csv", "r")
lines = f1.readlines()

dates = lines[0].split(",")[1:]
date_lines= lines[1:1894]  
formatted_data = []

for line in date_lines:
    values = line.strip().split(",")
    date_name = values[0]
    WeekAvgs = values[1:]

   
    date_dict = {}

    for i in range(len(dates)):
        date = dates[i].strip()
        value = WeekAvgs[i]
        date_dict[date] = value

    date_dict["Date"] = date_name
    formatted_data.append(date_dict)



f1.close()


#Save the json object to a file
f2 = open("FinalDJProject/Data/borough_data.json", "w")
json.dump(formatted_data, f2, indent = 4)

f2.close()