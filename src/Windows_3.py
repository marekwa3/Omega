from tkinter import filedialog , messagebox
import tkinter.messagebox as mbox
import Data_handler
import Connection
import Main_menu
import log
import tkinter as tk
import List_names

def Start_export_Enscrypted ( x) :
    def export_data():
        file_path=filedialog.asksaveasfilename(filetypes=[("Text Files","*.txt")],defaultextension=".txt")
        if file_path:
            try:
                conn=Connection.Connect()
                c=conn.cursor()

                id=id_var.get()

                c.execute("SELECT * FROM Secret_data WHERE id=%s",(id,))
                data=c.fetchall()

                with open(file_path,"w") as f:
                    for row in data:
                        f.write(f"{row[2]}: {row[3]}\n")

                messagebox.showinfo("Export data","Data byly exportována.")

            except Exception as e:
                print(e)
                messagebox.showerror("Error","error při exportu.")

            finally:
                if conn.is_connected():
                    conn.close()

    def update_id_label (*args) :
        selected_id = id_var.get ( )
        id_label.config ( text = f"Vybrané ID: {selected_id}" )
    def import_data ( ) :
        file_path = filedialog.askopenfilename ( filetypes = [("Text Files" , "*.txt")] )

        if file_path :
            try :

                conn = Connection.Connect ()
                cursor = conn.cursor ( )

                with open ( file_path , "r" ) as f :
                    for line in f :

                        name , data = line.strip ( ).split ( ": " )

                        sql = "INSERT INTO Secret_Data (`f_uzivatel`, `nazev` , `text`) VALUES (%s,%s,%s);"
                        values = ( x, name , data)
                        cursor.execute ( sql , values )
                        conn.commit ( )

                cursor.close ( )
                conn.close ( )

                tk.messagebox.showinfo ( "Import data" , "Data byla úspěšně importována do databáze." )

            except Exception as e :
                print ( e )
                tk.messagebox.showerror ( "Chyba" , "Při importu dat došlo k chybě." )

    w = tk.Tk ( )
    w.geometry ( "400x250" )
    w.title ( "Export Enscrypted Data" )
    w.config(bg="#EEE6CE")

    bg_color = "#EEE6CE"
    font = ("Helvetica" , 12)
    label_color = "#333333"
    button_color = "#03C988"
    button_hover_color = "#106ebe"
    button_font_color = "#ffffff"

    id_var = tk.StringVar ( )
    id_var.trace_add ( "write" , update_id_label )
    id_choices = []
    conn = Connection.Connect ( )
    c = conn.cursor ( )
    c.execute ( "SELECT id FROM Secret_data" )
    ids = c.fetchall ( )
    for i in ids :
        id_choices.append ( i [0] )
    id_label = tk.Label ( w , text = "Vyberte ID záznamu:" , font = font , fg = label_color , bg = bg_color )
    id_label.pack ( pady = 10 )

    id_dropdown = tk.OptionMenu ( w , id_var , *id_choices )
    id_dropdown.config ( font = font )
    id_dropdown.pack ( pady = 10 )

    button_frame = tk.Frame ( w , bg = bg_color )
    button_frame.pack ()

    button_export = tk.Button (
        button_frame ,
        text = "Exportovat data" ,
        font = font ,
        bg = button_color ,
        fg = button_font_color ,
        activebackground = button_hover_color ,
        command = export_data)
    button_export.pack ( side = tk.LEFT , padx = 10 , pady = 10 )

    button_import = tk.Button (
        button_frame ,
        text = "Importovat data" ,
        font = font ,
        bg = button_color ,
        fg = button_font_color ,
        activebackground = button_hover_color ,
        command = import_data)
    button_import.pack ( side = tk.LEFT , padx = 10 , pady = 10 )

    w.mainloop ( )


