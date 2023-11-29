from writer_class import WriterClass

writer = WriterClass('write_csv2')
writer.set_fields(['id','name','age','email'])
writer.set_rows([[1,'gjyli','26','gjylimekaj1@gmail.com'],
                [2,'vlori','30','vlori_b@hotmail.com'],
                 [3,'hello','24','hello@hotmail.com']])
# writer.write_to_file()
writer.read_from_file()
writer.write_to_excel_file()