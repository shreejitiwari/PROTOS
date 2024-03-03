from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import chrome_driver_updater

chrome_driver_updater.update()

LOGIN_TRUE = 0

def login_to_amizone():
    global driver
    driver = webdriver.Chrome("D:\ChromeDriver\chromedriver.exe")
    driver.maximize_window()

    driver.get("https://s.amizone.net/")
    username = driver.find_element(By.NAME, "_UserName")
    username.clear()
    username.send_keys("10208361")
    amizone_password = driver.find_element(By.NAME, "_Password")
    amizone_password.clear()
    amizone_password.send_keys("49da32")
    login_button = driver.find_element(By.CLASS_NAME, "login100-form-btn")
    login_button.send_keys(Keys.ENTER)
    global LOGIN_TRUE
    LOGIN_TRUE = 1

def remove_popup():
    close_popup = driver.find_element(By.CSS_SELECTOR, "#MyPopup55 > div > div > div.modal-header > button")
    close_popup.send_keys(Keys.ENTER)



def go_home():
    home_button = driver.find_element(By.XPATH, "//a[contains(@href, '/Home/_Home')]")
    home_button.send_keys(Keys.ENTER)
    time.sleep(3)
    remove_popup()    

def show_time_table(day = str(datetime.now().strftime("%A"))):
    timetable_button = driver.find_element(By.CSS_SELECTOR, "#M10")
    timetable_button.send_keys(Keys.ENTER)
    time.sleep(2)
    day_button = driver.find_element(By.XPATH, f"//a[contains(@href,'#{day.title()}')]")
    day_button.send_keys(Keys.ENTER)

def show_attendance():
    driver.find_element(By.CSS_SELECTOR, '#donutchart > div > div:nth-child(1) > div > svg').click()
    
def close_attendance():
    close_btn = driver.find_element(By.CSS_SELECTOR, "#MBA85 > div > div > div > div.modal-header.bg-green.fg-white > button")
    close_btn.send_keys(Keys.ENTER)

def show_calendar():
    driver.find_element(By.CSS_SELECTOR, '#M2').click()

def show_courses():
    driver.find_element(By.CSS_SELECTOR, '#M18').click()

def show_faculty():
    driver.find_element(By.CSS_SELECTOR, '#M27').click()

def show_id():
    driver.find_element(By.CSS_SELECTOR, "#M83").click()

def show_faculty():
    driver.find_element(By.CSS_SELECTOR, "#M27").click()

# MAIN
while True :
    command = input("Enter your command : ").lower()

    end_conditions = ['exit' in command,'end this program' in command,'get lost' in command,
                        "get out" in command,'nothing' in command,'no more command' in command,
                        'bye' in command,'take rest' in command,'so jao' in command, 'tata' in command] 

        
    # login_conditions = ['amizone' in command, 'login' in command]

    if any(end_conditions):
        print('''
        Okay Boss ..!!
        Ending the program.
        ''')
        if LOGIN_TRUE==1:
            driver.close()
        break

    if "login" in command and LOGIN_TRUE==0:
        login_to_amizone()
        time.sleep(3)
        remove_popup()


    if any(['id' in command, 'identity' in command, 'card' in command, 'i\'d' in command]):
        if LOGIN_TRUE==0:
            login_to_amizone()
            time.sleep(3)
            remove_popup()
        show_id()

    if any(["faculty" in command, "teachers" in command, "faculties" in command]):
        if LOGIN_TRUE==0:
            login_to_amizone()
            time.sleep(3)
            remove_popup()        
        show_faculty()

    
    


    
    


# login_to_amizone()
# time.sleep(3)
# remove_popup()
# show_id()
# time.sleep(10)
# go_home()
# time.sleep(2)
# show_attendance()
# time.sleep(5)
# close_attendance()
# time.sleep(2)
# show_time_table('thursday')
# time.sleep(3)
# show_calendar()
# time.sleep(7)
# show_courses()
# time.sleep(10)
# show_faculty()
# time.sleep(10)
# go_home()
# time.sleep(5)
# show_time_table('friday')
# time.sleep(5)
# go_home()
# driver.close()