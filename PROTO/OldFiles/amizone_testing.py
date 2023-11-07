from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import chrome_driver_updater 




class amizone:
    def __init__(self) -> None:
        chrome_driver_updater.update()
        self.driver =  webdriver.Chrome("D:\ChromeDriver\chromedriver.exe")
        self.login_done = False
        self.on_home_page = False
        self.attendance_on = False
        # pass

    def close_browser(self):
        self.driver.close()

    def remove_popup(self):
        close_popup = self.driver.find_element(By.CSS_SELECTOR, "#ModalPopApp > div > div > div.modal-footer > button")
        close_popup.send_keys(Keys.ENTER)
        self.login_done = True
        self.on_home_page = True
        

    def login_to_amizone(self):
        # global self.self.driver
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

        self.driver.get("https://s.amizone.net/")
        username = self.driver.find_element(By.NAME, "_UserName")
        username.clear()
        username.send_keys("10208361")
        amizone_password = self.driver.find_element(By.NAME, "_Password")
        amizone_password.clear()
        amizone_password.send_keys("49da32")
        login_button = self.driver.find_element(By.CLASS_NAME, "login100-form-btn")
        login_button.send_keys(Keys.ENTER)
        time.sleep(5)
        self.remove_popup()

    def go_home(self):
        home_button = self.driver.find_element(By.XPATH, "//a[contains(@href, '/Home/_Home')]")
        home_button.send_keys(Keys.ENTER)
        time.sleep(3)
        self.remove_popup()

    def show_time_table(self,day = str(datetime.now().strftime("%A"))):
        timetable_button = self.driver.find_element(By.CSS_SELECTOR, "#M10")
        timetable_button.send_keys(Keys.ENTER)
        time.sleep(2)
        day_button = self.driver.find_element(By.XPATH, f"//a[contains(@href,'#{day.title()}')]")
        day_button.send_keys(Keys.ENTER)
        self.on_home_page = False

    def show_attendance(self):
        self.driver.find_element(By.CSS_SELECTOR, '#donutchart > div > div:nth-child(1) > div > svg').click()
        self.on_home_page = False
        self.attendance_on = True

    def close_attendance(self):
        close_btn = self.driver.find_element(By.CSS_SELECTOR, "#MBA85 > div > div > div > div.modal-header.bg-green.fg-white > button")
        close_btn.send_keys(Keys.ENTER)
        self.on_home_page = True
        self.attendance_on = False

    def show_calendar(self):
        self.driver.find_element(By.CSS_SELECTOR, '#M2').click()
        self.on_home_page = False

    def show_courses(self):
        self.driver.find_element(By.CSS_SELECTOR, '#M18').click()
        self.on_home_page = False

    def show_faculty(self):
        self.driver.find_element(By.CSS_SELECTOR, '#M27').click()
        self.on_home_page = False

    def show_id(self):
        self.driver.find_element(By.CSS_SELECTOR, "#M83").click()
        self.on_home_page = False




# MAIN

amz = amizone()
while True :
    command = input("Enter your command : ").lower()

    end_conditions = ['exit' in command,'end this program' in command,'get lost' in command,
                        "get out" in command,'nothing' in command,'no more command' in command,
                        'bye' in command,'take rest' in command,'so jao' in command, 'tata' in command] 

        
    # login_conditions = ['amizone' in command, 'login' in command]

    if any(end_conditions):
        amz.close_browser()
        print('''
        Okay Boss ..!!
        Ending the program.
        ''')
        time.sleep(10)
        exit()

    if "login" in command:
        if not amz.login_done:
            amz.login_to_amizone()

    if any(['home' in command, 'return' in command]):
        if not amz.login_done:
            amz.login_to_amizone()
            time.sleep(5)
            # amz.remove_popup()
            # time.sleep(3)
            # on_home_page = True

        elif not amz.on_home_page:
            amz.go_home()

    if 'attendance' in command and 'close' not in command:
        if not amz.login_done:
            amz.login_to_amizone()
            time.sleep(5)
            # time.sleep(3)
            # on_home_page = True

        if not amz.on_home_page:
            amz.go_home()

        if not amz.attendance_on:
            amz.show_attendance()    

        time.sleep(15)
        amz.close_attendance()
            # attendance off 

    if any(['id' in command, 'identity' in command, 'card' in command, 'i\'d' in command]):
        if not amz.login_done:
            amz.login_to_amizone()
            time.sleep(10)
            # amz.remove_popup()
            # time.sleep(3)
            # on_home_page = True

        if not amz.on_home_page:
            amz.go_home()

        amz.show_id()    

    if any(["faculty" in command, "teachers" in command, "faculties" in command]):
        if not amz.login_done:
            amz.login_to_amizone()
            time.sleep(5)
            # amz.remove_popup()
            # time.sleep(3)
            # on_home_page = True

        if not amz.on_home_page:
            amz.go_home()
        amz.show_faculty()

    
    if all(['close' in command, 'attendance' in command]):
        try:
            amz.close_attendance()
        except:
            pass

        


# login_to_amizone()
# time.sleep(3)
# remove_popup()
# time.sleep(3)
# show_id()
# show_attendance()
# time.sleep(5)
# close_attendance()
# time.sleep(2)
# show_time_table('thursday')
# time.sleep(3)
# show_calendar()
# time.sleep(7)
# show_courses()
# time.sleep(5)
# show_faculty()
# time.sleep(5)
# go_home()

# show_time_table('friday')
# time.sleep(5)
# go_home()
# self.driver.close()