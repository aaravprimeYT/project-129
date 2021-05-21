import csv

data = []

with open ("project128_2.csv","r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data.append(row)

headers = data[0]

planetData = data[1:]

for dataPoint in planetData:
    dataPoint[0] = dataPoint[0].lower()

planetData.sort(key = lambda planetData:planetData[0])

with open("project128_2_sorted.csv","a+")as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planetData)