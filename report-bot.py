import time
import pyautogui
import argparse
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def getOptions(args=sys.argv[1:]):

    parser = argparse.ArgumentParser(description="This bot helps users to mass report accounts with clickbaits or objectionable material.")
    parser.add_argument("-u", "--usernames", type = str, default = "usr.txt", help = "Usernames to report ( Defaults to usr.txt in program directory ).")
    parser.add_argument("-a", "--accounts", type = str, default = "acc.txt", help = "Accounts list ( Defaults to acc.txt in program directory ).")

    options = parser.parse_args(args)

    return options

args = getOptions()

usr_file = args.usernames
acc_file = args.accounts

u = open(usr_file, "r").readlines()
u_file = [s.rstrip()for s in u]
u_file.reverse()

a = open(acc_file, "r").readlines()
a_file = [s.rstrip()for s in a]
a_file.reverse()

for username in u_file:
    user = []
    passw = []
    for lines in a_file:
        a_file = lines.split(":")

        un = a_file[0]
        pw = a_file[1]
        user.append(un)
        passw.append(pw)

    for line in range(len(a_file)+1):
        web = webdriver.Chrome()

        web.get("https://www.instagram.com/accounts/login/")
        assert "Instagram" in web.title

        time.sleep(1.5)

        elem_user = web.find_element(By.NAME, "username")
        elem_user.send_keys(user[line])
        time.sleep(0.7)
        elem_pass = web.find_element(By.NAME, "password")
        time.sleep(0.7)
        elem_pass.send_keys(passw[line])
        time.sleep(0.7)
        elem_pass.send_keys(Keys.ENTER)

        time.sleep(2.5)

        web.get("https://www.instagram.com/%s/" % username) # TO-DO: use links directly

        time.sleep(2.5)

        options = web.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[2]/div/div/div[3]/div')
        
        ActionChains(web)\
            .click(options)\
            .perform()
        
        time.sleep(2)

        report = web.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/button[3]')
        
        ActionChains(web)\
            .click(report)\
            .perform()

        time.sleep(2)

        report2 = web.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[2]/div')
        
        ActionChains(web)\
            .click(report2)\
            .perform()

        time.sleep(200)

        report3 = web.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[2]/div')
        
        ActionChains(web)\
            .click(report3)\
            .perform()

        web.click(text='Log Out')

        time.sleep(0.5)

        pyautogui.keyDown('ctrl')
        time.sleep(0.25)
        pyautogui.keyDown('w')
        time.sleep(0.5)
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('https://replit.com/@Cw')
    