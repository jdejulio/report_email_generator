#!/usr/bin/env python3


import emails
import os
import reports

table_data = [['Name', 'Amount', 'Value'],
             ['elderberries', 10, 0.45],
             ['figs', 5, 3],
             ['apples', 4, 2.75],
             ['durians', 1, 25],
             ['bananas', 5, 1.99],
             ['cherries', 23, 5.80],
             ['grapes', 13, 2.48]]
reports.generate("/tmp/report.pdf", "A Complete Inventory of My Fruit", "This is all my fruit.", table_data)

sender = "sender@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "List of Fruits"
body = "Hi\n\nI'm sending an attachment with all my fruit."

message = emails.generate(sender, receiver, subject, body, "/tmp/report.pdf")
emails.send(message)

student@7687732d6bd0:~/scripts$ cat            
cars.py     emails.py   example.py  reports.py  
student@7687732d6bd0:~/scripts$ cat reports.py 
#!/usr/bin/env python3


from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate(filename, title, additional_info, table_data):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line, report_table])
