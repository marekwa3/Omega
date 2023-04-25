import tkinter.messagebox as mbox
import re,Data_handler
from tkinter import messagebox
import Connection
import Main_menu
import log
import tkinter as tk
import List_names
from src.Toolbox import Tooltip

def Start_delete(x):
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

    W2.mainloop()
def Start_delete_all(x):
    def exit_to_main_menu():
        W2.destroy()
        Main_menu.start(x)
        log.log_Info("exit to main menu"," .uzivatel: "+x+"")

    def delet():
        conn=Connection.Connect()
        conn.autocommit=False

        cursor=conn.cursor()
        query="SELECT heslo FROM Uzivatel where id ="+str(x)+";"
        cursor.execute(query)
        result=cursor.fetchone()
        heslo_db=result[0]
        password=entry_heslo.get()
        print(type(password),password,type(heslo_db),heslo_db)

        if heslo_db==password:
            if mbox.askokcancel("Potvrzení smazání",f"Opravdu chcete smazat záznam s ID ?"):
                a=Connection.Connect()
                mycursor=a.cursor()
                sql="DELETE FROM `secret_data` where f_uzivatel = "+str(x)+""
                mycursor.execute(sql)
                a.commit()
                mbox.showinfo("Smazání úspěšné","Záznamy byl úspěšně smazán.")

        else:
            print ("nepovedlo")


    def show():
        List_names.Start(x)

    W2=tk.Tk()
    W2.config(bg="#EAE7B1")
    W2.geometry("1000x500")

    label_l=tk.Label(W2,text="zadejte heslo pro smazaní vašich dat:")
    label_l.pack()
    entry_heslo=tk.Entry(W2,font=("Helvetica",17),width=20)
    entry_heslo.pack(pady=10)

    button1=tk.Button(
    W2,text="smaž",
    font=("Helvetica",15),
    width=17,
    command=delet,
    foreground="white",
    bg="#03C988")
    button1.pack(pady=4)

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

    W2.mainloop()

def editor():
    import tkinter as tk
    from tkinter import filedialog

    def create_tooltip(widget,text):
        tooltip=Tooltip(widget,text)
        widget.bind("<Button-3>",lambda event: tooltip.show_tip())
        widget.bind("<Leave>",lambda event: tooltip.hide_tip())


    def remove_extra_spaces():
        text= input_text.get("1.0",tk.END)
        text=" ".join(text.split())
        input_text.delete("1.0",tk.END)
        input_text.insert(tk.END,text)

    def capitalize_sentences():
        text= input_text.get("1.0",tk.END)
        sentences=re.split('([.!?]\s)',text)
        capitalized_sentences=[sentence.capitalize() for sentence in sentences]
        new_text=''.join(capitalized_sentences)
        input_text.delete("1.0",tk.END)
        input_text.insert("1.0",new_text)

    def add_space_after_dot():
        text= input_text.get("1.0",tk.END)
        new_text=re.sub(r'(?<=[.!?])\s*',' ',text)
        input_text.delete("1.0",tk.END)
        input_text.insert("1.0",new_text)

    def count_words():
        text = input_text.get('1.0','end-1c')
        words = text.split()
        count = len(words)
        result_label.config(text=f"Počet slov: {count}")

    def save_file():
        text_to_save=input_text.get('1.0','end-1c')
        file_path=filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            try:
                with open(file_path,"w",encoding="utf-8") as file:
                    file.write(text_to_save)
            except Exception as e:
                tk.messagebox.showerror(title="Error",message="objevil se error při ukládaní:\n\n"+str(e))
                return
            tk.messagebox.showinfo(title="Success",message="soubor uložen úspěšně!")

    def open_file():
        try:
            file_path=filedialog.askopenfilename(defaultextension=".txt")
            if file_path:
                with open(file_path,"r",encoding="utf-8") as file:
                    file_content=file.read()
                    input_text.delete('1.0','end')
                    input_text.insert('1.0',file_content)
        except FileNotFoundError:
            messagebox.showerror("Error","soubor nenalezen!")
        except Exception as e:
            messagebox.showerror("Error",f"objevil se error: {str(e)}")

    root=tk.Tk()
    root.title("Textoví editor ")
    root.configure(bg='#FCF9C6')

    window_width=root.winfo_screenwidth()*0.8
    window_height=root.winfo_screenwidth()*0.8*16/9
    root.geometry(f"{int(window_width)}x{int(window_height)}")

    container=tk.Frame(root,bg='#FCF9C6')
    container.pack(side="top",fill="x",padx=10,pady=10)

    button_insert=tk.Button(
        container,
        text="odstraň zb mezery",
        width=20,
        command=remove_extra_spaces,
        highlightthickness=5,
        relief=tk.RIDGE
    )
    create_tooltip(button_insert,"otevře meny na výběr typu šifrovaní a poté umožní šifrovat")
    button_insert.pack(side="left",padx=10,pady=10)

    button_insert=tk.Button(
        container,
        text="velká první písmena",
        width=20,
        command=capitalize_sentences,
        highlightthickness=5,
        relief=tk.GROOVE
    )
    create_tooltip(button_insert,"otevře meny na výběr typu šifrovaní a poté umožní šifrovat")
    button_insert.pack(side="left",padx=10,pady=10)

    button_insert=tk.Button(
        container,
        width=20,
        text="přidej tečky za věty",
        command=add_space_after_dot,
        highlightthickness=5,
        relief=tk.RIDGE
    )
    create_tooltip(button_insert,"otevře meny na výběr typu šifrovaní a poté umožní šifrovat")
    button_insert.pack(side="left",padx=10,pady=10)

    open_button=tk.Button(
        container,
        width=20,
        text="Otevřít soubor",
        command=open_file,
        highlightthickness=5,
        relief=tk.GROOVE
    )
    open_button.pack(side="left",padx=10,pady=10)

    count_button=tk.Button(
        container,
        width=20,
        text="Spočítat slova",
        command=count_words,
        highlightthickness=5,
        relief=tk.RIDGE
    )
    count_button.pack(side="left",padx=10,pady=10)

    save_button=tk.Button(
        container,
        width=20,
        text="Uložit do souboru",
        command=save_file,
        highlightthickness=5,
        relief=tk.GROOVE
    )
    save_button.pack(side="left",padx=10,pady=10)

    result_label=tk.Label(container)
    result_label.pack(padx=10,pady=10,anchor="ne")

    input_container=tk.Frame(root,padx=10,pady=10)
    input_container.pack(fill="both",expand=True,pady=50)

    input_text=tk.Text(
        input_container,height=int(window_height/25),width=int(window_width/40),bg='white'
        )
    input_text.pack(side="top",fill="both",padx=10,pady=10,expand=True)

    root.mainloop()

def Start_delete_User (x) :
    def delet_me () :
        text1 = entry_heslo.get()
        Data_handler.delete_user(x , text1)

    W2 = tk.Tk()
    W2.config(bg = "lightblue")
    W2.geometry("1000x500")

    username_label = tk.Label(W2 , text = "zadejte své heslo pro smazáni")
    username_label.pack()

    entry_heslo = tk.Entry(W2 , font = ("Helvetica" , 14) , width = 13)
    entry_heslo.pack(pady = 10)

    button1 = tk.Button(
        W2 , text = "smaž" , font = ("Helvetica" , 10) , width = 15 , command = delet_me , foreground = "white" ,
        bg = "blue"
    )
    button1.pack(pady = 4)

    W2.mainloop()