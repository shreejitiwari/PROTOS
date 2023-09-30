# Print all available voices

import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:

    engine.setProperty('rate',140)
    engine.setProperty("voice",voice.id)

    # engine.say(f'Hello, I am {voice.name}. If you want to set this voice as my default voice, type "YES" or "Y"')
    # engine.runAndWait()
    # set = input('\n\n Do you want to set this as default voice(y/n) : ')
    # if set.lower() in  ' yes ':
    #     engine.say('Ok.. this is set as your default voice.')
    #     engine.runAndWait()

    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    # input()
        # break

    # else:
    #     print()
