def mytime(mil):
    mil = int(mil)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24
    print (hours+":"+minutes+":"+seconds)


millis=input("Enter time in milliseconds: ")
mytime(millis)