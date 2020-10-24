from selenium import webdriver
from datetime import datetime
import time

import datetime

first_time = datetime.datetime.now()

print(first_time)


year = int(input('enter year: '))
month = int(input('enter month: '))
day = int(input('enter day: '))
hours = int(input('enter hours: '))
min = int(input('enter min: '))
sec = int(input('enter sec: '))



later_time = datetime.datetime(year,month,day,hours,min,sec)

# print()


driver = webdriver.Chrome(r'c:\Users\<INSERT YOUR USERNAME HERE>\Desktop\chromedriver')
driver.get('http://web.whatsapp.com')


name = input('Enter the name of user or group : ')
msg = input('Enter the message : ')
count = int(input('Enter the count : '))

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
print(user)
print('\n\n\n')
user.click()

msg_box = driver.find_element_by_class_name('_1Plpp')

first_time = datetime.datetime.now()

print(first_time)

sec = (later_time-first_time).total_seconds()
print(sec)

time.sleep(sec)

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('_35EW6').click()






#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# import sys
# # Replace below path with the absolute path of the \
# #chromedriver in your computer
# driver = webdriver.Chrome(r'c:\Users\yashu\Desktop\chromedriver')
#
# driver.get("https://web.whatsapp.com/")
# # time.sleep()
# wait = WebDriverWait(driver, 600)
# # Replace 'My Bsnl' with the name of your friend or group name
# target = '"LOL"'
#
# # Replace the below string with your own message
# string = sys.argv[1]
#
# x_arg = '//span[contains(@title,' + target + ')]'
# group_title = wait.until(EC.presence_of_element_located((
# By.XPATH, x_arg)))
# print (group_title)
# print ("Wait for few seconds")
# group_title.click()
# message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
#
# message.send_keys(string)
# sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
# sendbutton.click()
# driver.close()
