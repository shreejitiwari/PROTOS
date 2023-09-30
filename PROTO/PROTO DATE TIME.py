import datetime as dt
import pyttsx3



eng = pyttsx3.init()
eng.setProperty("rate",135)
eng.setProperty("voice","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enIN_RaviM")

date = dt.date.today()
time = dt.datetime.now().strftime("%H:%M:%S")




print("Hello boss Shreeji\n")
eng.say("Hello boss Shreeji")
eng.runAndWait()

print("I am a program made by genius Shreeji Tiwari, my boss. I can tell you the current date and time\n")
eng.say("I am a program made by genius Shreeji Tiwari, my boss. I can tell you the current date and time")
eng.runAndWait()

print("The date is", str(date))
eng.say("The date is")
eng.say(date)
eng.runAndWait()

print("\nThe time is ",str(time))
eng.say("The time is "+str(time))
eng.runAndWait()