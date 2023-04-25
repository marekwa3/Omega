import tkinter as tk
from tkinter import filedialog , messagebox , ttk
import Connection , Data_handler , Main_menu
import log


def show_text1 (x) :
    def exit_to_main_menu () :
        w2.destroy()
        Main_menu.start(x)
        log.log_Info("exit to main menu" , " uzivatel: " + str(x))

    def find () :
        text2 = entry_id.get()
        text3 = entry_key.get()

        entry_text.delete("1.0" , "end")
        entry_text.insert("1.0" , Data_handler.select_text(text2 , text3 , x))
        entry_text.config(state = "disabled")

    w2 = tk.Tk()
    w2.config(bg = "#EAE7B1")
    w2.geometry("1000x500")

    username_label = tk.Label(w2 , text = "napiše id záznamu ")
    username_label.pack()

    entry_id = tk.Entry(w2 , font = ("Helvetica" , 14) , width = 13)
    entry_id.pack(pady = 10)

    username_label = tk.Label(w2 , text = "napiše klíč k záznamu ")
    username_label.pack()

    entry_key = tk.Entry(w2 , font = ("Helvetica" , 14) , width = 13)
    entry_key.pack(pady = 1)

    button1 = tk.Button(
        w2 ,
        text = "najdi" ,
        font = ("Helvetica" , 10) ,
        width = 15 ,
        command = find ,
        foreground = "white" ,
        bg = "blue"
    )
    button1.pack(pady = 4)

    frame = tk.Frame(w2)
    frame.pack()

    entry_text = tk.Text(frame , font = ("Helvetica" , 14) , width = 40 , height = 10 , highlightthickness = 1)
    entry_text.pack(side = tk.LEFT , pady = 10)

    default_text = "tady se zobrazí váš text :)"
    entry_text.insert("1.0" , default_text)

    scrollbar = tk.Scrollbar(frame , command = entry_text.yview)
    scrollbar.pack(side = tk.RIGHT , fill = tk.Y)

    entry_text.config(yscrollcommand = scrollbar.set)

    button3 = tk.Button(
        w2 ,
        text = "exit" ,
        font = ("Helvetica" , 10) ,
        width = 13 ,
        command = exit_to_main_menu ,
        foreground = "red" ,
        highlightthickness = 5
    )
    button3.pack(pady = 4)

    w2.mainloop()


def show_text2 (x) :
    def exit_to_main_menu () :
        W2.destroy()
        Main_menu.start(x)
        log.log_Info("exit to main menu" , " uzivatel: " + str(x))

    def find () :
        text2 = entry_id.get()

        entry_text.delete("1.0" , "end")
        entry_text.insert("1.0" , Data_handler.select_text2(text2 , x))
        entry_text.config(state = "disabled")

    W2 = tk.Tk()
    W2.config(bg = "#EAE7B1")
    W2.geometry("1000x500")

    username_label = tk.Label(W2 , text = "napiše id záznamu ")
    username_label.pack()

    entry_id = tk.Entry(W2 , font = ("Helvetica" , 14) , width = 13)
    entry_id.pack(pady = 10)

    username_label = tk.Label(W2 , text = "najděte klíč ")
    username_label.pack()

    button1 = tk.Button(
        W2 ,
        text = "najdi" ,
        font = ("Helvetica" , 10) ,
        width = 15 , command = find ,
        foreground = "white" ,
        bg = "blue"
    )
    button1.pack(pady = 4)

    frame = tk.Frame(W2)
    frame.pack()

    entry_text = tk.Text(frame , font = ("Helvetica" , 14) , width = 40 , height = 10 , highlightthickness = 1)
    entry_text.pack(side = tk.LEFT , pady = 10)

    default_text = "tady se zobrazí váš text :)"
    entry_text.insert("1.0" , default_text)

    scrollbar = tk.Scrollbar(frame , command = entry_text.yview)
    scrollbar.pack(side = tk.RIGHT , fill = tk.Y)

    entry_text.config(yscrollcommand = scrollbar.set)

    button3 = tk.Button(
        W2 ,
        text = "exit" ,
        font = ("Helvetica" , 10) ,
        width = 13 ,
        command = exit_to_main_menu ,
        foreground = "red" ,
        highlightthickness = 5
    )
    button3.pack(pady = 4)

    W2.mainloop()


