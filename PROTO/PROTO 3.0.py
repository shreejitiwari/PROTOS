import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
m = sr.Microphone()
proto = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enIN_RaviM"

proto.setProperty('rate' , 140)
proto.setProperty('voice',voice_id)


print("Hello there!!! , I am proto 3.0 . I will repeat Whatever you would say.")
proto.say("Hello dear , I am proto 3.0 . I will repeat Whatever you would say.")
proto.runAndWait()

try:
    with m as source : r.adjust_for_ambient_noise(source)

    while True:
        print("Say Something")
        proto.say("Say Something")
        proto.runAndWait()
        with m as source: audio = r.listen(source)
        try:
        
            txt = r.recognize_google(audio, 'hindi')
            pend=['exit','end this program','get lost',"get out"]
                
            if txt in pend:
                print("YOU : {}".format(txt))
                print("OKAY BOSS..........\n CLOSING THE PROGRAM......")
                proto.say("OKAY BOSS..........\n CLOSING THE PROGRAM......")
                proto.runAndWait()
                break
                
                
            else:
                print("you said: {}".format(txt))
                proto.say("you said," + txt)
                proto.runAndWait()


        except:
            print("Sorry , could not recognize")
            proto.say("sorry, could not recognize")
            proto.runAndWait()
            
except KeyboardInterrupt:
  pass

        
                
