import csv


def getData():
    data = []
    csv_data = open(str("Credential.csv"), "r")
    content = csv.reader(csv_data)
    next(content, None)
    for row in content:
        data.append(row)
    return data
