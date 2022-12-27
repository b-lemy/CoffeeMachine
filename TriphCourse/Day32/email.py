import smtplib

my_email = "lemabrian1234@gmail.com"
password = "Calvin123#"
connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="Brian.lema@mkombozibank.co.tz", msg="Hello")
connection.close()
