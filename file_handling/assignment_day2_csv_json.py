import csv
import json

def filter_adults():
    with open("data.csv") as data_file:
        dict_reader = csv.DictReader(data_file)
        adults = [row for row in dict_reader if int(row["Age"]) >= 18]
        #print (adults)
    
    with open("adults.csv", 'w', newline="") as adults_file:
        fields = ["Name", "Age"]
        csv_write = csv.DictWriter(adults_file, fieldnames= fields)
        csv_write.writeheader()
        csv_write.writerows(adults)


def add_to_json(file_name, dict_data):
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        data.append(dict_data)

    ### writing back to original json:
    with open(file_name, "w") as newjson_file:
        json.dump(data, newjson_file)

def search_log(log_file, search_keyword):
    with open(log_file) as file:
        for line in file:
            if search_keyword in line:
                print(line.strip())




######## Testing functions:
filter_adults()

json_data = {
    "name": "Prabin",
    "age": 24
  }
add_to_json("sample.json" , json_data)

search_log("search_log.txt", "critical")