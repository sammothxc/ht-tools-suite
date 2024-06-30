# Setup

## Dependencies
```
python3 -m venv ~/autoreport

bin/pip3 install pyautogui

bin/pip3 install webbot
```

## Files
Create `acc.txt` and fill it with burner accounts and their respective passwords following the style in `acc-example.txt`
Create `usr.txt` and fill it with accounts you want to report following the style in `usr-example.txt`

## Usage
Run`bin/python3 report-bot.py`

If you get an error complaining about the display or priveledges, run `xhost +local:$USER`

#### Let the magic begin
