import subprocess
import keyboard
import mouse
import time

# "C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=league_of_legends --launch-patchlien=live
# open Riot Client


def open_riotclient():
    print("hotkey is running!")
    subprocess.Popen(
        [
            "C:\\Riot Games\\Riot Client\\RiotClientServices.exe",
            "--launch-product=league_of_legends",
            "--launch-patchline=live",
        ],
        
    )

# log me to league account


with open('database.txt', 'r') as files:
    lines = files.readlines()

if len(lines) >= 2:
    username = lines[0].strip()
    password = lines[1].strip()

    if len(lines) >= 4:
        username1 = lines[2].strip()
        password2 = lines[3].strip()



def account1():
    mouse.move(300, 350)
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    keyboard.write(username)
    mouse.move(300, 420)
    mouse.click()
    time.sleep(1)
    keyboard.write(password)
    mouse.move(400, 800)
    mouse.click()


def account2():
    mouse.move(300, 350)
    mouse.click()
    time.sleep(1)
    keyboard.write(username1)
    mouse.move(300, 420)
    mouse.click()
    time.sleep(1)
    keyboard.write(password2)
    mouse.move(400, 800)
    mouse.click()
