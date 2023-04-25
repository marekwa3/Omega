import json
import mysql.connector

def nacti ( ) :
    """
    metoda pro nacteni dat z souboru c.conf
    """
    text = ""
    try :
        conf = open ("../data/c.conf","r")
    except :
        raise Exception ( "Nelze nacist soubor" )
    else :
        for line in conf :
            text += line
        conf.close ( )
        return text

""" metody na sebraní dat z načteného souboru """

def host ( ) :
    try :
        data = json.loads ( nacti ( ) )
        return data ['host']
    except :
        raise Exception ( "Nelze nacist host data" )


def user ( ) :
    try :
        data = json.loads ( nacti ( ) )
        return data ['user']
    except :
        raise Exception ( "Nelze nacist user data" )


def password ( ) :
    try :
        data = json.loads ( nacti ( ) )
        return data ['password']
    except :
        raise Exception ( "Nelze nacist password data" )


def database ( ) :
    try :
        data = json.loads ( nacti ( ) )
        return data ['database']
    except :
        raise Exception ( "Nelze nacist database data" )


data1 = host ( )
data2 = user ( )
data3 = password ( )
data4 = database ( )


def Connect ( ) :
    connect = mysql.connector.connect (
        host = data1 ,
        user = data2 ,
        password = data3 ,
        database = data4
    )

    return connect

Connect ( )