def Start_edit(x):
    def exit_to_main_menu():
        w2.destroy()
        Main_menu.start(x)
        log.log_Info("exit to main menu"," .uzivatel: "+x+"")

    def save():
        print()
        text1=entry_text.get("1.0",tk.END)
        text2=entry_id.get()
        key=entry_key.get()
        Data_handler.start_update(text1,text2,key,x)

    def find():
        text2=entry_id.get()
        text3=entry_key.get()

        entry_text.delete("1.0","end")
        entry_text.insert("1.0",Data_handler.select_text(text2,text3,x))

    def save_copy():
        conn=Connection.Connect()
        conn.autocommit=False


        cursor=conn.cursor()
        query="SELECT nazev FROM secret_data where id ="+entry_id.get()+"kopie"+";"
        cursor.execute(query)
        result=cursor.fetchone()
        nazev=result[0]
        print(nazev)

        text3=nazev
        text1=entry_text.get("1.0",tk.END)
        text2=entry_key.get()

        Data_handler.insert(text2,text1,"1",x,text3)

        messagebox.showinfo("kopie uložena","kopie se úspěšně uložila.")



    w2=tk.Tk()
    w2.config(bg="#C1DEAE")
    w2.geometry("1000x500")

    username_label=tk.Label(w2,text="napiše id záznamu ")
    username_label.pack()

    entry_id=tk.Entry(w2,font=("Helvetica",14),width=13)
    entry_id.pack(pady=10)

    username_label=tk.Label(w2,text="napiše klíč k záznamu ")
    username_label.pack()

    entry_key=tk.Entry(w2,font=("Helvetica",14),width=13)
    entry_key.pack(pady=1)

    button1=tk.Button(
        w2,
        text="najdi",
        font=("Helvetica",10),
        width=15,
        command=find,
        foreground="white",
        bg="#03C988"
    )
    button1.pack(pady=4)

    frame=tk.Frame(w2)
    frame.pack()

    entry_text=tk.Text(frame,font=("Helvetica",14),width=40,height=10,highlightthickness=1)
    entry_text.pack(side=tk.LEFT,pady=10)

    default_text="tady se zobrazí váš text :)"
    entry_text.insert("1.0",default_text)

    scrollbar=tk.Scrollbar(frame,command=entry_text.yview)
    scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

    entry_text.config(yscrollcommand=scrollbar.set)

    button_save=tk.Button(
    w2,
        text="ulož",
        font=("Helvetica",10),
        width=13,
        command=save,
        foreground="white",
        bg="#03C988",
        highlightthickness=5)
    button_save.pack(pady=4)

    button_save_copy=tk.Button(
        w2,
        text="ulož kopii",
        font=("Helvetica",10),
        width=13,
        command=save_copy,
        foreground="white",
        bg="#03C988",
        highlightthickness=5
    )
    button_save_copy.pack(pady=4)

    button3=tk.Button(
    w2,
        text="exit",
        font=("Helvetica",10),
        width=13,
        command=exit_to_main_menu,
        foreground="white",
        bg="#F44336",
    highlightthickness=5)

    button3.pack(pady=4)

    w2.mainloop()

def Start_edit2(x):

    def save_copy():
        conn=Connection.Connect()
        conn.autocommit=False


        cursor=conn.cursor()
        query="SELECT nazev FROM secret_data where id ="+entry_id.get()+"kopie"+";"
        cursor.execute(query)
        result=cursor.fetchone()
        nazev=result[0]
        print(nazev)

        text3=nazev
        text1=entry_text.get("1.0",tk.END)
        text2="/"

        Data_handler.insert(text2,text1,"1",x,text3)

        messagebox.showinfo("kopie uložena","kopie se úspěšně uložila.")

    def exit_to_main_menu():
        w2.destroy()
        Main_menu.start(x)
        log.log_Info("exit","exit to main menu .uzivatel: "+x+"")

    def save():
        text1=entry_text.get("1.0",tk.END)
        text2=entry_id.get()

        Data_handler.start_update2(text1,text2,x)

    def find():
        text2=entry_id.get()


        entry_text.delete("1.0","end")
        entry_text.insert("1.0",Data_handler.select_text2(text2,x))

    w2=tk.Tk()
    w2.config(bg="#EEE6CE")
    w2.geometry("1000x500")

    username_label=tk.Label(w2,text="napiše id záznamu ")
    username_label.pack()

    entry_id=tk.Entry(w2,font=("Helvetica",14),width=13)
    entry_id.pack(pady=10)

    username_label=tk.Label(w2,text="napiše klíč k záznamu ")
    username_label.pack()

    button1=tk.Button(
        w2,
        text="najdi",
        font=("Helvetica",10),
        width=15,
        command=find,
        foreground="white",
        bg="#03C988"
    )
    button1.pack(pady=4)

    frame=tk.Frame(w2)
    frame.pack()

    entry_text=tk.Text(frame,font=("Helvetica",14),width=40,height=10,highlightthickness=1)
    entry_text.pack(side=tk.LEFT,pady=10)

    default_text="tady se zobrazí váš text :)"
    entry_text.insert("1.0",default_text)

    scrollbar=tk.Scrollbar(frame,command=entry_text.yview)
    scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

    entry_text.config(yscrollcommand=scrollbar.set)

    button_save=tk.Button(
        w2,
        text="ulož",
        font=("Helvetica",10),
        width=13,
        command=save,
        foreground="white",
        bg="#03C988",
        highlightthickness=5
    )
    button_save.pack(pady=4)

    button_save_copy=tk.Button(
        w2,
        text="ulož kopii",
        font=("Helvetica",10),
        width=13,
        command=save_copy,
        foreground="white",
        bg="#03C988",
        highlightthickness=5
    )
    button_save_copy.pack(pady=4)

    button3=tk.Button(
        w2,
        text="exit",
        font=("Helvetica",10),
        width=13,
        command=exit_to_main_menu,
        foreground="white",
        bg="#F44336",
        highlightthickness=5
    )
    button3.pack(pady=4)

    w2.mainloop()




