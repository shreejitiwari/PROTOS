import webbrowser
import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import speech_recognition as sr
import pyttsx3
from webdriver_manager.chrome import ChromeDriverManager

r = sr.Recognizer()
m = sr.Microphone()
with m as source : r.adjust_for_ambient_noise(source)
proto = pyttsx3.init()
voice_id = "Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
proto.setProperty('voice',voice_id)
proto.setProperty('rate' , 140)




# q = input("What you want to do : ").lower()
# webbrowser.open(f"https://www.vedantu.com")

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

# def listen():
    
def close():
    print(f"YOU : {command}")
    print("OKAY BOSS..........\n CLOSING THE PROGRAM......")
    proto.say("OKAY BOSS..........\n CLOSING THE PROGRAM......")
    proto.runAndWait()
    exit()


def vedantu(user):
    
    batch_dict = {'maths' : '//*[@id="app"]/div/div/div[5]/div/div/div/div/div[3]/div[4]/div[2]/div[15]/label',
                   'mathematics' : '//*[@id="app"]/div/div/div[5]/div/div/div/div/div[3]/div[4]/div[2]/div[15]/label',
                   'physics' : '/html/body/div[3]/div/div/div[5]/div/div/div/div/div[3]/div[4]/div[2]/div[16]/label',
                   'chemistry' : '/html/body/div[3]/div/div/div[5]/div/div/div/div/div[3]/div[4]/div[2]/div[6]/label'}

    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    driver.get("https://www.vedantu.com")
    
    try:
        def vedantu_login():
            driver.implicitly_wait(5)
            
            sign_in_button = driver.find_element_by_class_name("button button_button__2GW-o button--small button_buttonSmall__3aGZA     button--secondary button_buttonSecondary__10WYP Header_signInButton__2iDLl")
            driver.execute_script("arguments[0].click();", sign_in_button)
            
            email_box = driver.find_element_by_class_name('login-input-group')
            email_box.send_keys("sharadmamtaald@gmail.com")
            
            next_button = driver.find_element_by_class_name('common-bottom-btn')
            next_button.click()
            
            driver.implicitly_wait(5)
            
            password_box = driver.find_element_by_class_name('login-input-group')
            password_box.send_keys("#Shreeji@IITH24")
            
            driver.implicitly_wait(6)
            
            next_button_2 = driver.find_element_by_class_name('common-bottom-btn')
            driver.execute_script("arguments[0].click();", next_button_2)
     
        
        def vedantu_show_upcoming_sessions():
            vedantu_login()
            driver.implicitly_wait(5)
           
    
            my_upcoming_sessions = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div/a[2]/div')
            my_upcoming_sessions.click()
            
            driver.implicitly_wait(5)
            
            for subject in user.split():
                if subject in batch_dict:
                    filter_button = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[3]')
                    filter_button.click()
                    
                    driver.implicitly_wait(3)
                    
                    clear_all_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[5]/div/div/div/div/div[3]/div[4]/div[1]/div[2]/span')
                    clear_all_button.click()
                    
                    driver.implicitly_wait(3)
                    
                    subject_button = driver.find_element_by_xpath(batch_dict[subject])
                    subject_button.click()
                    
                    driver.implicitly_wait(5)
                    
                    apply_button = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[5]/div/div/div/div/div[4]/div')
                    driver.execute_script("arguments[0].click();", apply_button)
          
        
        def vedantu_join_session():
            vedantu_show_upcoming_sessions()
            
            driver.implicitly_wait(5)
            
            join_button = driver.find_element_by_xpath("//*[contains(text(), 'Join Now')]")
            join_button.click()
            
            driver.implicitly_wait(5)
                        
            continue_button = driver.find_element_by_xpath('//*[@id="checkAudioAndVideo"]/div[3]')
            continue_button.click()

        

        for keyword in user.split():
            if keyword in ['login','sign in','signin']:
                vedantu_login()
             
            elif keyword in ['upcoming','sessions']:
                vedantu_show_upcoming_sessions()
                
            elif keyword in ['join','attend']:
                vedantu_join_session()

    except:
        pass



while True:
    print("Listening...")
    proto.say("What is the command boss ?")
    proto.runAndWait()
    with m as source: audio = r.listen(source)
    
    try:
        command = r.recognize_google(audio,language='en-in')
        command = command.lower()      
        print(f"COMMAND: {command}")
        
        end_conditions = ['exit' in command,'end this program' in command,'get lost' in command,
                          "get out" in command,'nothing' in command,'no more command' in command,
                          'bye' in command,'take rest' in command,'so jao' in command]        
        
        vedantu_conditions =  ['vedantu' in command,'sessions' in command,'session' in command]
    
    
        if any(end_conditions):
            print("OKAY BOSS..........\n CLOSING THE PROGRAM......")
            proto.say("OKAY BOSS..........\n CLOSING THE PROGRAM......")
            proto.runAndWait()
            break
    
        
        
        elif any(vedantu_conditions):
            print('proto : Okay boss. Just wait for 2 minutes.'.upper())
            proto.say('Okay boss. Just wait for 2 minutes. ')
            proto.runAndWait()
            
            vedantu(command)
            
            print('command_status : done'.upper())
            proto.say('Done boss.')
            proto.runAndWait()
            
        else:
            print('proto : don\'t know how to reply this. Try saying in another way.'.upper())
            proto.say('um...sorry boss...I  don\'t know how to reply this. Try saying in another way.')
            proto.runAndWait()
            
            
    except:
        print("Sorry , could not recognize")
        proto.say("sorry, could not recognize")
        proto.runAndWait()








# driver = webdriver.Chrome("C:\\chromedriver.exe")
# driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")

# # sign_in_button = driver.find_element_by_xpath('//*[@id="gb"]/div/div[2]/a')
# # sign_in_button.click()

# email_id_box = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
# email_id_box.send_keys('Proto.newoix@gmail.com')

# driver.implicitly_wait(5)

# next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
# next_button.click()

# driver.implicitly_wait(5)

# password_box = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
# password_box.send_keys('#GodSikhu@24')

# next_button = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
# next_button.click()

# driver.implicitly_wait(5)

# driver.execute_script('window.open ("time", "new window")')
# driver.switch_to_window(driver.window_handles[1])

# driver.execute_script('window.open ("https://www.youtube.com", "new window")')
# driver.switch_to_window(driver.window_handles[1])
# driver.find_element_by_xpath('/html/body').send_keys(Keys.CONTROL+'t')
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'t')


# driver.get("https://meet.google.com/map-idyv-fop")


# driver = webdriver.Chrome("C:\\chromedriver.exe")
# driver.get("https://meet.google.com/map-idyv-fop")

# sign_in_button = driver.find_element_by_xpath('//*[@id="gb"]/div/div[2]/a')
# sign_in_button.click()

# email_id_box = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
# email_id_box.send_keys('tiwarishreeji@gmail.com')

# next_button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
# next_button.click()

# driver.implicitly_wait(5)

# password_box = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
# password_box.send_keys('proto@3.0')

# next_button = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
# next_button.click()