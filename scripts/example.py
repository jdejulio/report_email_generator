#!/usr/bin/env python3


import email.message
import mimetypes
import os.path
import smtplib

def generate(sender, recipient, subject, body, attachment_path):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  # Process the attachment and add it to the email
  attachment_filename = os.path.basename(attachment_path)
  mime_type, _ = mimetypes.guess_type(attachment_path)
  mime_type, mime_subtype = mime_type.split('/', 1)

  with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                          maintype=mime_type,
                          subtype=mime_subtype,
                          filename=attachment_filename)

  return message

def send(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()
student@7687732d6bd0:~/scripts$ cat           
cars.py     emails.py   example.py  reports.py  
student@7687732d6bd0:~/scripts$ cat example.py 
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
