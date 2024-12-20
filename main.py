from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#tthis is for webdriver add
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
#othership_stage url direct
driver.get("https://hwms-stage.othership.com/")
#email field find using full x path ( copy the full ex path from chorme)
input_element = driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div/div/input")
input_element.send_keys("rafsun.sqa@gmail.com" + Keys.ENTER )
time.sleep(10)
input_element = driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div/div/div/input")
input_element.send_keys("Stage_Password@1" + Keys.ENTER)
time.sleep(10)
input_element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div[3]/div/button[1]")






#time how much the windows will stay open - 10000= 166 min, 1000 = 16 min 100 = 1 mn 40 sc
time.sleep(10000)



