import smtplib

sender_email = "honey37bunny@gmail.com"
rec_email = 'sp5944409@gmail.com'

message = "Hi Bro what are you doing?"

# password = input(str("Please enter your password : "))
password = "bunnyHoney8055"

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(sender_email,password)
print('Login Successful!')

server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)
