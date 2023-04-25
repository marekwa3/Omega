import tkinter as tk
import re
import random
import string
from tkinter import simpledialog,filedialog,messagebox
from Toolbox import Tooltip
import Connection
import Data_handler
import Main_menu
import log

def Start_insert(x):

    log.log_Info("Start_insert","uzivatel: "+str(x)+" insert")
    key = ""

    def exit_to_main_menu():

        W1.destroy()
        Main_menu.start(x)

    def save_text():
        conn=Connection.Connect()
        conn.autocommit=False
        cursor=conn.cursor()

        text3=entry_nazev.get()
        text1=entry_text.get("1.0",tk.END)
        text2=entry_klic.get()

        Data_handler.insert(text2,text1,"1",x,text3)

        query="SELECT MAX(id) FROM secret_data"
        cursor.execute(query)
        result=cursor.fetchone()
        id1=result[0]

        query="SELECT text FROM secret_data WHERE id = %s"
        values=(id1,)
        cursor.execute(query,values)
        result=cursor.fetchone()
        text_encrypted=result[0]
        label.config(text=text_encrypted)

    def save_text_from_user():
        text_to_save=entry_text.get("1.0","end-1c")
        filename=filedialog.asksaveasfilename(
            defaultextension=".txt",filetypes=[("Text Files","*.txt"),("All Files","*.*")]
            )
        if filename:
            with open(filename,"w") as file:
                file.write(text_to_save)
                messagebox.showinfo("Information","Text uložen!")

    def find_and_replace():
        search_term=simpledialog.askstring("najdi a přepiš","Enter hledané slovo:")
        if search_term is not None:
            replace_term=simpledialog.askstring("najdi a přepiš","Enter nahrazovací slovo:")
            if replace_term is not None:
                text=entry_text.get("1.0",tk.END)
                new_text=text.replace(search_term,replace_term)
                entry_text.delete("1.0",tk.END)
                entry_text.insert("1.0",new_text)

    def generate_key():
        global key
        key=''.join(random.choices(string.ascii_uppercase+string.digits,k=16))  # Generování náhodného klíče délky 16 znaků z velkých písmen a číslic
        entry_klic.delete(0,tk.END)
        entry_klic.insert(0,key)
        label.config(text="generovaný klíč: "+key)

    def remove_extra_spaces():
        text=entry_text.get("1.0",tk.END)
        text=" ".join(text.split())  # Odstranění nadbytečných mezer pomocí funkce split a join
        entry_text.delete("1.0",tk.END)
        entry_text.insert(tk.END,text)

    def capitalize_sentences():
        text=entry_text.get("1.0",tk.END)
        sentences=re.split('([.!?]\s)',text)
        capitalized_sentences=[sentence.capitalize() for sentence in sentences]
        new_text=''.join(capitalized_sentences)
        entry_text.delete("1.0",tk.END)
        entry_text.insert("1.0",new_text)

    def add_space_after_dot():
        text=entry_text.get("1.0",tk.END)
        new_text=re.sub(r'(?<=[.!?])\s*',' ',text)
        entry_text.delete("1.0",tk.END)
        entry_text.insert("1.0",new_text)

    def open_file():
        try:
            file_path=filedialog.askopenfilename(defaultextension=".txt")
            if file_path:
                with open(file_path,"r",encoding="utf-8") as file:
                    file_content=file.read()
                    entry_text.delete('1.0','end')
                    entry_text.insert('1.0',file_content)
        except FileNotFoundError:
            messagebox.showerror("Error","File not found!")
        except Exception as e:
            messagebox.showerror("Error",f"An error occurred: {str(e)}")

    def count_words():
        text=entry_text.get("1.0","end-1c")
        word_count=len(text.split())
        label_word_count.config(text=f"Počet slov: {word_count}")

    def create_tooltip(widget,text):
        tooltip=Tooltip(widget,text)
        widget.bind("<Button-3>",lambda event: tooltip.show_tip())
        widget.bind("<Leave>",lambda event: tooltip.hide_tip())

    W1=tk.Tk()
    W1.config(bg="#C1DEAE")
    W1.geometry("900x700")
    W1.title("Insert")



    left_frame=tk.Frame(W1 , bg="#C1DEAE" )
    left_frame.pack(side=tk.LEFT,padx=50)

    right_frame=tk.Frame(W1 , bg="#C1DEAE")
    right_frame.pack(side=tk.RIGHT,padx=50)

    username_label=tk.Label(W1,text="Nazev:",font=("Helvetica",14,),bg="#C1DEAE")
    username_label.pack(pady=3)

    entry_nazev=tk.Entry(W1,font=("Helvetica",12),width=20)
    entry_nazev.pack()

    password_label=tk.Label(W1,text="Klic pro zaheslovani:",font=("Helvetica",14),bg="#C1DEAE")
    password_label.pack(pady=3)

    entry_klic=tk.Entry(W1,font=("Helvetica",12),width=20)
    entry_klic.pack()

    input_frame=tk.Frame(W1)
    input_frame.pack(pady=3)

    entry_text=tk.Text(
    input_frame,font=("Helvetica",14),width=60,height=15,wrap="word",highlightthickness=1)
    entry_text.pack(side=tk.LEFT,padx=10)

    scrollbar=tk.Scrollbar(input_frame,command=entry_text.yview)
    scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
    entry_text.config(yscrollcommand=scrollbar.set)

    find_replace_button=tk.Button(
        right_frame,
        text="Find and Replace",
        font=("Helvetica",10),
        width=12,
        command=find_and_replace,
        fg="black",
        bg="#00C897",
        bd=5,
        relief=tk.FLAT
    )
    create_tooltip(find_replace_button,"najde slovo a přepíše ho")
    find_replace_button.pack()

    generate_key_button=tk.Button(
        left_frame,
        text="Generate Key",
        font=("Helvetica",10),
        width=12,
        command=generate_key,
        fg="white",
        bg="#03C988",
        bd=5,
        relief=tk.FLAT
    )
    create_tooltip(generate_key_button,"nahraje text ze souboru")
    generate_key_button.pack(pady=10)

    addtext_button=tk.Button(
        left_frame,
        text="nahrat text",
        font=("Helvetica",10),
        width=12,
        command=open_file,
        fg="white",
        bg="#03C988",
        bd=5,
        relief=tk.FLAT
    )
    create_tooltip(addtext_button,"vytvoří nahodný klíč pro vaše zaheslovaní")
    addtext_button.pack(pady=10)

    save_button=tk.Button(
        left_frame,
        text="Uložit do souboru",
        font=("Helvetica",10),
        width=12,
        command=save_text_from_user,
        fg="white",
        bg="green",
        bd=5,
        relief=tk.FLAT,
    )
    create_tooltip(save_button,"spočíta a vypíše počet slov")
    save_button.pack(pady=10)

    save_button=tk.Button(
        left_frame,
        text="Vloz do databaze",
        font=("Helvetica",10),
        width=12,
        command=save_text,
        fg="white",
        bg="green",
        bd=5,
        relief=tk.FLAT
    )
    create_tooltip(save_button,"uložení do db")
    save_button.pack(pady=10)

    menu_button=tk.Button(
        left_frame,
        text="Zpet do menu",
        font=("Helvetica",10),
        width=12,
        command=exit_to_main_menu,
        fg="white",
        bg="red",
        bd=5,
        relief=tk.FLAT
    )
    create_tooltip(menu_button,"zpět do hl meny")
    menu_button.pack(pady=10)

    clean_button=tk.Button(
        right_frame,
        text="uklizení mezer",
        font=("Helvetica",10),
        width=12,
        command=remove_extra_spaces,
        fg="black",
        bg="#00C897",
        bd=5,
        relief=tk.FLAT
    )
    clean_button.pack(pady=10)

    shift_button=tk.Button(
        right_frame,
        text="Zvětšit písmen",
        font=("Helvetica",10),
        width=12,
        command=capitalize_sentences,
        fg="black",
        bg="#00C897",
        bd=5,
        relief=tk.FLAT
    )
    create_tooltip(shift_button,"přidá velká písmena slovům na začátku věty")
    shift_button.pack(pady=10)

    add_space_button=tk.Button(
        right_frame,
        text="Přidat mezer",
        font=("Helvetica",10),
        width=12,
        command=add_space_after_dot,
        fg="black",
        bg="#00C897",
        bd=5,
        relief=tk.FLAT
    )
    create_tooltip(add_space_button,"přidá mezeru za konec vět ")
    add_space_button.pack(pady=10)

    word_count_button=tk.Button(
        right_frame,
        text="Počet slov",
        font=("Helvetica",10),
        width=12,
        command=count_words,
        fg="black",
        bg="#00C897",
        bd=5,
        relief=tk.FLAT
    )
    create_tooltip(word_count_button,"spočíta a vypíše počet slov")
    word_count_button.pack(pady=10)

    label=tk.Label(W1,font=("Helvetica",14),fg="black")
    label.pack()

    label_word_count=tk.Label(W1,font=("Helvetica",14),fg="black")
    label_word_count.pack(pady=10)

    W1.mainloop()




