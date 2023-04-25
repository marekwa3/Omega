import tkinter as tk
import xml.etree.ElementTree as ET
from Toolbox import Tooltip
import mysql
import Connection
from tkinter import filedialog,messagebox


def xml_to_file(x):
    def create_tooltip(widget,text):
        tooltip=Tooltip(widget,text)
        widget.bind("<Button-3>",lambda event: tooltip.show_tip())
        widget.bind("<Leave>",lambda event: tooltip.hide_tip())

    def create_xml():
        a=Connection.Connect()
        c=a.cursor()
        c.execute("SELECT * FROM Uzivatel WHERE id = "+str(x)+"")
        rows=c.fetchall()

        preview=""
        for row in rows:
            preview+=f"id: {row[0]}, jmeno: {row[1]}, heslo: {row[2]}, cislo: {row[3]}\n"

        if messagebox.askyesno("Data Preview",preview+"\n\nDo you want to write these data to an XML file?"):
            root=ET.Element("Uzivatele")
            for row in rows:
                uzivatel=ET.SubElement(root,"Uzivatel")
                id=ET.SubElement(uzivatel,"id")
                id.text=str(row[0])
                jmeno=ET.SubElement(uzivatel,"jmeno")
                jmeno.text=row[1]
                heslo=ET.SubElement(uzivatel,"heslo")
                heslo.text=row[2]
                cislo=ET.SubElement(uzivatel,"cislo")
                cislo.text=str(row[3])

            tree=ET.ElementTree(root)
            tree.write("Uzivatele.xml")

            label.config(text="Data byla úspěšně zapsána do souboru Uzivatele.xml")

    def insert_xml():
        a=Connection.Connect()
        c=a.cursor()

        file_path=filedialog.askopenfilename(defaultextension=".xml",filetypes=[("XML Files","*.xml")])
        if file_path:
            tree=ET.parse(file_path)
            root=tree.getroot()

            preview=""
            for uzivatel in root.findall('Uzivatel'):
                id=int(uzivatel.find('id').text)
                jmeno=uzivatel.find('jmeno').text
                heslo=uzivatel.find('heslo').text
                cislo=int(uzivatel.find('cislo').text)
                preview+=f"id: {id}, jmeno: {jmeno}, heslo: {heslo}, cislo: {cislo}\n"

            if messagebox.askyesno("Data Preview",preview+"\n\nDo you want to insert these data into the database?"):
                for uzivatel in root.findall('Uzivatel'):
                    id=int(uzivatel.find('id').text)
                    jmeno=uzivatel.find('jmeno').text
                    heslo=uzivatel.find('heslo').text
                    cislo=int(uzivatel.find('cislo').text)
                    while True:
                        try:
                            c.execute(
                                "INSERT INTO Uzivatel (id,jmeno,heslo,cislo) VALUES (%s, %s, %s, %s)",
                                (id,jmeno,heslo,cislo)
                                )
                            a.commit()
                            break
                        except mysql.connector.IntegrityError:
                            id+=1

                label.config(text="Data byla úspěšně vložena do databáze")

    root=tk.Tk()
    root.title("Menu")
    root.geometry("1000x500")
    root.configure(background="#FCF9C6")

    root.columnconfigure(0,weight=1)  # make the first column resizable

    root.rowconfigure(0,weight=1)  # make the first row resizable

    column=tk.Frame(root,bg="#EAE7B1")
    column.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)


    button_create=tk.Button(
        column,text="Vytvořit XML soubor",
        command=create_xml,
        font=("Helvetica",12,"bold"),
        width=20,
        bg="#03C988",
        fg="white",
        relief=tk.FLAT
        )
    create_tooltip(button_create,"Vytvoří XML soubor z dat v databázi")
    button_create.pack(pady=10,padx=10,fill="x")

    button_insert=tk.Button(
        column,text="Vložit data z XML do databáze",
        command=insert_xml,
        font=("Helvetica",12,"bold"),
        width=20,
        bg="#03C988",
        fg="white",
        relief=tk.FLAT
        )
    create_tooltip(button_insert,"Vloží data z XML souboru do databáze")
    button_insert.pack(pady=10,padx=10,fill="x")

    label=tk.Label(column,text="",bg="#EAE7B1")
    label.pack()

    root.mainloop()

