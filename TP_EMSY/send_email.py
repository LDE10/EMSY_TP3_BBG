__author__ = "Pouly Steeve"
__version__ = "0.1"
__maintainer__ = "Pouly Steeve"
__email__ = "steve.pouly@eduvaud.ch"
__status__ = "Production"
__date__ = "avril 2026"

#-----------------------------------------------------
# Importing libraries and modules
#-----------------------------------------------------
import datetime                                                             # Library for date and time related stuff
import smtplib                                                              # Library for email related stuff

#-----------------------------------------------------
# Declaring functions
#-----------------------------------------------------
def send_email(receiver, subject, message):                                 #Fonction envoye de mail
    server = smtplib.SMTP("mail.etml-es.ch")
    server.login("luc.derre@etml-es.ch","v3c8ychWtXURJ*Mw")                 #Connexion à un compte infomaniaque avec code d'accès
    sender = "luc.derre@etml-es.ch"                                         #Mail d'infomaniaque

    headers = {                                                             #Structure d' un e-mail
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Disposition': 'inline',
        'Content-Transfer-Encoding': '8bit',
        'From': sender,
        'To':receiver,
        'Date': datetime.datetime.now().strftime('%a, %d %b %Y  %H:%M:%S %Z'),
        'X-Mailer': 'python',
        'Subject': subject
    }
    # create the message
    msg = ''
    for key, value in headers.items():
        msg += "%s: %s\n" % (key, value)

    # add contents
    msg += "\n%s\n" % (message)

    try:
        server.sendmail(headers['From'], headers['To'], msg.encode("utf8"))
        server.quit()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)
