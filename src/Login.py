import tkinter as tk
import Connection,Main_menu,Windows_1
import log
from PIL import Image, ImageTk
import random

def login ( ):


    def _user_check (text1):
        conn=Connection.Connect ()
        conn.autocommit=False
        cursor=conn.cursor ()
        query="SELECT id FROM Uzivatel where jmeno ='"+text1+"';"
        cursor.execute (query)
        result=cursor.fetchone ()
        user_id=result [0]
        return (user_id)

    text1 = username_entry.get()
    text2 = password_entry.get()

    conn = Connection.Connect()
    conn.autocommit = False

    cursor = conn.cursor()
    query = "SELECT heslo FROM Uzivatel where jmeno ='" + text1 + "';"
    cursor.execute(query)
    result = cursor.fetchone()
    heslo_db = result [0]
    password = text2

    if heslo_db==password:
        log.log_Info("login","uzivatel: "+text1+" se přihlásil")
        login_w.destroy()
        Main_menu.start(_user_check (text1))
    else:
        log.log_Info("login","uzivatel: "+text1+" se pokusil přihlásit ale nepodařilo se ")
        error_label=tk.Label(login_w,text="Špatné jméno nebo heslo!",fg="red",font=("Helvetica",12),bg="#f0f0f0")
        error_label.pack(pady=10)

def register ( ):

    Windows_1.Start_register()

login_w = tk.Tk()
login_w.geometry("500x500")
login_w.config(bg="#EAE7B1")
login_w.title("Přihlášení")

new_image = Image.open("../images/db.png")
new_image = new_image.resize((40, 40))
new_image = ImageTk.PhotoImage(new_image)
new_label = tk.Label(login_w, image=new_image, bg="#EAE7B1")
new_label.pack()
new_label.place(relx=1.0, y=0, anchor='ne')

logo_image = Image.open("../images/db.png")
logo_image = logo_image.resize((200, 200))
logo_image = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(login_w, image=logo_image,bg="#EAE7B1")
logo_label.pack(pady=30)

logo_image2 = Image.open("../images/leaf.png")
logo_image2 = logo_image2.resize((40, 40))
logo_image2 = ImageTk.PhotoImage(logo_image2)
logo_label2 = tk.Label(login_w, image=logo_image2,bg="#EAE7B1")
logo_label2.pack()
logo_label2.place(x=0, y=0)

username_frame = tk.Frame(login_w, bg="#EAE7B1")
username_frame.pack(pady=10)
username_label = tk.Label(username_frame, text="jméno:", font=("Helvetica", 10), bg="#EAE7B1")
username_label.pack(side="left", padx=10)
username_text = tk.StringVar()
username_entry = tk.Entry(username_frame, textvariable=username_text, font=("Helvetica", 10), width=20)
username_entry.pack(side="left")


password_frame = tk.Frame(login_w, bg="#EAE7B1")
password_frame.pack(pady=10)
password_label = tk.Label(password_frame, text="Heslo:", font=("Helvetica", 10), bg="#EAE7B1")
password_label.pack(side="left", padx=10)
password_text = tk.StringVar()
password_entry = tk.Entry(password_frame, show="*", textvariable=password_text, font=("Helvetica", 10), width=20)
password_entry.pack(side="left")

button_frame = tk.Frame(login_w, bg="#EAE7B1")
button_frame.pack(pady=30)

login_button = tk.Button(button_frame,
    text="Přihlásit se",
    command=login,
    font=("Helvetica", 10),
    bg="#03C988",
    fg="white",
    relief="raised",
    bd=2,
    padx=10,
    pady=5)
login_button.pack(side="left", padx=20)

register_button = tk.Button(button_frame,
    text="Registrovat se",
    command=register,
    font=("Helvetica", 10),
    bg="#A0D995",
    fg="green",
    relief="raised",
    bd=2,
    padx=10,
    pady=5)
register_button.pack(side="left", padx=20)

random_text=random.choice(["XOR šifrování lze použít pro jednoduché šifrování zpráv, avšak je snadno prolomitelné",
                           "XOR šifrování se používá například v telekomunikacích.",
                           "Fernet šifrování používá významně delší klíče než XOR šifrování, což zvyšuje jeho bezpečnost.",
                           "XOR šifrování je snadné implementovat a vyžaduje pouze několik řádků kódu v Pythonu.",
                           "Metoda XOR se často používá v kryptografii pro ochranu dat a autentizaci.",
                           "Fernet je symetrická šifra, která používá algoritmus AES-128 pro šifrování.",
                           "Pokud je použit dostatečně náhodný klíč, metoda XOR může být velmi bezpečná a odolná.",
                           "Fernet šifrování používá významně delší klíče než XOR šifrování, což zvyšuje jeho bezpečnost.",
                            ])

label_tip=tk.Label(login_w,text="zajímavost:",bg="#FCF9C6",font=("Helvetica",8,"italic"))
label_tip.place(relx=0.5, rely=0.9, anchor="center")
label_random=tk.Label(login_w,text=random_text,bg="#FCF9C6",font=("Helvetica",8,"italic"))
label_random.place(relx=0.5, rely =0.95, anchor="center")

login_w.mainloop()
