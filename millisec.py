def mytime(mil):
    mil = int(mil)
    seconds=(mil/1000)%60
    seconds = int(seconds)
    minutes=(mil/(1000*60))%60
    minutes = int(minutes)
    hours=int(mil/(1000*60*60))%24
    print (hours,":",minutes,":",seconds)


millis=input("Enter time in milliseconds: ")
mytime(millis)