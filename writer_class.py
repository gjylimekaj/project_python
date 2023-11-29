import csv
import xlsxwriter

class WriterClass:
    def __init__(self,file_name):
        self.fields = None
        self.rows = None
        self.file_name = file_name

    def set_fields(self,fields):
        self.fields = fields
    def set_rows(self,rows):
        self.rows = rows

    def write_to_file(self):
        with open(self.file_name + '.txt', 'w', newline = '') as csvfile:
            csvwriter = csv.writer(csvfile)

            csvwriter.writerow(self.fields)
            csvwriter.writerows(self.rows)
        csvfile.close()

    def read_from_file(self):
        with open(self.file_name + '.txt', 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            self.fields = next(csvreader)
            for row in csvreader:
                print(row)

    def write_to_excel_file(self):
        workbook = xlsxwriter.Workbook(self.file_name + '.xlsx')
        worksheet = workbook.add_worksheet()

        # Write the header (fields) to the first row
        for col_num, field in enumerate(self.fields):
            worksheet.write(0, col_num, field)

        # Write the rows starting from the second row
        for row_num, row in enumerate(self.rows, start=1):
            for col_num, value in enumerate(row):
                worksheet.write(row_num, col_num, value)

        # Finally, close the Excel file
        workbook.close()
