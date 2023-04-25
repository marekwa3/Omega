import Encrypter_Descrypter1
import Encrypter_Descrypter2
import Connection
import log
import mysql.connector.errors


def insert ( va1 , va2 , x , y , va3 ) :
    """
    metoda pro insert do databáze
    va1 = klic
    va2 = text na zašifrovaní
    va3 = nazev textu
    """
    try :
        if x == "1" :
            a = Connection.Connect ( )
            a.autocommit = False
            mycursor = a.cursor ( )

            va_y = y
            va = Encrypter_Descrypter1.Encrypt ( va2 , va1 )
            va2 = va

            sql = "INSERT INTO `Secret_Data` (`f_uzivatel`, `nazev` , `text`) VALUES (%s,%s,%s);"
            values = (va_y , va3 , va2)
            mycursor.execute ( sql , values )
            a.commit ( )
            log.log_Info ( 'Data_handeler' , 'vložení x 1 dokončeno ' )
            a.close ( )

        elif x == "2" :
            a = Connection.Connect ( )
            a.autocommit = False
            mycursor = a.cursor ( )

            log.log_Info ( 'Data_handeler' , 'Začala nová registrace ' )

            sql = "INSERT INTO `secret`.`uzivatel` ( `jmeno`, `heslo`, `cislo`) VALUES (%s,%s,%s);"

            values = (va1 , va2 , y)
            mycursor.execute ( sql , values )
            a.commit ( )
            log.log_Info ( 'Data_handeler' , 'registrace úspěšně dokončena' )

            a.close ( )

        elif x == "3" :
            a = Connection.Connect ( )
            a.autocommit = False
            mycursor = a.cursor ( )

            print ( "\npridani textu \n" )

            va_y = y
            va = Encrypter_Descrypter2.Encrypt ( va2 )
            va2 = va

            sql = "INSERT INTO `Secret_Data` (`f_uzivatel`, `nazev` , `text`) VALUES (%s,%s,%s);"
            values = (va_y , va3 , va2)
            mycursor.execute ( sql , values )
            a.commit ( )
            log.log_Info ( 'Data_handeler' , 'vložení x 2 dokončeno ' )
            a.close ( )

    except mysql.connector.errors.IntegrityError as e :
        a.rollback ( )
        log.log_Warning ( 'Data_handeler' , f'Chyba při vkládání do databáze: {e}' )
    except Exception as e :
        log.log_Warning ( 'Data_handeler' , f'Neočekávaná chyba: {e}' )


def delete ( x , id ) :
    mycursor = Connection.Connect ( )

    conn = Connection.Connect ( )
    c = conn.cursor ( )
    c.execute ( "SELECT f_uzivatel FROM secret_data where id = " + id + ";" )
    data = c.fetchall ( )
    ddata = (data[ 0 ])

    a = Connection.Connect ( )
    a.autocommit = False
    print ( "delete text" )

    mycursor = a.cursor ( )
    sql = "DELETE FROM `secret_data` where id = " + id + ""
    try :
        if x == ddata[ 0 ] :
            print ( "proslo" )
            mycursor.execute ( sql )
            a.commit ( )
            print ( "dokonceno" )
        else :
            print ( "toto neni vase " )
    except :

        a.rollback ( )

        print ( "nedokončeno z důvodu chyby" )

    a.close ( )


def delete_user ( x , text ) :
    conn = Connection.Connect ( )
    conn.autocommit = False
    cursor = conn.cursor ( )
    query = "SELECT heslo FROM Uzivatel where id =" + str ( x ) + ";"
    cursor.execute ( query )
    result = cursor.fetchone ( )
    heslo_db = result[ 0 ]
    password = str ( text )

    if heslo_db == password :
        log.log_Info ( "delete" , "uzivatel: " + str ( x ) + " se zmazal  " )

        a = Connection.Connect ( )
        mycursor = a.cursor ( )
        sql = "DELETE FROM `secret_data` where f_uzivatel = " + str ( x ) + ""
        mycursor.execute ( sql )
        a.commit ( )
        a = Connection.Connect ( )
        mycursor = a.cursor ( )
        sql = "DELETE FROM `Uzivatel` where id = " + str ( x ) + ""
        mycursor.execute ( sql )
        a.commit ( )

    else :

        log.log_Warning ( "delete" , "uzivatel:" + str ( x ) + " se zmazal pokusil smazat sam sebe  " )


def select_text ( text , key , x ) :
    conn = Connection.Connect ( )
    conn.autocommit = False
    cursor = conn.cursor ( )
    query = "SELECT f_uzivatel FROM secret_data where id =" + text + ";"
    cursor.execute ( query )
    control_id = cursor.fetchone ( )
    control_id_final = control_id[ 0 ]

    if x == control_id_final :
        conn = Connection.Connect ( )
        conn.autocommit = False
        cursor = conn.cursor ( )
        query = "SELECT text FROM secret_data where id =" + text + ";"
        cursor.execute ( query )
        result = cursor.fetchone ( )
        text_ensrypted = result[ 0 ]

        text_final = Encrypter_Descrypter1.Decrypt ( text_ensrypted , key )
    else :
        text_final = "toto bohužel není vaše"

    return (text_final)


def select_text2 ( text , x ) :
    conn = Connection.Connect ( )
    conn.autocommit = False
    cursor = conn.cursor ( )
    query = "SELECT f_uzivatel FROM secret_data where id =" + text + ";"
    cursor.execute ( query )
    control_id = cursor.fetchone ( )
    control_id_final = control_id[ 0 ]

    if x == control_id_final :
        conn = Connection.Connect ( )
        conn.autocommit = False
        cursor = conn.cursor ( )
        query = "SELECT text FROM secret_data where id =" + text + ";"
        cursor.execute ( query )
        result = cursor.fetchone ( )
        text_ensrypted = result[ 0 ]

        text_final = Encrypter_Descrypter2.Decrypt ( text_ensrypted )
    else :
        text_final = "toto bohužel není vaše"

    return (text_final)


def start_update ( text , id , key , x ) :
    text_enscrypted = Encrypter_Descrypter1.Encrypt ( text , key )

    a = Connection.Connect ( )
    mycursor = a.cursor ( )
    sql = "UPDATE Secret_data SET text = '" + text_enscrypted + "' WHERE id = " + str ( id ) + ";"
    mycursor.execute ( sql )
    a.commit ( )


def start_update2 ( text , id , x ) :
    text_enscrypted = Encrypter_Descrypter2.Encrypt ( text )

    a = Connection.Connect ( )
    mycursor = a.cursor ( )
    sql = "UPDATE Secret_data SET text = '" + text_enscrypted + "' WHERE id = " + str ( id ) + ";"
    mycursor.execute ( sql )
    a.commit ( )
