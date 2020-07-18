import sqlite3
import sys
from tkinter import messagebox

def conexdb():
    conex=sqlite3.connect("dbase/bdatos")
    cursor=conex.cursor()
    try:
        cursor.execute('''
		    CREATE TABLE JULIO_ANTONIO_MELLA (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                ESCUELA VARCHAR (50),
                EL_TIPO_MODEMS VARCHAR (50),
                CANTIDAD_USUARIOS VARCHAR (50),
                RESP_CONECTIVIDAD VARCHAR (50),
                RESP_SI VARCHAR (50),
                TELEFONO NUMERIC (8),
                IP VARCHAR (15),
                MASC_SUBRED VARCHAR(15),
                P_ENLACE VARCHAR(15),
                COMENTARIO VARCHAR(150))
                ''')
        cursor.execute('''
			CREATE TABLE JOAQUIN_AGUERO (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				ESCUELA VARCHAR (50),
				EL_TIPO_MODEMS VARCHAR (50),
				CANTIDAD_USUARIOS VARCHAR (50),
				RESP_CONECTIVIDAD VARCHAR (50),
				RESP_SI VARCHAR (50),
				TELEFONO NUMERIC (8),
				IP VARCHAR (15),
				MASC_SUBRED VARCHAR(15),
				P_ENLACE VARCHAR(15),
				COMENTARIO VARCHAR(150))
				''')

        cursor.execute('''
			CREATE TABLE CANDIDO_GONZALEZ (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				ESCUELA VARCHAR (50),
				EL_TIPO_MODEMS VARCHAR (50),
				CANTIDAD_USUARIOS VARCHAR (50),
				RESP_CONECTIVIDAD VARCHAR (50),
				RESP_SI VARCHAR (50),
				TELEFONO NUMERIC (8),
				IP VARCHAR (15),
				MASC_SUBRED VARCHAR(15),
				P_ENLACE VARCHAR(15),
				COMENTARIO VARCHAR(150))
				''')
        cursor.execute('''
			CREATE TABLE IGNACIO_AGRAMONTE (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,				
				ESCUELA VARCHAR (50),
				EL_TIPO_MODEMS VARCHAR (50),
				CANTIDAD_USUARIOS VARCHAR (50),
				RESP_CONECTIVIDAD VARCHAR (50),
				RESP_SI VARCHAR (50),
				TELEFONO NUMERIC (8),
				IP VARCHAR (15),
				MASC_SUBRED VARCHAR(15),
				P_ENLACE VARCHAR(15),
				COMENTARIO VARCHAR(150))
				''')
        messagebox.showinfo('Base datos', 'La base datos fue creada correctamente.')
        
    except:
        messagebox.showwarning('Base datos', 'La base datos ya existe')