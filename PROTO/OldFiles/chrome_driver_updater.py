def update():
    from webdriver_auto_update.webdriver_auto_update import WebdriverAutoUpdate
    driver_directory = "D:\ChromeDriver"
    driver_manager = WebdriverAutoUpdate(driver_directory)
    driver_manager.main()