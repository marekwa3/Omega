import tkinter as tk
from mailbox import mbox
from tkinter import messagebox


import Ecrypter_Windows1,Ecrypter_Windows2
import Windows_2,Windows_3
from Toolbox import Tooltip
import Main_menu
from src import Data_handler,log,List_names


def Start_Edit_menu(x):

    def create_tooltip(widget,text):
        tooltip=Tooltip(widget,text)
        widget.bind("<Button-3>",lambda event: tooltip.show_tip())
        widget.bind("<Leave>",lambda event: tooltip.hide_tip())

    def edit():
        w1.destroy()
        Windows_3.Start_edit(x)

    def edit2():
        w1.destroy()
        Windows_3.Start_edit2(x)

    w1=tk.Tk()
    w1.title("Menu")
    w1.geometry("1000x500")
    w1.configure(background="#FCF9C6")

    button_edit1=tk.Button(
        w1,
        text="Edit Text and Data",
        font=("Helvetica",12,"bold"),
        width=20,
        command=edit,
        bg="#03C988",
        fg="white",
        relief=tk.FLAT
    )
    button_edit1.pack(pady=10)
    create_tooltip(button_edit1,"otevře okno na editaci dat zašifrovaných metodou xor")

    button_edit2=tk.Button(
        w1,
        text="Edit Text and Data",
        font=("Helvetica",12,"bold"),
        width=20,
        command=edit2,
        bg="#03C988",
        fg="white",
        relief=tk.FLAT
    )
    button_edit2.pack(pady=10)
    create_tooltip(button_edit2,"otevře okno na editaci dat zašifrovaných metodou fernet")

    w1.mainloop()
def Start_Encrypt_menu(x):

    def create_tooltip(widget,text):
        tooltip=Tooltip(widget,text)
        widget.bind("<Button-3>",lambda event: tooltip.show_tip())
        widget.bind("<Leave>",lambda event: tooltip.hide_tip())

    def Encrypter1():
        w.destroy()
        Ecrypter_Windows1.Start_insert(x)

    def Encrypter2():
        w.destroy()
        Ecrypter_Windows2.Start_insert(x)

    def exit_to_main_menu () :
        w.destroy()
        Main_menu.start(x)
        log.log_Info("exit" , "exit to main menu .uzivatel: " + x + "")

    w=tk.Tk()
    w.title("Menu")
    w.geometry("500x300")
    w.configure(background="#EAE7B1")

    button_insert=tk.Button(
        w,
        text="Encrypter 1",
        font=("Helvetica",12,"bold"),
        width=20,
        command=Encrypter1,
        bg="#4CAF50",
        fg="white",
        relief=tk.FLAT
    )
    button_insert.pack(pady=10)
    create_tooltip(button_insert,"otevře okno na zašifrovaní metodou xor")

    button_2=tk.Button(
        w,
        text="Encrypter 2",
        font=("Helvetica",12,"bold"),
        width=20,
        command=Encrypter2,
        bg="#4CAF50",
        fg="white",
        relief=tk.FLAT
    )
    button_2.pack(pady=10)
    create_tooltip(button_2,"otevře okno na zašifrovaní metodou fernet")

    button_3=tk.Button(
        w,
        text="exit",
        font=("Helvetica",12,"bold"),
        width=20,
        command=exit_to_main_menu,
        bg="red",
        fg="white",
        relief=tk.FLAT
    )
    create_tooltip(button_3,"vratí na hlavní meny")
    button_3.pack(pady=10)

def Start_Descrypt(x):

    def create_tooltip(widget,text):
        tooltip=Tooltip(widget,text)
        widget.bind("<Button-3>",lambda event: tooltip.show_tip())
        widget.bind("<Leave>",lambda event: tooltip.hide_tip())

    def Descrypt1():
        w.destroy ( )
        Windows_2.show_text1(x)


    def Descrypt2():
        w.destroy ( )
        Windows_2.show_text2(x)

    def exit():
        w.destroy ()


    w=tk.Tk()
    w.title("Menu")
    w.geometry("500x300")
    w.configure(background="#EAE7B1")

    button_1=tk.Button(
        w,
        text="rozkoduj xor",
        font=("Helvetica",12,"bold"),
        width=20,
        command=Descrypt1,
        bg="#4CAF50",
        fg="white",
        relief=tk.FLAT
    )
    create_tooltip(button_1,"rozkódování XOR šifrování s opakovaným klíčem.")
    button_1.pack(pady=10)

    button_2=tk.Button(
        w,
        text="rozkoduj fernet",
        font=("Helvetica",12,"bold"),
        width=20,
        command=Descrypt2,
        bg="#4CAF50",
        fg="white",
        relief=tk.FLAT
    )
    create_tooltip(button_2,"rozkódování Symetrické šifrování Fernet")
    button_2.pack(pady=10)

    button_insert=tk.Button(
        w,
        text="exit",
        font=("Helvetica",12,"bold"),
        width=20,
        command=exit,
        bg="red",
        fg="white",
        relief=tk.FLAT
    )
    create_tooltip(button_2,"ukončí aplikaci")
    button_insert.pack(pady=10)

