from pypresence import Presence
from datetime import datetime
from time import sleep, time

id=str(input("The program wouldn't run without your discord id (Applications ID). REMEMBER: DONT SHARE YOUR ID WITH OTHERS. \n Give an id: "))
RPC = Presence(id) # put your discord id here
RPC.connect()
while True:
    Current = datetime.now().strftime("%H:%M:%S") # | getting current time
    Current2 = Current                            # | making a copy

    if (int(Current[3:5])//5==0):                                           # \
        Current = str(int(Current[:2])%12) + "00"                           #  \
    elif (int(Current[3:5])//5==1):                                         #   \
        Current = str(int(Current[:2])%12) + "05"                           #    } getting name of jpg - for example: current time is 15:30 jpg name would be 330.jpg
    else:                                                                   #   /
        Current = str(int(Current[:2])%12) + str((int(Current[3:5])//5)*5)  #  /
    print ("Current", Current)                                              # /

    RPC.update(                                                                                     # \
        large_image = Current,                                                                      #  \
        large_text = "Refreshing every 5th minute!",                                                #   } updating discord status
        start = (time () - int(Current2[:2])*3600 - int(Current2[3:5])*60 - int(Current2[6:8])*1)   #  /
    )                                                                                               # /

    Current = datetime.now().strftime("%M:%S")                              # \
    if (Current[3:5] != "00"):                                              #  \
        Current = 360-((int(Current[:2])%5)*60) - 60-(int(Current[3:5]))    #   } calculating sleep time (we want to refresh every 5th minute)
    else:                                                                   #  /
        Current = 300-((int(Current[:2])%5)*60)                             # /

    print (f"sleeping for {Current//60} minutes and {Current%60} seconds..\n")
    sleep(Current)
