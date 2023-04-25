import itertools
import log
import tkinter as tk
from tkinter import messagebox

def Encrypt(text, key):
    # Převod řetězců text a key na bajty
    text_bytes = text.encode()
    key_bytes = key.encode()

    # Kontrola typu textu a klíče
    if not isinstance ( text , str ) or not isinstance ( key , str ) :
        messagebox.showerror ( "Error" , "imput text musí být string" )
        return
    if len ( key.strip ( ) ) == 0 :
        messagebox.showerror ( "Error" , "klíč je prázdný" )
        return

    if len ( key_bytes ) < 4 :
        messagebox.showerror ( "Error" , "klíč je krátký" )
        return

    if len ( text.strip ( ) ) == 0 :
        messagebox.showerror ( "Error" , "text je prázdný" )
        return

    # Pokud je text delší než klíč, klíč se zopakuje pomocí cyklu a bude stejně dlouhý jako text

    if len(text_bytes) > len(key_bytes):
        repeated_key = bytes(itertools.islice(itertools.cycle(key_bytes), len(text_bytes)))
    else:
        repeated_key = key_bytes[:len(text_bytes)]

    # Pro každý bajt textu se provede operace XOR s odpovídajícím bajtem klíče
    # Výsledkem této operace je nový bajt, který je uložen do výsledného bajtového řetězce
    result = bytearray(x ^ y for x, y in zip(text_bytes, repeated_key))
    return result.hex()


def Decrypt(ciphertext_hex, key):
    # Zkontrolujeme, zda vstupní parametry ciphertext_hex a key jsou řetězce
    if not isinstance(ciphertext_hex, str) or not isinstance(key, str):
        raise TypeError("Input ciphertext and key must be strings")
    # Dekódujeme hexadecimální řetězec ciphertext_hex do bajtového řetězce ciphertext
    ciphertext = bytes.fromhex(ciphertext_hex)
    # Převedeme klíč na bajtový řetězec
    key_bytes = key.encode()

    if len(key_bytes) < 1:
        messagebox.showerror ( "Error" , "key je prázdný" )
        return

    # Pokud je text delší než klíč, klíč se zopakuje pomocí cyklu a bude stejně dlouhý jako text
    if len(ciphertext) > len(key_bytes):
        repeated_key = bytes(itertools.islice(itertools.cycle(key_bytes), len(ciphertext)))
    else:
        repeated_key = key_bytes[:len(ciphertext)]
    # Dekódujeme šifrovaný text pomocí operace XOR s opakovaným klíčem
    result = bytearray(x ^ y for x, y in zip(ciphertext, repeated_key))
    return result.decode()




