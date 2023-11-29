import csv

fields = ['id','name','age','email']
rows = [[1,'gjyli','26','gjylimekaj1@gmail.com'],
        [2,'vlori','30','vlori_b@hotmail.com'],
        [3,'hello','24','hello@hotmail.com']]

with open('write_csv.txt','w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

