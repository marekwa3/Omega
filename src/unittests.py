
import unittest

import Encrypter_Descrypter1,Encrypter_Descrypter2,Data_handler

import mysql.connector as mysql



class TestEncryptionFunctions(unittest.TestCase):

    def test_encrypt_decrypt1(self):
        text="Hello, world!"
        key="secret"

        ciphertext_hex=Encrypter_Descrypter1.Encrypt(text,key)
        plaintext=Encrypter_Descrypter1.Decrypt(ciphertext_hex,key)

        self.assertEqual(text,plaintext)

    def test_empty_key(self):
        text="Hello, world!"
        key=""
        ciphertext_hex="some initial value"

        with self.assertRaises(ValueError):
            ciphertext_hex=Encrypter_Descrypter1.Encrypt(text,key)

        with self.assertRaises(ValueError):
            plaintext=Encrypter_Descrypter1.Decrypt(ciphertext_hex,key)

    def test_invalid_hex_string(self):
        ciphertext_hex="invalid_hex_string"
        key="secret"

        with self.assertRaises(ValueError):
            plaintext=Encrypter_Descrypter1.Decrypt(ciphertext_hex,key)

    def test_encrypt_decrypt2(self):
        text="Hello, world!"
        encrypted_message_str=Encrypter_Descrypter2.Encrypt(text)
        decrypted_text=Encrypter_Descrypter2.Decrypt(encrypted_message_str)
        self.assertEqual(text,decrypted_text)

class TestInsert(unittest.TestCase):

    def test_insert_x1(self):
        result = Data_handler.insert("my_key", "my_text", "1", "my_user", "my_title")
        self.assertEqual(result, None)

    def test_insert_x2(self):
        result = Data_handler.insert("my_key", "my_text", "2", "my_number", "my_title")
        self.assertEqual(result, None)
class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Connect to the database
        self.connection = mysql.connect(
            host='localhost',
            user='root',
            password='',
            database='Secret'
        )
        self.create_table()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Uzivatel (id int primary key auto_increment, jmeno varchar(20), heslo varchar(50) not null, cislo numeric)')

    def test_insert_and_delete(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Uzivatel (jmeno, heslo, cislo) VALUES ('Jan', 'heslo123', 123)")
        cursor.execute("INSERT INTO Uzivatel (jmeno, heslo, cislo) VALUES ('Petr', 'heslo456', 456)")
        self.connection.commit()

        cursor.execute("DELETE FROM Uzivatel WHERE jmeno = 'Jan'")
        self.connection.commit()

        cursor.execute("SELECT * FROM Uzivatel WHERE jmeno = 'Jan'")
        self.assertEqual(len(cursor.fetchall()), 0)


if __name__=='__main__':
    unittest.main()