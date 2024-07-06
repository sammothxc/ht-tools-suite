Tools for Hitmen to make our jobs more efficient and easier.

# Setup
## Development Status
✅ = Works as intended

⚠️ = Works with minor issues

❌ = Does not work

|          |report-accts|report-posts|scroll-reels|
| -------- |   :-----:  |  :------:  |   :-----:  |
| Chrome   |     ⚠️      |      ❌    |     ✅     |
| Firefox  |     ⚠️      |      ❌    |     ⚠️      |
| Safari   |     ⚠️      |      ❌    |     ✅     |
| Edge     |     ⚠️      |      ❌    |     ✅     |

### TODO
- [ ] Fix post element locations in report-posts.py
- [ ] Add CP option to report-posts.py
- [ ] GUI for easier use
- [ ] Build exeutables for Windows/Mac/Linux platforms


## Dependencies
CLone the repository and run the following commands to install the necessary dependencies.

Linux and Mac:
```
python3 -m venv venv

source venv/bin/activate

pip3 install pyautogui

pip3 install webbot
```

Windows: 
```
py -m venv venv

venv\Scripts\activate

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
To auto report all users listed in acc.txt, run `python3 report-accts.py`

To auto report specific posts for users listed in ac.txt, run `python3 report-posts.py`

To auto scroll through Instagram reels to avoid bot detection, run `python3 scroll-reels.py` WHILE YOU ARE AFK.
Note: Once it navigates to the reels page, you may have to click to focus the window and scroll once to initiate the auto scrolling.

Linux users: If you get an error complaining about the display or priveledges, run `xhost +local:$USER`

#### Let the magic begin
