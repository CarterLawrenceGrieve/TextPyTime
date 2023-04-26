from time import time
import os
from twilio.rest import Client

def Start():
    global starttime
    starttime=time()

def CleanNum(num):
    if type(num)==int:
        return num
    elif type(num)==str:
        num=num.replace('-','')
        num=num.replace('.','')
        return num
    else:
        raise Exception("Man just put it in normal, with the area code and all that ('1-234-5678'), I can't be bothered to figure out how to clean this up better without more research than I'm willing to do for a meme")


def Stop(phonenum):
    phonenum=CleanNum(phonenum)
    endtime=time()
    grantotal=endtime-starttime
    minutes,seconds=divmod(grantotal,60)
    hours, minutes=divmod(minutes,60)
    seconds=round(seconds)
    if hours==True:
        sent=f'The script ran in {hours} hours,{minutes} minutes, and {seconds} seconds.  Such speed!'
    elif minutes==True:
        sent=f'The script ran in {minutes} minutes, and {seconds} seconds.  Such speed!'
    else:
        sent=f'The script ran in {seconds} seconds.  Such speed!'
    
    account_sid = "INSERT YOUR OWN TWILIO ACCOUNT SID HERE"
    auth_token = "INSERT YOUR TWILIO AUTHENTICATION TOKEN HERE"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body=sent,
    from_="INSERT YOUR OWN TWILIO PHONE NUMBER HERE",
    to=f"{phonenum}"
    )

if __name__=='__main__':
    Start()
    Stop(input("Please input the phone number to send the confirmation text to"))
