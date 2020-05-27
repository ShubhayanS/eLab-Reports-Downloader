from selenium import webdriver

from urllib.parse import quote   

import re
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep

#URL for OS elab. Change the url below for other eLabs
url = 'https://care.srmist.edu.in/srmos/login'


driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(60)


#Type your Registration ID within quotes below
user = sys.argv[1]
print("Registration Number is - ",user)

#Type your Password within quotes below instead of ???
pw = sys.argv[2]
print("Your Pw is - ",pw)

#DONOT Change anything after this point!
s=".mat-input-element"
obj= driver.find_elements_by_css_selector(s)
print(obj)
c=0
for i in obj:
    #print(i)
    if(c==0):
        i.send_keys(user)
        c=1
    else:
        i.send_keys(pw)

btn = driver.find_element_by_xpath("/html/body/app-root/div/app-login/div/mat-card/div[2]/form/button")

        
btn.click()

status = driver.find_element_by_xpath("/html/body/app-root/div/app-student-home/div/mat-card/div/div/app-student-home-card/mat-card")
status.click()

qp = driver.find_element_by_css_selector('#svgChart > g > g:nth-child(4) > path:nth-child(1)')

qp.click()

prev = driver.find_element_by_xpath("/html/body/app-root/div/app-student-solve/div[1]/button[1]") 

ct=100
for i in range(100):
    print("I am in question number ",ct)
    ct=ct-1
    sleep(3)
    try:
        evaluate = driver.find_element_by_xpath("/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[3]/button[2]")
        sleep(10)
        evaluate.click()
        result = driver.find_elements_by_xpath("/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[4]/a[1]")
        txt = result[0].text        
        print("C ",txt,"@")
        sleep(5)
        if(txt == 'RESULT - 100%'):
            report = driver.find_element_by_xpath("/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[4]/a[2]")
            report.click()
            sleep(10)
            prev.click()
        else:
            trigger = driver.find_element_by_xpath("/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[1]/mat-form-field/div/div[1]/div/mat-select/div")
            trigger.click()
            cpp = driver.find_elements_by_css_selector(".mat-select-panel .mat-optgroup-label, .mat-select-panel .mat-option")
            opt = 0
            for j in cpp:
                if(opt!=0):
                    j.click()
                else:
                    opt = 1
            sleep(5)
            evaluate = driver.find_element_by_xpath("/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[3]/button[2]")
            sleep(10)
            evaluate.click()
            result = driver.find_elements_by_xpath("/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[4]/a[1]")
            txt = result[0].text
            print("CPP ", txt)
            if(txt == 'RESULT - 100%'):
                report = driver.find_element_by_xpath("/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[4]/a[2]")
                sleep(5)
                report.click()
                sleep(10)
                prev.click()
                #break
            else:
                print("Question not evaluated fully in C or C++")
                prev.click()
    except:
        print("Unknown Error")