def Start_dictonary (x) :
    def translate_word () :
        conn = Connection.Connect ( )
        c = conn.cursor ( )

        word = entry.get ( ).lower ( )

        # Hledání slova v tabulce dictionary
        c.execute ( "SELECT translation FROM dictionary WHERE word = '" + word + "';" )
        result = c.fetchone ( )

        # Pokud slovo v tabulce dictionary nebylo nalezeno, hledáme v tabulce translations
        if result is None :
            c.execute ( "SELECT word FROM dictionary WHERE translation = '" + word + "';" )
            result = c.fetchone ( )
            if result is not None :
                output.config ( text = result[ 0 ] )
            else :
                output.config ( text = "Slovo bohužel nenalezeno v slovníku :(" )
        else :
            output.config ( text = result[ 0 ] )

        conn.close ( )

    def show_dictionary () :
        conn = Connection.Connect()
        c = conn.cursor()
        c.execute("SELECT * FROM dictionary")
        results = c.fetchall()
        conn.close()

        dictionary_window = tk.Toplevel()
        dictionary_window.title("Slovník")

        tree = ttk.Treeview(dictionary_window , columns = ('word' , 'translation'))
        tree.heading('#0' , text = 'ID')
        tree.heading('word' , text = 'Slovo')
        tree.heading('translation' , text = 'Překlad')

        for row in results :
            tree.insert('' , 'end' , text = row[0] , values = (row[1] , row[2]))

        tree.pack(expand = True , fill = 'both')

    def add_word () :
        word = new_word_entry.get().lower()
        translation = new_translation_entry.get().lower()
        a = Connection.Connect()
        mycursor = a.cursor()

        sql = "INSERT INTO dictionary( word, translation) VALUES (%s, %s);"

        values = (word , translation)

        try :
            mycursor.execute(sql , values)
            a.commit()
            log.log_Info ( "slovnik" , "pridano slovo " + word + "s překladem "+translation )
            status_label.config(text = "Slovo přidáno do slovníku")
        except :
            a.rollback()
            status_label.config(text = "Slovo nepřidáno do slovníku")

        a.close()

        new_word_entry.delete(0 , tk.END)
        new_translation_entry.delete(0 , tk.END)

    def export_dictionary () :
        file_path = filedialog.asksaveasfilename(defaultextension = ".txt" , filetypes = [("Text Files" , "*.txt")])

        if file_path :
            with open(file_path , "w") as f :
                conn = Connection.Connect()
                c = conn.cursor()
                c.execute("SELECT * FROM dictionary")
                results = c.fetchall()
                for row in results :
                    f.write("{},{},{}\n".format(row[0], row[1], row[2]))
                conn.close()

            messagebox.showinfo("Export slovníku" , "Slovník byl úspěšně exportován do souboru.")

    def import_dictionary () :
        file_name = filedialog.askopenfilename(filetypes = [("Text Files" , "*.txt")])
        with open(file_name , "r") as f :
            conn = Connection.Connect()
            c = conn.cursor()

            for line in f :
                parts = line.strip().split(",")
                if len(parts) == 3 and None not in parts :
                    word = parts[1]
                    translation = parts[2]
                    sql = "INSERT INTO dictionary (word, translation) VALUES (%s, %s);"
                    values = (word , translation)
                    try :
                        c.execute(sql , values)
                        conn.commit()
                        status_label.config(text = "Slovo přidáno do slovníku")
                    except :
                        conn.rollback()
                        status_label.config(text = "Slovo nepřidáno do slovníku")


            conn.commit()
            conn.close()

        messagebox.showinfo("Import slovníku" , "Slovník byl úspěšně importován ze sou")

    W2 = tk.Tk()
    W2.config(bg = "#357282")
    W2.geometry("1000x500")
    W2.title("Slovník")

    translate_frame = tk.Frame(W2 , pady = 10 , bg = "")
    translate_frame.pack()

    label = tk.Label(translate_frame , text = "Zadej slovo k překladu:" , font = ("Arial" , 14))
    label.grid(row = 0 , column = 0)

    entry = tk.Entry(translate_frame , width = 30 , font = ("Arial" , 14))
    entry.grid(row = 0 , column = 1)

    button = tk.Button(
        translate_frame ,
        text = "Přeložit" ,
        font = ("Arial" , 14) ,
        command = translate_word
    )
    button.grid(row = 0 , column = 2 , padx = 10)

    output = tk.Label(translate_frame , text = "" , font = ("Arial" , 14))
    output.grid(row = 1 , column = 0 , columnspan = 3)

    add_frame = tk.Frame(W2 , pady = 10)
    add_frame.pack()

    add_label = tk.Label(add_frame , text = "Přidat slovíčko do slovníku:" , font = ("Arial" , 14))
    add_label.grid(row = 0 , column = 0)

    new_word_label = tk.Label(add_frame , text = "Slovo:" , font = ("Arial" , 14))
    new_word_label.grid(row = 1 , column = 0)

    new_word_entry = tk.Entry(add_frame , width = 30 , font = ("Arial" , 14))
    new_word_entry.grid(row = 1 , column = 1)

    new_translation_label = tk.Label(add_frame , text = "Překlad:" , font = ("Arial" , 14))
    new_translation_label.grid(row = 2 , column = 0)

    new_translation_entry = tk.Entry(add_frame , width = 30 , font = ("Arial" , 14))
    new_translation_entry.grid(row = 2 , column = 1)

    add_button = tk.Button(
        add_frame , text = "Přidat slovíčko" ,
        font = ("Arial" , 14) ,
        command = add_word
    )
    add_button.grid(row = 3 , column = 1 , pady = 10)

    status_label = tk.Label(add_frame , text = "" , font = ("Arial" , 14))

    export_frame = tk.Frame(W2 , pady = 10)
    export_frame.pack()

    export_button = tk.Button(
        export_frame ,
        text = "Exportovat slovník" ,
        font = ("Arial" , 14) ,
        command = export_dictionary
        )
    export_button.pack()

    import_button = tk.Button(
        export_frame , text = "Import slovník" , font = ("Arial" , 14) , command = import_dictionary
        )
    import_button.pack()

    show_button = tk.Button(
        export_frame ,
        text = "ukaž slovník" ,
        font = ("Arial" , 14) ,
        command = show_dictionary
    )
    show_button.pack()
    show_button.pack()



