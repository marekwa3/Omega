import tkinter as tk
import Windows_2
import Windows_4
import xml_handler
from src.Toolbox import Tooltip


def Start(x):

    def create_tooltip(widget,text):
        tooltip=Tooltip(widget,text)
        widget.bind("<Button-3>",lambda event: tooltip.show_tip())
        widget.bind("<Leave>",lambda event: tooltip.hide_tip())
    def xml():
        w.destroy()
        xml_handler.xml_to_file(x)
    def del_User():
        w.destroy()
        Windows_4.Start_delete_User(x)

    def edit_User():
        w.destroy()
        Windows_2.Start_profile_edit(x)

    def back():
        w.destroy()

    w = tk.Tk()
    w.title("Menu")
    w.geometry("400x200")
    w.configure(background="#EAE7B1")

    w.columnconfigure(0, weight=1)
    w.columnconfigure(1, weight=1)

    left_column = tk.Frame(w, bg="#FCF9C6")
    left_column.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    left_middle_column = tk.Frame(w, bg="#FCF9C6")
    left_middle_column.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    right_middle_column = tk.Frame(w, bg="#FCF9C6")
    right_middle_column.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    right_column = tk.Frame(w, bg="#FCF9C6")
    right_column.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    button_del_user = tk.Button(
        right_column,
        text="zpět",
        font=("Helvetica", 12, "bold"),
        width=20,
        command=back,
        bg="#FFC107",
        fg="white",
        relief="groove"
    )
    button_del_user.pack(pady=10)

    button_edit_user = tk.Button(
        left_middle_column,
        text="edit user data",
        font=("Helvetica", 12, "bold"),
        width=20,
        command=edit_User,
        bg="#F44336",
        fg="white",
        relief="groove"
    )
    create_tooltip(button_edit_user,"umožní uživteli přepsat svoje osobní údaje")
    button_edit_user.pack(pady=10)

    button_xml=tk.Button(
        left_column,
        text="xml export import",
        font=("Helvetica",12,"bold"),
        width=20,
        command=xml,
        bg="#F44336",
        fg="white",
        relief="groove"
    )
    create_tooltip(button_xml,"umožní uživteli uložit profil do xml")
    button_xml.pack(pady=10)

    button_del_user_data = tk.Button(
        right_middle_column,
        text="Delete User and Data",
        font=("Helvetica", 12, "bold"),
        width=20,
        command=del_User,
        bg="#F44336",
        fg="white",
        relief="groove"
    )
    create_tooltip(button_xml , "umožní uživteli smazat sebe a data")
    button_del_user_data.pack(pady=10)

