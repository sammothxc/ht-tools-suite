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

    parser = argparse.ArgumentParser(description="This bot helps users to mass report posts of objectionable material.")
    parser.add_argument("-u", "--usernames", type = str, default = "usr.txt", help = "Usernames to report posts on ( Defaults to usr.txt in program directory ).")
    parser.add_argument("-a", "--accounts", type = str, default = "acc.txt", help = "Accounts list ( Defaults to acc.txt in program directory ).")

    options = parser.parse_args(args)

    return options

########## Instagram Post XPATH Layout
# /html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/div[2]/div/div[(ROW #)]/div[(COL 1-3)]
def reportPost(row, col):
    post = web.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/div[2]/div/div[{row}]/div[{col}]')
    clickElement(post)
    optionDots = web.find_element(By.XPATH, '/html/body/div[8]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/div/div/div')
    clickElement(optionDots)
    reportOption = web.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[1]')
    clickElement(reportOption)
    reportType = web.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[2]/div')
    clickElement(reportType)
    reportType2 = web.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/fieldset/div[1]/div/div/input')
    clickElement(reportType2)
    submitReport = web.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[6]/button')
    clickElement(submitReport)
    close = web.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div[4]/button')
    clickElement(close)
    return None

def clickElement(elem):
    ActionChains(web).click(elem).perform()
    return None

args = getOptions()

usr_file = args.usernames
acc_file = args.accounts

try:
    u = open(usr_file, "r").readlines()
    u_file = [s.rstrip()for s in u]
except FileNotFoundError:
    print("ERROR: no usr.txt file found")
    exit(2)

try:
    a = open(acc_file, "r").readlines()
    a_file = [s.rstrip()for s in a]
    a_file.reverse()
except FileNotFoundError:
    print("ERROR: no acc.txt file found")
    exit(2)

user = []
passw = []

web = webdriver.Firefox()
web.implicitly_wait(10)

for lines in a_file:
    a_file = lines.split(":")

    try:
        un = a_file[0]
        pw = a_file[1]
    except IndexError:
        print("ERROR: Wrong syntax in acc.txt")
    user.append(un)
    passw.append(pw)

for line in range(len(a_file)+1):
    try:
        web.get("https://www.instagram.com/accounts/login/")
        assert "Instagram" in web.title
    except:
        print("ERROR: Failed to open the web browser.")
        break
    
    elem_user = web.find_element(By.NAME, "username")
    elem_user.send_keys(user[line])
    time.sleep(0.7)
    elem_pass = web.find_element(By.NAME, "password")
    time.sleep(0.7)
    elem_pass.send_keys(passw[line])
    time.sleep(0.7)
    elem_pass.send_keys(Keys.ENTER)

    time.sleep(4)
    
    for username in u_file:
        
        web.implicitly_wait(10)

        web.get(username)

    row = 1
    col = 1
    while True:
        print("Post Position: ", row, col)
        print("Report post? (y)es / (n)o / (d)one")
        report = input()
        if report == "y":
            reportPost(row, col)
        elif report == "n":
            pass
        elif report == "d":
            break
        if col < 3:
            col += 1
        else:
            row += 1
            col = 1

        pyautogui.keyDown('ctrl')
        time.sleep(0.25)
        pyautogui.keyDown('w')
        time.sleep(0.5)
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('https://replit.com/@Cw')