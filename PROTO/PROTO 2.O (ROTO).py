#!/usr/bin/env python
import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

try:
    with m as source: r.adjust_for_ambient_noise(source)
    r.pause_threshold=5
    while True:
        print("Say Something!!!!")
        with m as source:
            audio = r.listen(source)
        print('Recognizing....')
        try:
            text = r.recognize_google(audio,language='hinglish')
            print("you said: {}".format(text))
        except:
            print('Sorry could not recognize')
        
except KeyboardInterrupt:
    pass
