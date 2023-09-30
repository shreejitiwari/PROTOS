import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()


try:
    with m as source: r.adjust_for_ambient_noise(source)
    
    while True:
        print('Speaker 1 : ')
        with m as source:
            audio1 = r.listen(source)
        
        try:
            text1 = r.recognize_google(audio)
            s1='{}'.format(text)
            print("Speaker 1 said : {}".format(text))
            with open('spkr.txt', 'a+') as f:
                f.write(s1.lower()+',')

    
        except:
            print('Sorry could not recognize')
            
        
            
        
        print('Speaker 2 : ')
        with m as source:
            audio2 = r.listen(source)
        
        try:
            text2 = r.recognize_google(audio)
            s2='{}'.format(text)
            print("Speaker 2 said : {}".format(text))
            with open('spkr.txt', 'a+') as f:
                f.write(s2.lower()+',')

        except:
            print('Sorry could not recognize')
            
        

except KeyboardInterrupt:
    pass



