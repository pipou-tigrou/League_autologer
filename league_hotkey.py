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


with open('database.txt', 'r') as fichier:
    lignes = fichier.readlines()

if len(lignes) >= 4:
    username = lignes[0].strip()
    password = lignes[1].strip()
    username1 = lignes[2].strip()
    password2 = lignes[3].strip()


def account_logger():
    mouse.move(300, 350)
    mouse.click()
    time.sleep(1)
    keyboard.write(username)
    mouse.move(300, 420)
    mouse.click()
    time.sleep(1)
    keyboard.write(password)
    mouse.move(400, 800)
    mouse.click()


def account_logger2():
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


def account1():
    subprocess.Popen(
        [
            "C:\\Riot Games\\Riot Client\\RiotClientServices.exe",
            "--launch-product=league_of_legends",
            "--launch-patchline=live",
        ],

    )
    time.sleep(7)

    mouse.move(300, 350)
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
    subprocess.Popen(
        [
            "C:\\Riot Games\\Riot Client\\RiotClientServices.exe",
            "--launch-product=league_of_legends",
            "--launch-patchline=live",
        ],

    )
    time.sleep(7)

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
