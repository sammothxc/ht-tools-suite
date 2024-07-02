Tool for reporting explicit accounts on instagram under the 'Nudity or Sexual Activity' category.

# Setup
Tested on Linux and Mac, theoretically works on Windows.

## Dependencies
Linux and Mac:
```
python3 -m venv ~/hitman-tools

bin/pip3 install pyautogui

bin/pip3 install webbot
```

Windows: 
```
py -m venv ~/hitman-tools

py -m pip install pyautogui

py -m pip install webbot
```

## Files
Create `usr.txt` and fill it with burner accounts (at least 1 account) and their respective passwords following the format:
```
username1:password1
username2:password2
username3:password3
...
```

Create `acc.txt` and fill it with the direct link to accounts you want to report following the format:
```
https://www.instagram.com/username1/
https://www.instagram.com/username2/
https://www.instagram.com/username3/
...
```

## Usage
To auto report all users listed in acc.txt, run `bin/python3 [your browser]/report-accts.py`

To auto report specific posts for users listed in ac.txt, run `bin/python3 [your browser]/report-posts.py`

To auto scroll through Instagram reels to avoid bot detection, run `bin/python3 [your browser]/scroll-reels.py`

Linux users: If you get an error complaining about the display or priveledges, run `xhost +local:$USER`

#### Let the magic begin
