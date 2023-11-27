import csv

fields = ['name','age','email']
rows = [['gjyli','26','gjylimekaj1@gmail.com'],
        ['vlori','30','vlori_b@hotmail.com'],
        ['hello','24','hello@hotmail.com']]

with open('write_csv.txt','w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

