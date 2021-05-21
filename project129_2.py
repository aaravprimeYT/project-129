import csv

dataset1 = []
dataset2 = []

with open ("project127_2.csv","r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset1.append(row)

with open ("project128_2.csv","r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset2.append(row)

headers1 = dataset1[0]
planetData1 = dataset1[1:]

headers2 = dataset2[0]
planetData2 = dataset2[1:]

headers = headers1 + headers2
planetData = []

for index,dataRow in enumerate(planetData1):
    planetData.append(planetData1[index] + planetData2[index])
    
with open("project129_final.csv","a+")as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planetData)