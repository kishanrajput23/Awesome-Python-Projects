from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


search = input('Enter the name of reciever: ')
message = input('Enter the message: ')
count = int(input('Enter the number of times the mesage should be sent: '))


class WhatsppBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        #options.binary_location = webdriver.ChromeOptions()
        #options.binary_location = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"
        #chrome_driver_binary = "C:\\Users\muz\AppData\Local\Programs\Python\Python36-32\Scripts\chromedriver.exe"
        
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get('https://web.whatsapp.com/')
        sleep(25)
        self.driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]").send_keys(search,Keys.RETURN)
        messagebox = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        for n in range(count):
            sleep(1)
            messagebox.send_keys(message, Keys.RETURN)
    
bot=WhatsppBot()       