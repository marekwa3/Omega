import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
import log
from tkinter import messagebox

def Encrypt(text):
    if len ( text.strip ( ) ) == 0 :
        messagebox.showerror ( "Error" , "text je prázdný" )
        return
    try:
        key = Fernet.generate_key()  # Vygenerování náhodného klíče pro šifrování
        f = Fernet(key)  # Inicializace instance třídy Fernet s vygenerovaným klíčem
        encrypted_message = f.encrypt(text.encode())  # Zašifrování zadaného textu pomocí třídy Fernet
        encrypted_message_str = encrypted_message.decode()  # Převedení zašifrovaného textu na řetězec
        root = tk.Tk()  # Vytvoření instance hlavního okna pro dialogové okno souboru
        root.withdraw()  # Skrytí hlavního okna aplikace
        file_path = filedialog.asksaveasfilename(defaultextension='.key', filetypes=[('Key files', '*.key')])  # Dialogové okno pro výběr umístění souboru s klíčem
        if file_path:
            with open(file_path, 'wb') as file:  # Otevření souboru s klíčem pro zápis bytů
                file.write(key)  # Zápis klíče do souboru
        return encrypted_message_str  # Vrácení zašifrovaného textu v řetězcové podobě
    except Exception as e:  # Výjimka pro případ chyby
        log.log_Error ( 'Enc' , 'chyba šifrovaní ' )
        return None

def Decrypt(encrypted_text):
    try:
        root = tk.Tk()  # Vytvoření instance hlavního okna pro dialogové okno souboru
        root.withdraw()  # Skrytí hlavního okna aplikace
        key_file = filedialog.askopenfilename(filetypes=[('Key files', '*.key')])  # Dialogové okno pro výběr souboru s klíčem

        with open(key_file, 'rb') as f:  # Otevření souboru s klíčem pro čtení bytů
            key = f.read()  # Načtení klíče ze souboru

        f = Fernet(key)  # Inicializace instance třídy Fernet s načteným klíčem
        decrypted_text = f.decrypt(encrypted_text.encode())  # Dešifrování zadaného zašifrovaného textu pomocí třídy Fernet
        return decrypted_text.decode()  # Vrácení dešifrovaného textu v řetězcové podobě
    except Exception as e:  # Výjimka pro případ chyby
        log.log_Error ( 'Des' , 'chyba šifrovaní ' )
        return None  # Vrácení hodnoty None pro indikaci chyby