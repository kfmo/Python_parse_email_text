#The parse function takes as input the filepath of the file ("Prescription.txt") 
#and produces as output a dictionary

def parse(filepath):
    contents = open(filepath, 'r')
    lines = contents.readlines()
    doctors = {}
    for line in lines:
        if line[0:9] == 'Physician':
            if line[11:-1] not in doctors:
                doctors = {line[11:-1]}
                doctor = line[11:-1]
        if line[0:11] == 'Appointment':
            appts = {line[18:-1]}
            appt = line[18:-1]
        if line[0:10] == 'Medication':
            meds = {'Prescribed Medications': line[12:-1]}
        if line[0:4] == 'Dose':
            dosage = {'Dose': line[6:-1]}
        if line[0:10] == 'Directions':
            instructions = {'Directions': line[12:-1]}
        if line[0:8] == 'Pharmacy':
            pharm = {'Pharmacy': line[10:-1]}
        if line[0:7] == 'Address':
            loc = {'Address': line[9:-1]}
        if line[0:7] == 'Pick-up':
            pickup = {'Pick-up Date': line[14:]}
    appts = {appt: [meds, dosage, instructions, pharm, loc, pickup]}
    doctors = {doctor: appts}
    return doctors



#Below uses the smtplib and email modules to create and send email notifications    

import smtplib
from email.mime.multipart import MIMEMultipart

prescription = parse(filepath)

email_msg = MIMEMultipart()
email_msg['From'] = 'from email'

#If sending a text message notification instead of an email, then 'receiving email' 
#should be the mobile service provider's email to SMS Gateway
  #e.g., '10-digit phone number'@txt.att.net; '10-digit phone number'@vtext.com 
  
email_msg['To'] = 'receiving email'
email_msg['Subject'] = 'subject header'

#An example of what would go in between the single quotes of msg:
  #prescription['Dr. Rodwell']['6/30/2015'][3]['Pharmacy']
  #prescription['Dr. Rodwell']['6/30/2015'][4]['Address']
  #prescription['Dr. Rodwell']['6/30/2015'][5]['Pick-up Date']

msg = ''

mail = smtplib.SMTP('smtp.gmail.com', 'port')   #email service provider and port number
mail.ehlo_or_helo_if_needed()   #greet the smtp server
mail.starttls()   #create tls connection
mail.login('from email', 'password')  #login with email credentials
mail.sendmail('from email', 'receiving email', msg)   #send msg to recipient

mail.close()  #logout

