from selenium.webdriver.chrome import options
from selenium import webdriver  
from selenium.webdriver.common.by import By
import time  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client

def sendvineet():
    account_sid = 'ACdec1fc4ec94011e54ed96cbadceddef4' 
    auth_token = '611d6cc9e47471c342346247897b8de0' 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create(  
                                messaging_service_sid='MG6897347b3330780ef47e51d003706a95', 
                                body='Vikram: Bro SLot is Open',      
                                to='+918827015401' 
                            ) 
    
    print(message.sid)
    
def sendvikram():
    account_sid = 'AC2e233b29ea3bc7156b7d16480fd6224b' 
    auth_token = 'aac7afc7c6365baa82a09e4096cba53e' 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create(  
                                messaging_service_sid='MG4c155bd3ec2f584ba631da8455e1293b', 
                                body='hihihi',      
                                to='+919893781339' 
                            ) 
    
    print(message.sid)

class vfs:
    def __init__(self):
        self.url = "https://visa.vfsglobal.com/ind/en/pol/login"
        Firefox_options = webdriver.FirefoxOptions()
        # Firefox_options.add_argument("--headless")
        # Firefox_options.add_argument("--disable-dev-shm-usage")
        # Firefox_options.add_argument("--no-sandbox")
        self.driver = driver = webdriver.Firefox(options=Firefox_options,executable_path=r"C:/Users/VIKRAM/Downloads/geckodriver-v0.30.0-win64\geckodriver.exe")
        # self.driver.fullscreen_window()
    def sendvineet():
        account_sid = 'ACdec1fc4ec94011e54ed96cbadceddef4' 
        auth_token = '611d6cc9e47471c342346247897b8de0' 
        client = Client(account_sid, auth_token) 

        message = client.messages.create(  
                                    messaging_service_sid='MG6897347b3330780ef47e51d003706a95', 
                                    body='Vikram: Bro SLot is Open',      
                                    to='+918827015401' 
                                ) 

        print(message.sid)
    
    def sendvikram():
        account_sid = 'AC2e233b29ea3bc7156b7d16480fd6224b' 
        auth_token = 'aac7afc7c6365baa82a09e4096cba53e' 
        client = Client(account_sid, auth_token) 
        
        message = client.messages.create(  
                                    messaging_service_sid='MG6897347b3330780ef47e51d003706a95', 
                                    body='Vikram: Bro SLot is Open',      
                                    to='+918827015401' 
                                ) 
        
        print(message.sid)
    
    def login(self):
        self.driver.get(self.url)
        time.sleep(5)
        
        username = "vikramiiitmc@gmail.com"
        password = "Lhm@57284"
        time.sleep(3)
        username_field = self.driver.find_element(By.XPATH,'//*[@id="mat-input-0"]').send_keys(username)
        password_field = self.driver.find_element(By.XPATH,'//*[@id="mat-input-1"]').send_keys(password)

        # login
        login = True
        
        while login:
            try:
                if self.driver.current_url == "https://visa.vfsglobal.com/ind/en/pol/dashboard":
                    print("Login Success")
                    break
                else:
                    login_css = "/html/body/app-root/div/app-login/section/div/div/mat-card/form/button"
                    login_element = self.driver.find_element(By.XPATH,login_css).is_displayed()
                    self.driver.find_element(By.XPATH,login_css).click()
                    time.sleep(1)
                    self.driver.find_element(By.XPATH,login_css).click()
                    time.sleep(.2)
                    self.driver.find_element(By.XPATH,login_css).click()
                    print("clicked login")
            except:
                pass          
            time.sleep(2)    
        # Click New Booking
        time.sleep(3)
        self.driver.find_element(By.XPATH,'/html/body/app-root/div/app-dashboard/section/div/div[2]/button').click()
        print("start new booking")
        
        time.sleep(3)
        
        # applicatiopn
        
        self.driver.find_element(By.XPATH,'//*[@id="mat-select-value-1"]').click()
        time.sleep(3)
        # /html/body/div[5]/div[2]/div/div/div/mat-option[9]/span
        element = self.driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/div/div/mat-option[9]/span')
        self.driver.execute_script("arguments[0].click();",element)
        
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="mat-select-value-3"]').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/div/div/mat-option[1]/span').click()
        
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,'//*[@id="mat-select-value-5"]').click()
        # self.driver.find_element(By.XPATH,'//*[@id="mat-option-9"]').click()
        time.sleep(5)
        status = ""
        try:
            status = self.driver.find_element(By.XPATH,'/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[4]')
            status.text
            print(status.text)
            status = status.text
            # self.sendvineet()
            # self.sendvikram()
            # print("called twilio")
        except:
            pass
        print(status)
        if status != "No appointment slots are currently available":
            sendvikram()
            sendvineet()
            print("\nstatus : ",status," Msg sent")
        
        return status
    
    def close(self):
        self.driver.close()
            
VFS = vfs()
VFS.login()
VFS.close()
# vineet
# 611d6cc9e47471c342346247897b8de0
# vikram
# aac7afc7c6365baa82a09e4096cba53e
# ot-sdk-eight ot-sdk-columns