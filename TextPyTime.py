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
        raise Exception("Man just put it in like a normie")


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
    
    account_sid = "AC5b354b171acb19895bfd41c3302b34d2"
    auth_token = "59635563c98e24ad8608e60f64a438af"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body=sent,
    from_="+18449925528",
    to=f"{phonenum}"
    )

if __name__=='__main__':
    Start()
    Stop(input("Please input the phone number to send the confirmation text to"))