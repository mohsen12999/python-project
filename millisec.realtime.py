import time

def mytime(mil):
    mil = int(mil)
    seconds=(mil/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24
    print (hours+":"+minutes+":"+seconds+"."+(mil%1000))


mytime = time.time()
millis = int(round(mytime * 1000))
mytime(millis)