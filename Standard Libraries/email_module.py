#5. email module - Pyhton comes with buolt in smtplib module for sending mails using Simple mail transfer protocol
import smtplib

# sending mail using gmail account
# create a smtp session
s=smtplib.SMTP('smtp.gmail.com',587)

# start tls for security
s.starttls()

# login to your gmail account
s.login("jitendra9860vishwakarma@gmail.com","Ramanja@infinity0")

# message to be sent
msg="Happy New Year"

# sending the mail to recipient
s.sendmail("jitendra9860vishwakarma@gmail.com","luckyvishwa1104@gmail.com",msg)

# terminaate the session 
s.quit()
