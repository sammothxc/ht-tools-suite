Tool for reporting explicit accounts on instagram under the 'Nudity or Sexual Activity' category.

# Setup
Tested on Linux and Mac, theoretically works on Windows but making python work is all up to you.

## Dependencies
Linux and Mac:
```
python3 -m venv ~/autoreport

bin/pip3 install pyautogui

bin/pip3 install webbot
```

Windows: 
```
py -m venv ~/autoreport

py -m pip install pyautogui

py -m pip install webbot
```

## Files
Create `acc.txt` and fill it with burner accounts and their respective passwords following the format in `acc-example.txt`

Create `usr.txt` and fill it with the direct link to accounts you want to report following the format in `usr-example.txt`

## Usage
To auto report all users listed in acc.txt, run `bin/python3 report-accts.py`
To auto report specific posts for users listed in ac.txt, run `bin/python3 report-posts.py`

Linux users: If you get an error complaining about the display or priveledges, run `xhost +local:$USER`

#### Let the magic begin
