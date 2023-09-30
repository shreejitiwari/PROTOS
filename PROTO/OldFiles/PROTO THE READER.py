import pyttsx3
import datetime as dt


proto=pyttsx3.init()
voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_MarkM'
proto.setProperty('rate' , 150)
proto.setProperty('voice', voice_id)


date = dt.date.today()
time = dt.datetime.now().strftime("%H:%M:%S")


print("Hello there, I am a reader program. I will read out whatever you ask me to read. ")
proto.say("Hello there, I am a reader program. I will read out whatever you ask me to read .")
proto.runAndWait()


while True:  
    proto.say("Enter the paragraph")
    proto.runAndWait()
    para=input('''Enter the paragraph : ''').lower()

    
    
    if para in ["exit","bye","end the program","close the program","end","close","end it","stop it","stop the program"]:
        print("Okay, ending the program.")
        print("\nHave a GOOD DAY !!")
        proto.say("Okay , I , Proto ,  ending the program . Have a good day. ")
        proto.runAndWait()

        break
    
    
    elif para in ['todays date', 'today date', 'date today']:
        print("The date is", str(date))
        proto.say("The date is")
        proto.say(date)
        proto.runAndWait()
    
    
    elif para in  ['current time','what is the time','whats the time right now']:
        print(f"The time is {time}")
        proto.say("The time is")
        proto.say(time)
        proto.runAndWait()
    
    

    else:
        proto.say(para)
        proto.runAndWait()




















