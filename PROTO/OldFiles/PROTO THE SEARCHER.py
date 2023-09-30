from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


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

for i in range(5):
    user_input = input("What you waana search on youtube : ")
    # ip = input()


    # def YouTube_Search(querry):
        
    #         driver.get("https://www.youtube.com/results?search_query="+user_input)
            
    #         search_box = driver.find_element_by_xpath('//*[@id="search"]')
            
    #         search_box.send_keys(querry)
            
    #         search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
    #         search_button.click()
    
    querry = "https://www.youtube.com/results?search_query="+user_input
    if bool(user_input) == True:

    #     YouTube_Search(user_input)
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(querry)
    
