import os
import smtplib
from email.message import EmailMessage
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir('folderpath') if isfile(join('folderpath', f))]
onlyfiles.remove('EmailSender.py')
# uncomment the line below if want to turn the script in an exe
# onlyfiles.remove('program.bat')
print(onlyfiles)

msg = EmailMessage()
msg['Subject'] = ''
msg['From'] = ''
msg['To'] = ''
msg.set_content('')

for file in onlyfiles:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='application', subtype='vnd.openxmlformats-officedocument.wordprocessingml.document', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('', '')
    smtp.send_message(msg)


for file in onlyfiles:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    os.rename('folderpath'+str(file_name), 'folderpath/oldfiles/'+str(file_name))

# replace folderpath to path of the folder the .py file is in
# this script will attach .docx files that are in the same folder, and send them to the target email
# after sending, the files will be moved to an "oldfiles" folder
