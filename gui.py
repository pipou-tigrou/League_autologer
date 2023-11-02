import customtkinter
from league_hotkey import account1
from league_hotkey import account2


def add_username():
    user_input = entry1.get()
    with open("database.txt", "a") as file:
        file.write(user_input + "\n")
        entry1.delete(0, "end")


def add_password():
    user_input = entry2.get()
    with open("database.txt", "a") as file:
        file.write(user_input + "\n")
        entry2.delete(0, "end")


def add_account():
    add_username()
    add_password()


def check_first_line():
    with open('database.txt', 'r') as file:
        first_line = file.readline().strip()  # Lire et supprimer les espaces inutiles

        if first_line:  # Vérifie si la première ligne n'est pas vide
            button1.pack(pady=4, padx=4)
        root.after(1000, check_first_line)


def check_from_line_3():
    with open('database.txt', 'r') as file:
        lines = file.readlines()
        if len(lines) > 2:
            button2.pack()
        root.after(1000, check_from_line_3)


def toomutchaccount():
    with open('database.txt', 'r') as file:
        lines = file.readlines()
        if len(lines) > 4:
            label2 = customtkinter.CTkLabel(master=frame, text="max account is 2", font=("Roboto", 24), text_color="red")
            label2.pack(pady=15, padx=10)
        root.after(1000, toomutchaccount)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("350x400")
root.title("League Logger")
root.iconbitmap("normal.ico")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="add account", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="UserName")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="add", command=add_account)
button.pack(pady=15, padx=10)

button1 = customtkinter.CTkButton(master=frame, text="account1", command=account1)
check_first_line()

button2 = customtkinter.CTkButton(master=frame, text="account2", command=account2)
check_from_line_3()

toomutchaccount()

root.mainloop()
