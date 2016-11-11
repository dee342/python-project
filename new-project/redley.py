import csv
import json
#from json2html import *


#Read CSV File
def read_csv(file, json_file, format):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        write_json(csv_rows, json_file, format)

#Convert csv data into json and write it

def write_json(data, json_file, format):

    with open(json_file, "w") as f:
        if format == "pretty":
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))
        else:
            f.write(json.dumps(data))


if __name__ == "__main__":
    csvfile = "C://Users//Petal//PycharmProjects//new-project//file.csv";
    jsonfile = "C://Users//Petal//PycharmProjects//new-project//file.json";
    read_csv(csvfile,jsonfile,"pretty");
