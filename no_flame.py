import keyboard
from league_hotkey import open_riotclient
from league_hotkey import account_logger
from league_hotkey import account_logger2

# change rude word to nice one
keyboard.add_abbreviation("rope", "it fine can win")
keyboard.add_abbreviation("boom", "HE HE HE AH ")
keyboard.add_abbreviation("low", "nice ")
keyboard.add_abbreviation("dog", "human ")
keyboard.add_abbreviation("kys", "Kai-wai ")


# add the hotkey
keyboard.add_hotkey("shift + C", open_riotclient)
keyboard.add_hotkey("shift + W", account_logger)
keyboard.add_hotkey("shift + X", account_logger2)

# make it so the .py don't finish
input("oui ")
