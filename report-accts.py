import time
import argparse
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

## Get the options from the command line
def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="This bot helps users to mass report accounts full of objectionable material.")
    parser.add_argument("-u", "--user", type = str, default = "usr.txt", help = "Instagram User(s) to report posts from (Defaults to usr.txt).")
    parser.add_argument("-a", "--accounts", type = str, default = "acc.txt", help = "Accounts to report (Defaults to acc.txt).")
    options = parser.parse_args(args)
    return options

## Choose the browser
def chooseBrowser():
    print("(c)hrome (f)irefox (s)afari (e)dge")
    report = input()
    if report == "c":
        return webdriver.Chrome()
    elif report == "f":
        return webdriver.Firefox()
    elif report == "s":
        return webdriver.Safari()
    elif report == "e":
        return webdriver.Edge()
    else:
        print("Invalid browser choice. Defaulting to Chrome.")
        return webdriver.Chrome()

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
            print("ERROR: Wrong syntax in acc.txt")
        user.append(un)
        passw.append(pw)

    ## Login to the accounts
    web = chooseBrowser()
    web.implicitly_wait(10)

    for line in range(len(u_file)+1):
        print("Logging in as " + user[line])
        try:
            web.get("https://www.instagram.com/accounts/login/")
            assert "Instagram" in web.title
        except:
            print("ERROR: Failed to open the web browser.")
            break

        ## Refuse cookies
        try:
            print("Refusing Cookies...")
            WebDriverWait(web, 5).until(EC.element_to_be_clickable((By.XPATH,\
                '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]'))).click()
        except:
            pass
        
        elem_user = web.find_element(By.NAME, "username")
        elem_user.send_keys(user[line])
        time.sleep(0.7)
        elem_pass = web.find_element(By.NAME, "password")
        time.sleep(0.7)
        elem_pass.send_keys(passw[line])
        time.sleep(0.7)
        elem_pass.send_keys(Keys.ENTER)
        time.sleep(5)
        
        ## Report the accounts
        for accounts in a_file:
            web.get(accounts)
            
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
            time.sleep(1)

if '__main__':
    main()