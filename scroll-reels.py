import time
import argparse
import sys
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

## Get the options from the command line
def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="This bot helps users avoid automation detection features of instagram by scrolling thru reels.")
    parser.add_argument("-u", "--user", type = str, default = "usr.txt", help = "Instagram User(s) to report posts from (Defaults to usr.txt).")
    options = parser.parse_args(args)
    return options

def main():
    ## Get user credentials
    args = getOptions()
    usr_file = args.user

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

    ## Open web browser
    web = webdriver.Chrome()
    web.implicitly_wait(10)

    try:
        web.get("https://www.instagram.com/accounts/login/")
        assert "Instagram" in web.title
        print("Successfully opened the web browser.")
    except:
        print("ERROR: Failed to open the web browser.")
        exit(2)
    
    ## Login
    print("Entering username...")
    elem_user = web.find_element(By.NAME, "username")
    elem_user.send_keys(un)
    print("Entering password...")
    elem_pass = web.find_element(By.NAME, "password")
    elem_pass.send_keys(pw)
    print("Logging in...")
    time.sleep(0.3)
    elem_pass.send_keys(Keys.ENTER)
    time.sleep(4)
    print("Logged in.")

    ## Navigate to reels
    web.get("https://www.instagram.com/reels/")
    time.sleep(4)

    ## Scroll through reels
    SCROLL_PAUSE_TIME = 0.5
    while True:
        html = web.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.PAGE_DOWN)
        time.sleep(random.randrange(2, 10))

if '__main__':
    main()