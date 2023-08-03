import smtplib
from email.mime.text import MIMEText



def send_email_to_myself(percentage,price):
    sendAddress = '######'  # set to your own address
    # Authorization code
    password = '######' # set to your own Authorization code,get from your email website
    # connect to server
    server = smtplib.SMTP_SSL('######', 465) # for example: smtp.163.com
    # Login E-mail
    loginResult = server.login(sendAddress, password)
    # print(loginResult)

    # content
    content = "run to biance, instance percentage: " + str(percentage)

    msg = MIMEText(content, 'plain', 'utf-8')


    msg['From'] = '######'
    # recipient 

    msg['To'] = '######'



    # email theme
    msg['Subject'] = 'waves notification'

    server.sendmail(sendAddress,['########'],msg.as_string())
    print("The email has been sent")
if __name__ == "__main__":
    print("test")