import time
import argparse
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

## Get the options from the command line
def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="This bot helps users to mass report accounts full of objectionable material.")
    parser.add_argument("-u", "--user", type = str, default = "usr.txt", help = "Instagram User(s) to report posts from (Defaults to usr.txt).")
    parser.add_argument("-a", "--accounts", type = str, default = "acc.txt", help = "Accounts to report (Defaults to acc.txt).")
    options = parser.parse_args(args)
    return options

## Click the element
def clickElement(elem, web):
    ActionChains(web).click(elem).perform()
    return None

def main():
    ## Load the usernames and accounts
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

    ## Login to the accounts
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
        
        ## Report the accounts
        for username in u_file:
            web.get(username)
            
            options = web.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[2]/div/div/div[3]/div')
            clickElement(options, web)
            
            report = web.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/button[3]')
            clickElement(report, web)

            report2 = web.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[2]/div')
            clickElement(report2, web)

            report3 = web.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[1]/button[1]/div')
            clickElement(report3, web)

            report4 = web.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[1]/button[5]/div/div[1]')
            clickElement(report4, web)
            
            report5 = web.find_element(By.XPATH, '//*[@id="IGDSRadioButtontag-3"]')
            clickElement(report5, web)
            
            report6 = web.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[6]/button')
            clickElement(report6, web)

if '__main__':
    main()