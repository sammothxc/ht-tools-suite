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
TODO
```

## Files
Create `acc.txt` and fill it with burner accounts and their respective passwords following the style in `acc-example.txt`

Create `usr.txt` and fill it with accounts you want to report following the style in `usr-example.txt`

## Usage
Run`bin/python3 report-bot.py`

Linux users: If you get an error complaining about the display or priveledges, run `xhost +local:$USER`

#### Let the magic begin