def Start_delete(x):

    def create_tooltip(widget,text):
        tooltip=Tooltip(widget,text)
        widget.bind("<Button-3>",lambda event: tooltip.show_tip())
        widget.bind("<Leave>",lambda event: tooltip.hide_tip())

    def exit_to_main_menu():
        W2.destroy()
        Main_menu.start(x)
        log.log_Info("exit to main menu"," .uzivatel: "+x+"")

    def delet():
        text1=entry_cislo.get()
        if mbox.askokcancel("Potvrzení smazání",f"Opravdu chcete smazat záznam s ID {text1}?"):
            Data_handler.delete(x,text1)
            mbox.showinfo("Smazání úspěšné","Záznam byl úspěšně smazán.")

    def show():
        List_names.Start(x)

    W2=tk.Tk()
    W2.config(bg="#EAE7B1")
    W2.geometry("1000x500")

    username_label=tk.Label(W2,text="zadejte id záznamu k smazání:")
    username_label.pack()
    entry_cislo=tk.Entry(W2,font=("Helvetica",17),width=20)
    entry_cislo.pack(pady=10)

    button1=tk.Button(
        W2,text="smaž",
        font=("Helvetica",15),
        width=17,
        command=delet,
        foreground="white",
        bg="#03C988")
    button1.pack(pady=4)
    create_tooltip(button1,"tlačitko smaže záznam podle zadaného záznamu")

    button_frame=tk.Frame(W2,bg="#EAE7B1")
    button_frame.pack(pady=30)

    button2=tk.Button(
        button_frame
        ,text="ukaž výpis záznamů",
        font=("Helvetica",15),
        width=20,
        command=show,
        foreground="#00C897")
    button2.pack(side="left", padx=20)
    create_tooltip(button2,"tlačitko ukáže vaše záznamy")

    button_exit=tk.Button(
    button_frame
    ,text="exit",
    font=("Helvetica",15),
    width=20,
    command=exit_to_main_menu,
    foreground="white",
    bg="red",
    )
    button_exit.pack(side="left",padx=20)
    create_tooltip(button_exit,"zpět na hlavní meny")

    W2.mainloop()

def Start_register():
    def exit_():
        W1.destroy()

    def validate_phone_number(phone_number):
        if not phone_number.isdigit():
            return False

        if not (len(phone_number)==9 and all(
                char.isdigit() for char in phone_number[5:]
                )):
            return False

        return True

    def save_register():
        text=entry_heslo.get()
        text1=entry_jmeno.get()
        text2=(text.encode('utf-8'))
        text3=entry_cislo.get()

        if not validate_phone_number(text3):
            messagebox.showerror("Error","špatý formát tel čísla")
            return

        try:
            Data_handler.insert(text1,text2,"2",text3,"0")

            log.log_Info("uzivatel  ",text1+" se zaregistroval")

            W1.destroy()

        except Exception as e:
            messagebox.showerror("Error","Error při ukládaní registračních dat: {}".format(str(e)))

    W1=tk.Tk()
    W1.title("Registration")
    W1.geometry("500x500")
    W1.config(bg="#F7E7CE")

    title_label=tk.Label(W1,text="registrace",font=("Helvetica",20),bg="#F7E7CE",fg="#4B4B4B")
    title_label.pack(pady=20)

    username_label=tk.Label(W1,text="uživatelské jméno:",font=("Helvetica",14),bg="#F7E7CE",fg="#4B4B4B")
    username_label.pack()
    entry_jmeno=tk.Entry(W1,font=("Helvetica",14),width=20)
    entry_jmeno.pack(pady=5)

    password_label=tk.Label(W1,text="heslo:",font=("Helvetica",14),bg="#F7E7CE",fg="#4B4B4B")
    password_label.pack()
    entry_heslo=tk.Entry(W1,show="*",font=("Helvetica",14),width=20)
    entry_heslo.pack(pady=5)

    phone_label=tk.Label(W1,text="tel cislo:",font=("Helvetica",14),bg="#F7E7CE",fg="#4B4B4B")
    phone_label.pack()
    entry_cislo=tk.Entry(W1,font=("Helvetica",14),width=20)
    entry_cislo.pack(pady=5)

    button_frame=tk.Frame(W1,bg="#F7E7CE")
    button_frame.pack(pady=20)
    button=tk.Button(
        button_frame
        ,text="Registrovat",
        font=("Helvetica",14),
        width=15,command=save_register,
        bg="#4B4B4B",
        fg="#F7E7CE",
        highlightthickness=5
    )
    button.pack(side=tk.LEFT,padx=10)

    button2=tk.Button(
        button_frame,
        text="Exit",
        font=("Helvetica",14),
        width=15,command=exit_,
        bg="#4B4B4B",
        fg="#F7E7CE",
        highlightthickness=5
        )
    button2.pack(side=tk.RIGHT,padx=10)

    W1.mainloop()


