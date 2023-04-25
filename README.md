# Omega
Secret data
Secret data projekt umožňuje nejen šifrovat data metodami XOR a Fernet, ale také editovat již šifrovaná data. 
Navíc je k dispozici jednoduchý slovník, který si uživatel může naplnit sám a data z něj jsou ukládána do databáze MySQL.

Instalace
Stáhněte si projekt Secret data.
Rozbalte soubory do složky na vašem počítači.
Nainstalujte potřebné balíčky (tkinter filedialog , messagebox , logging , re , Toolbox , itertools ,mailbox , PIL ,  mysql-connector )
Nakonfigurujte připojení k databázi MySQL v souboru c.conf.

po spuštění
Zobrazí se hlavní menu s možnostmi přihlášení a registrace.
Pokud nemáte účet, můžete se zaregistrovat kliknutím na tlačítko "Registrovat se".
Po úspěšném přihlášení nebo registraci se zobrazí další menu s možností výběru šifrovací metody - XOR nebo Fernet.
Zvolte šifrovací metodu a zadejte text, který chcete zašifrovat.
U metody XOR zadejte klíč, který chcete použít k zašifrování textu.
Klikněte na tlačítko "Šifrovat" a zobrazí se zašifrovaný text.
Klikněte na tlačítko "Uložit do databáze" a zašifrovaný text se uloží do databáze MySQL.
Pokud chcete dešifrovat text, vyberte ho z databáze a klikněte na tlačítko "Dešifrovat".
U metody XOR zadejte správný klíč pro dešifrování textu.
Dešifrovaný text se zobrazí v aplikaci.

Popis šifrování
Tento projekt podporuje dva druhy šifrování: XOR a Fernet.

XOR šifrování je symetrická šifra, která využívá operaci XOR pro šifrování a dešifrování dat. Pro šifrování se používá klíč, který má stejnou délku jako data. Pokud jsou klíč a data stejně dlouhé, lze pomocí XOR šifry snadno zašifrovat a dešifrovat data.

Fernet šifrování je druh šifrování, který používá stejný klíč pro šifrování a dešifrování dat. Klíč je velmi důležitý, protože pokud bude někdo znát váš klíč, bude moci přečíst vaše zašifrovaná data. Proto je důležité, aby byl klíč chráněn a uchováván v bezpečí.
klíč se v mém projektu ukládá do souboru

Ukázky použití
Následující ukázka kódu ukazuje, jak lze použít metodu XOR pro šifrování dat:

from encryption import XOR

key = "my_secret_key"
data = b"my_data_to_encrypt"
xored_data = XOR.encrypt(key, data)

Tato ukázka kódu ukazuje, jak lze použít metodu Fernet pro šifrování dat:

# generování klíče
key = Fernet.generate_key()
# inicializace Fernet objektu s klíčem
fernet = Fernet(key)

# data k zašifrování
data = b"my_data_to_encrypt"
# šifrování dat pomocí Fernet objektu
fernet_data = fernet.encrypt(data)

Přispívání
Jsme otevřeni přispění nových funkcí nebo oprav chyb v našem projektu. Pokud máte nápad na vylepšení, můžete nás kontaktovat na emailu maly@spsejecna.cz.

Autor
Tento projekt byl vytvořen jednotlivcem. Pokud máte jakékoliv dotazy nebo připomínky, kontaktujte mě na emailu maly@spsejecna.cz.

Licence
Tento projekt je licencován pod MIT licencí, více informací naleznete v souboru LICENSE.

Podpora
Pokud máte jakékoli dotazy ohledně tohoto projektu, můžete mě kontaktovat na emailu maly@spsejecna.cz.
