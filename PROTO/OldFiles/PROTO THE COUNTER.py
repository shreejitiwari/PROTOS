import pyttsx3,time
proto=pyttsx3.init()
proto.setProperty('rate' , 210)

while True:
    n=abs(int(input('How many numbers you want to count : ')))
    for i in range(n,0,-1):
        print(i)
        proto.say(i)
        proto.runAndWait()
    ##                                time.sleep(1/5)
    print('\nFire !!!')
    proto.say('Fire')
    proto.runAndWait()