def Start_profile_edit (x) :
    print(x)

    def submit () :
        name = name_entry.get()
        password = password_entry.get()
        number = number_entry.get()

        conn = Connection.Connect()
        mycursor = conn.cursor()

        sql = "UPDATE Uzivatel SET jmeno = '" + name + "', heslo = '" + password + "', cislo = '" + number + "' WHERE id = " + str(x) + ";"
        mycursor.execute(sql)
        conn.commit()
        result_label.config(text = f"Záznam byl aktualizován pro ID {x}")

    w = tk.Tk()
    w.title("Upravit profil")
    w.geometry("400x300")
    w.config(bg = "#EAE7B1")

    title_label = tk.Label(
        w , text = "Upravit profil" , font = ("Helvetica" , 20 , "bold") , pady = 10 , bg = "lightblue"
    )
    title_label.pack()

    name_label = tk.Label(w , text = "Jméno:" , font = ("Helvetica" , 12) , bg = "lightblue" , padx = 10 , pady = 5)
    name_label.pack()
    name_entry = tk.Entry(w , font = ("Helvetica" , 12))
    name_entry.pack()

    password_label = tk.Label(
        w , text = "Heslo:" , font = ("Helvetica" , 12) , bg = "lightblue" , padx = 10 , pady = 5
    )
    password_label.pack()

    password_entry = tk.Entry(w , show = "*" , font = ("Helvetica" , 12))
    password_entry.pack()

    number_label = tk.Label(
        w , text = "Číslo:" , font = ("Helvetica" , 12) , bg = "lightblue" , padx = 10 , pady = 5
    )
    number_label.pack()
    number_entry = tk.Entry(w , font = ("Helvetica" , 12))
    number_entry.pack()

    old_label = tk.Label(
        w , text = "Staré heslo:" , font = ("Helvetica" , 12) , bg = "lightblue" , padx = 10 , pady = 5
    )
    old_label.pack()

    old_entry = tk.Entry(w , show = "*" , font = ("Helvetica" , 12))
    old_entry.pack()

    result_label = tk.Label(w , text = "" , font = ("Helvetica" , 12) , fg = "green" , pady = 10 , bg = "lightblue")
    result_label.pack()

    submit_button = tk.Button(
        w ,
        text = "Odeslat" ,
        font = ("Helvetica" , 12)
        , command = submit
    )
    submit_button.pack()

    w.mainloop()
