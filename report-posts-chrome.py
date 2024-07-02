import time
import argparse
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

## Get options from command line
def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="This bot helps users to mass report posts of objectionable material.")
    parser.add_argument("-u", "--user", type = str, default = "usr.txt", help = "Instagram User(s) to report posts from (Defaults to usr.txt).")
    parser.add_argument("-a", "--accounts", type = str, default = "acc.txt", help = "Accounts to report (Defaults to acc.txt).")
    options = parser.parse_args(args)
    return options

## Report the post
def reportPost(web):
    optionDots = web.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/div/div/div/div')
    clickElement(optionDots, web)
    reportOption = web.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[1]')
    clickElement(reportOption, web)
    reportType = web.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[2]/div')
    clickElement(reportType, web)
    reportType2 = web.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/fieldset/div[1]/div/div/input')
    clickElement(reportType2, web)
    submitReport = web.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[6]/button')
    clickElement(submitReport, web)
    close = web.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div[4]/button')
    clickElement(close, web)
    return None

## Go to the next post
def nextPost(web):
    try:
        nextButton = web.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button')
        clickElement(nextButton, web)
        return True
    except:
        return False
    
## Click the element
def clickElement(elem, web):
    ActionChains(web).click(elem).perform()
    return None

def main():
    ## Load the usernames and accounts
    args = getOptions()
    usr_file = args.user
    acc_file = args.accounts
    user = []
    passw = []

    try:
        a = open(acc_file, "r").readlines()
        a_file = [s.rstrip()for s in a]
    except FileNotFoundError:
        print("ERROR: no acc.txt file found")
        exit(2)

    try:
        u = open(usr_file, "r").readlines()
        u_file = [s.rstrip()for s in u]
    except FileNotFoundError:
        print("ERROR: no usr.txt file found")
        exit(2)

    for lines in u_file:
        u_file = lines.split(":")
        try:
            un = u_file[0]
            pw = u_file[1]
        except IndexError:
            print("ERROR: Wrong syntax in usr.txt")
        user.append(un)
        passw.append(pw)

    ## Login to the accounts
    web = webdriver.Chrome()
    web.implicitly_wait(10)

    for line in range(len(u_file)+1):
        print("Logging in as " + user[line])
        try:
            web.get("https://www.instagram.com/accounts/login/")
            assert "Instagram" in web.title
            print("Successfully opened the web browser.")
        except:
            print("ERROR: Failed to open the web browser.")
            exit(2)
        
        time.sleep(0.25)
        print("Entering username...")
        elem_user = web.find_element(By.NAME, "username")
        elem_user.send_keys(user[line])
        time.sleep(0.25)
        print("Entering password...")
        elem_pass = web.find_element(By.NAME, "password")
        elem_pass.send_keys(passw[line])
        time.sleep(0.25)
        print("Logging in...")
        elem_pass.send_keys(Keys.ENTER)
        time.sleep(4)
        print("Logged in.")
        
        ## Cycle through the posts
        for accounts in a_file:
            print("Reporting posts from: " + accounts)
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