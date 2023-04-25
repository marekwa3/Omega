import tkinter as tk
import Connection
from tkinter import ttk

def Start(x):

    def refresh_data():
        tree.delete(*tree.get_children())
        conn = Connection.Connect()
        c = conn.cursor()
        c.execute("SELECT id, nazev FROM secret_data WHERE f_uzivatel = "+x+";")
        data = c.fetchall()
        for row in data:
            tree.insert("", tk.END, values=row)
        conn.close()

    def search_data():
        query=search_entry.get().strip()

        if not query:
            return
        conn=Connection.Connect()
        c=conn.cursor()
        c.execute(f"SELECT id, nazev FROM secret_data WHERE f_uzivatel = {x} AND nazev LIKE '%{query}%'")
        data=c.fetchall()
        tree.delete(*tree.get_children())
        for row in data:
            tree.insert("",tk.END,values=row)
        conn.close()

    def get_all_data():
        tree.delete(*tree.get_children())
        conn=Connection.Connect()
        c=conn.cursor()
        c.execute("SELECT id, nazev FROM secret_data WHERE f_uzivatel = "+x+";")
        data=c.fetchall()
        for row in data:
            tree.insert("",tk.END,values=row)
        conn.close()


    x = str(x)

    roo = tk.Tk()
    roo.title("Secret Data")
    roo.geometry("400x400")
    roo.configure(bg="#ffffe0")

    search_frame=tk.Frame(roo,bg="#ffffe0")
    search_frame.pack(padx=20,pady=(10,0),fill="x")

    search_label=tk.Label(search_frame,text="Hledat:",font=("Arial",12),bg="#ffffe0")
    search_label.pack(side="left",padx=5)

    search_entry=tk.Entry(search_frame,width=20)
    search_entry.pack(side="left",padx=5)

    search_button=tk.Button(
        search_frame,
        text="Hledat",
        command=search_data)
    search_button.pack(side="left",padx=5)

    search_button=tk.Button(
        search_frame,
        text="vsechny data",
        command=get_all_data
    )
    search_button.pack(side="left",padx=5)

    username_label = tk.Label(roo, text="Vaše záznamy:", font=("Arial", 14), bg="#ffffe0")
    username_label.pack(pady=10)

    tree_frame = tk.Frame(roo)
    tree_frame.pack(padx=20, pady=10, fill="both", expand=True)

    tree = ttk.Treeview(tree_frame, columns=("ID", "Název"), show="headings")
    tree.column("ID", width=30, anchor="center", stretch=False)
    tree.heading("ID", text="ID", anchor="center")
    tree.column("Název", width=100, anchor="w", stretch=True)
    tree.heading("Název", text="Název", anchor="w")
    tree.pack(side="left", fill="both", expand=True)
    tree.configure(style="Custom.Treeview")

    style = ttk.Style()
    style.configure("Custom.Treeview.Heading", padding=(10, 5))
    style.configure("Custom.Treeview", padding=(10, 5))

    y_scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    y_scrollbar.pack(side="right", fill="y")

    tree.configure(yscrollcommand=y_scrollbar.set)

    conn = Connection.Connect()
    c = conn.cursor()
    c.execute("SELECT id, nazev FROM secret_data WHERE f_uzivatel = "+x+";")
    data = c.fetchall()

    for row in data:
        tree.insert("", tk.END, values=row)

    conn.close()

    refresh_button = tk.Button(roo, text="Refresh", command=refresh_data)
    refresh_button.pack(pady=5)

    close_button = tk.Button(roo, text="Zavřít", command=roo.destroy)
    close_button.pack(pady=5)

    roo.mainloop()
