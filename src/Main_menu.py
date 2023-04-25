import tkinter as tk
import List_names
import Windows_1,Windows_2,Windows_3,Windows_4
import Edit_Profile_menu
from Toolbox import Tooltip

def start(x):

    def create_tooltip(widget,text):
        tooltip=Tooltip(widget,text)
        widget.bind("<Button-3>",lambda event: tooltip.show_tip())
        widget.bind("<Leave>",lambda event: tooltip.hide_tip())

    def insert():
        root.destroy()
        Windows_1.Start_Encrypt_menu(x)

    def edit_menu():
        root.destroy()
        Windows_1.Start_Edit_menu(x)

    def descrypt():
        root.destroy()
        Windows_1.Start_Descrypt(x)

    def delete():
        root.destroy()
        Windows_4.Start_delete(x)

    def delete_all():
        root.destroy()
        Windows_4.Start_delete_all(x)

    def list():
        List_names.Start(x)
    def editor_window():

        Windows_4.editor()

    def dictonary():
        Windows_2.Start_dictonary(x)

    def show_profile_menu():
        Edit_Profile_menu.Start(x)

    def export_data():
        Windows_3.Start_export_Enscrypted(x)

    def exit():
        root.destroy ()

    root = tk.Tk ( )
    root.title ( "Menu" )
    root.geometry ( "1000x500" )
    root.configure ( background = "#FCF9C6" )

    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    root.columnconfigure(2,weight=1)
    root.columnconfigure(3,weight=1)
    root.rowconfigure(0,weight=1)

    left_column=tk.Frame(root,bg="#EAE7B1")
    left_column.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)

    left_middle_column=tk.Frame(root,bg="#EAE7B1")
    left_middle_column.grid(row=0,column=1,sticky="nsew",padx=10,pady=10)

    right_middle_column=tk.Frame(root,bg="#EAE7B1")
    right_middle_column.grid(row=0,column=2,sticky="nsew",padx=10,pady=10)

    right_column=tk.Frame(root,bg="#EAE7B1")
    right_column.grid(row=0,column=3,sticky="nsew",padx=10,pady=10)

    button_insert = tk.Button (
        left_column ,
        text = "zakódování menu" ,
        font = ("Helvetica" , 12 , "bold") ,
        width = 20 ,
        command = insert ,
        bg = "#03C988" ,
        fg = "white" ,
        relief=tk.FLAT
    )
    create_tooltip(button_insert,"otevře meny na výběr typu šifrovaní a poté umožní šifrovat")
    button_insert.pack (pady=10, padx=10, fill="x")

    button_menu_decode = tk.Button (
        left_column ,
        text = "data dekódovač menu" ,
        font = ("Helvetica" , 12 , "bold") ,
        width = 20 ,
        command = descrypt,
        bg = "#03C988" ,
        fg = "white" ,
        relief=tk.FLAT
    )
    create_tooltip(button_menu_decode,"otevře meny na výběr typu dešifrovaní a poté umožní dešifrovat")
    button_menu_decode.pack (pady=10, padx=10, fill="x")

    button_show=tk.Button(
        left_column,
        text="editace dat meny",
        font=("Helvetica",12,"bold"),
        width=20,
        command=edit_menu,
        bg="#03C988",
        fg="white",
        relief=tk.FLAT
    )
    create_tooltip(button_show,"otevře meny na editace")
    button_show.pack(pady=10, padx=10, fill="x")

    button_export = tk.Button (
        left_column ,
        text = "export dat" ,
        font = ("Helvetica" , 12 , "bold") ,
        width = 20 ,
        command = export_data ,
        bg = "#03C988" ,
        fg = "white" ,
        relief=tk.FLAT
    )
    create_tooltip(button_export,"otevře okno na export dat")
    button_export.pack (pady=10, padx=10, fill="x")

    button_delete = tk.Button (
        left_middle_column ,
        text = "mazáni podle id" ,
        font = ("Helvetica" , 12 , "bold") ,
        width = 20 ,
        command = delete ,
        bg = "#A0D995" ,
        fg = "green" ,
        relief=tk.FLAT
    )
    create_tooltip(button_delete,"otevře okno na mazání záznamů")
    button_delete.pack (pady=10, padx=10, fill="x")

    button_delete_all=tk.Button(
        left_middle_column,
        text="smaž všechny data",
        font=("Helvetica",12,"bold"),
        width=20,
        command=delete_all,
        bg="#A0D995",
        fg="green",
        relief=tk.FLAT
    )
    create_tooltip(button_delete_all,"otevře okno na mazání všech záznamů")
    button_delete_all.pack(pady=10, padx=10, fill="x")

    button_delete_all=tk.Button(
        left_middle_column,
        text="textový editor",
        font=("Helvetica",12,"bold"),
        width=20,
        command=editor_window,
        bg="#A0D995",
        fg="green",
        relief=tk.FLAT
    )
    create_tooltip(button_delete_all,"otevře okno na mazání všech záznamů")
    button_delete_all.pack(pady=10, padx=10, fill="x")

    button_file_save = tk.Button (
        right_middle_column ,
        text = "Slovník" ,
        font = ("Helvetica" , 12 , "bold") ,
        width = 20 ,
        command = dictonary ,
        bg = "#607D8B" ,
        fg = "white" ,
        relief=tk.FLAT
    )
    create_tooltip(button_file_save,"otevře jednoduchý slovnník")
    button_file_save.pack (pady=10, padx=10, fill="x")

    button_show_info = tk.Button (
        right_middle_column ,
        text = "přehled záznamů" ,
        font = ("Helvetica" , 12 , "bold") ,
        width = 20 ,
        command = list ,
        bg = "#607D8B" ,
        fg = "white" ,
        relief=tk.FLAT
    )
    create_tooltip(button_show_info,"otevře okno které ukazuje vaše záznamy")
    button_show_info.pack (pady=10,
                           padx=10,
                           fill="x")


    button_exit = tk.Button (
        right_column ,
        text = "editace profilu menu" ,
        font = ("Helvetica" , 12 , "bold") ,
        width = 20 ,
        command = show_profile_menu ,
        bg = "#F44336" ,
        fg = "white" ,
        relief=tk.FLAT
    )
    create_tooltip(button_exit,"otevre meny na editaci profilu ")
    button_exit.pack (pady=10,
                      padx=10,
                      fill="x")

    button_exit = tk.Button (
        right_column ,
        text = "exit" ,
        font = ("Helvetica" , 12 , "bold") ,
        width = 20 ,
        command = exit ,
        bg = "#F44336" ,
        fg = "white" ,
        relief=tk.FLAT
    )
    button_exit.pack (pady=10,
                      padx=10,
                      fill="x")

    create_tooltip(button_exit,"exit")

    root.mainloop ( )
