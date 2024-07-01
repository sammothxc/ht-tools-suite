import time
import argparse
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def getOptions(args=sys.argv[1:]):

    parser = argparse.ArgumentParser(description="This bot helps users to mass report posts of objectionable material.")
    parser.add_argument("-u", "--user", type = str, default = "usr.txt", help = "Instagram User(s) to report posts from (Defaults to usr.txt).")
    parser.add_argument("-a", "--accounts", type = str, default = "acc.txt", help = "Accounts to report (Defaults to acc.txt).")
    options = parser.parse_args(args)
    return options

def reportPost(web):
    optionDots = web.find_element(By.XPATH, '/html/body/div[8]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/div/div/div')
    clickElement(optionDots, web)
    reportOption = web.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[1]')
    clickElement(reportOption, web)
    reportType = web.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[2]/div')
    clickElement(reportType, web)
    reportType2 = web.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/fieldset/div[1]/div/div/input')
    clickElement(reportType2, web)
    submitReport = web.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[6]/button')
    clickElement(submitReport, web)
    close = web.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div[4]/button')
    clickElement(close, web)
    return None

def nextPost(web):
    try:
        nextButton = web.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button')
        clickElement(nextButton, web)
        return True
    except:
        return False
    
def clickElement(elem, web):
    ActionChains(web).click(elem).perform()
    return None

def main():
    args = getOptions()
    usr_file = args.user
    acc_file = args.accounts

    try:
        a = open(acc_file, "r").readlines()
        a_file = [s.rstrip()for s in a]
    except FileNotFoundError:
        print("ERROR: no acc.txt file found")
        exit(2)

    try:
        with open(usr_file, "r") as pass_file:
            u_file = pass_file.read().split(":")
    except FileNotFoundError:
        print("ERROR: no usr.txt file found")
        exit(2)

    try:
        un = u_file[0]
        pw = u_file[1]
    except IndexError:
        print("ERROR: wrong syntax in usr.txt")
        exit(2)

    web = webdriver.Firefox()
    web.implicitly_wait(10)

    try:
        web.get("https://www.instagram.com/accounts/login/")
        assert "Instagram" in web.title
    except:
        print("ERROR: Failed to open the web browser.")
        exit(2)
    
    elem_user = web.find_element(By.NAME, "username")
    elem_user.send_keys(un)
    elem_pass = web.find_element(By.NAME, "password")
    elem_pass.send_keys(pw)
    time.sleep(0.3)
    elem_pass.send_keys(Keys.ENTER)
    time.sleep(4)
    
    for accounts in a_file:
        web.get(accounts)
        firstPost = web.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/div[2]/div/div[1]/div[1]')
        clickElement(firstPost, web)
        while True:
            print("Report post? (y) / n")
            report = input()
            if report == "n":
                if not nextPost(web):
                    break
            else:
                reportPost(web)
                if not nextPost(web):
                    break

if '__main__':
    main()