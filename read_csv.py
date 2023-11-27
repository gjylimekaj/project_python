import csv

with open('our_birthday.txt','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    fields = next(csvreader)
    for row in csvreader:
        print(row)
        # print(row[0])
        # print(row[0],row[1],row[2])