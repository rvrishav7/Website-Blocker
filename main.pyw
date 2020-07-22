import time
from datetime import datetime as dt
blocked_sites=["www.facebook.com","www.instagram.com","www.twitter.com"] #list of websites to be blocked
path=r"C:\Windows\System32\drivers\etc\hosts"   #path to the hosts fle in Windows
to='127.0.0.1'  #the address to which connection for blocked sites are redirected
while True:
    block_start=dt(dt.now().year,dt.now().month,dt.now().day,8)
    block_stop=dt(dt.now().year,dt.now().month,dt.now().day,23,30)
    time.sleep(3)
    if block_start < dt.now() < block_stop :    #if current time is within range, block the sites
        print("Go Back to Work!")
        with open(path,'r+') as file:
            content=file.read()
            for site in blocked_sites:
                if site in content:
                    pass
                else:
                    file.write(to+" "+site+'\n')
    else:
        print("You are free!!")
        with open(path,'r+') as file:
            content= file.readlines() #makes a list of lines in variable content
            file.seek(0)    #brings pointer to the bwginning of file
            for line in content:
                if not any(site in line for site in blocked_sites): # means if not any elements of blocked sites
                    file.write(line)                                #belong in the lines add it to the file
            file.truncate()         #deletes whatever is at the end of the file so that same file doesn't get copued again and again
