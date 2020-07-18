from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import sqlite3

import sys
sys.path.insert(0, 'D:/Installers/Curso Python/archivos/intefaz grafica/ttk/completo/main.py')

#Crear registro --------
def crear(**data):
	conex=sqlite3.connect("dbase/bdatos")
	cursor=conex.cursor()
	if data['opcionvar']==0:		
		cursor.execute("INSERT INTO JOAQUIN_AGUERO VALUES(NULL,'" + data['escuela'] +
			"','" + data['moden'] +
			"','" + data['usuario'] +
			"','" + data['respcon'] +
			"','" + data['respsi'] + 
			"','" + data['telefono'] +
			"','" + data['ip'] +
			"','" + data['mascara'] + 
			"','" + data['puerta'] +
			"','" + data['text'] +"')")
		conex.commit()
		messagebox.showinfo("Base datos","Registro insertado con éxito en distrito Joaquín Aguero")
		conex.close()

	elif data['opcionvar']==1:
		cursor.execute("INSERT INTO IGNACIO_AGRAMONTE VALUES(NULL,'" + data['escuela'] +
			"','" + data['moden'] +
			"','" + data['usuario'] +
			"','" + data['respcon'] +
			"','" + data['respsi'] + 
			"','" + data['telefono'] +
			"','" + data['ip'] +
			"','" + data['mascara'] + 
			"','" + data['puerta'] +
			"','" + data['text'] +"')")
		conex.commit()
		messagebox.showinfo("Base datos","Registro insertado con éxito en distrito Ignacio Agramonte")
		conex.close()

	elif data['opcionvar']==2:
		cursor.execute("INSERT INTO JULIO_ANTONIO_MELLA VALUES(NULL,'" + data['escuela'] +
			"','" + data['moden'] +
			"','" + data['usuario'] +
			"','" + data['respcon'] +
			"','" + data['respsi'] + 
			"','" + data['telefono'] +
			"','" + data['ip'] +
			"','" + data['mascara'] + 
			"','" + data['puerta'] +
			"','" + data['text'] +"')")
		conex.commit()
		messagebox.showinfo("Base datos","Registro insertado con éxito en distrito Julio Antonio Mella")
		conex.close()

	elif data['opcionvar']==3:
		cursor.execute("INSERT INTO CANDIDO_GONZALEZ VALUES(NULL,'" + data['escuela'] +
			"','" + data['moden'] +
			"','" + data['usuario'] +
			"','" + data['respcon'] +
			"','" + data['respsi'] + 
			"','" + data['telefono'] +
			"','" + data['ip'] +
			"','" + data['mascara'] + 
			"','" + data['puerta'] +
			"','" + data['text'] +"')")
		conex.commit()
		messagebox.showinfo("Base datos","Registro insertado con éxito en distrito Candido González")
		conex.close()
	else:
		messagebox.showwarning("Base datos","Debe llenar los campos por favor")

#actualizar registro
def actualizar(**data):
	conex = sqlite3.connect("dbase/bdatos")
	cursor = conex.cursor()
	datos_actualizar = data['moden'],data['usuario'], data['respcon'], data['respsi'], data['telefono'], data['ip'],data['mascara'],data['escuela'],data['text']
	dat_escuela = data['escuela']

	if data['opcionvar']==0:
		cursor.execute('UPDATE JOAQUIN_AGUERO SET EL_TIPO_MODEMS=?, CANTIDAD_USUARIOS=?,RESP_CONECTIVIDAD=?, RESP_SI=?,TELEFONO=?,IP=?,MASC_SUBRED=?,P_ENLACE=?,COMENTARIO=?' +
			'WHERE ESCUELA="%s"' %(dat_escuela),(datos_actualizar))

		conex.commit()
		messagebox.showinfo("Base datos", "Registro actualizado con éxito en distrito Joaquín Aguero")

	elif data['opcionvar']==1:
		cursor.execute('UPDATE IGNACIO_AGRAMONTE SET EL_TIPO_MODEMS=?, CANTIDAD_USUARIOS=?,RESP_CONECTIVIDAD=?, RESP_SI=?,TELEFONO=?,IP=?,MASC_SUBRED=?,P_ENLACE=?,COMENTARIO=?' +
			'WHERE ESCUELA="%s"' %(dat_escuela),(datos_actualizar))

		conex.commit()

		messagebox.showinfo("Base datos", "Registro actualizado con éxito en distrito Ignacio Agramonte")

	elif data['opcionvar']==2:
		cursor.execute('UPDATE JULIO_ANTONIO_MELLA SET EL_TIPO_MODEMS=?, CANTIDAD_USUARIOS=?,RESP_CONECTIVIDAD=?, RESP_SI=?,TELEFONO=?,IP=?,MASC_SUBRED=?,P_ENLACE=?,COMENTARIO=?' +
			'WHERE ESCUELA="%s"' %(dat_escuela),(datos_actualizar))

		conex.commit()

		messagebox.showinfo("Base datos", "Registro actualizado con exito en distrito Julio Antonio Mella")


	elif data['opcionvar']==3:
		cursor.execute('UPDATE CANDIDO_GONZALEZ SET EL_TIPO_MODEMS=?, CANTIDAD_USUARIOS=?,RESP_CONECTIVIDAD=?, RESP_SI=?,TELEFONO=?,IP=?,MASC_SUBRED=?,P_ENLACE=?,COMENTARIO=?' +
			'WHERE ESCUELA="%s"' %(dat_escuela),(datos_actualizar))

		conex.commit()


		messagebox.showinfo("Base datos", "Registro actualizado con éxito en distrito Cándido González")
		
#borrar regitro base dato
def borrar_base(**data):
	nombre_borrar=data['escuela']
	conex = sqlite3.connect("dbase/bdatos")
	cursor = conex.cursor()

	if data['opcionvar']==0:
		cursor.execute('DELETE FROM JOAQUIN_AGUERO WHERE ESCUELA="%s"'%(nombre_borrar,))
		conex.commit()
		messagebox.showinfo("Borrar Base Datos", "Registro borrado de la base datos correctamente")		

	elif data['opcionvar']==1:
		cursor.execute('DELETE FROM IGNACIO_AGRAMONTE WHERE ESCUELA="%s"'%(nombre_borrar,))
		conex.commit()
		messagebox.showinfo("Borrar Base Datos", "Registro borrado de la base datos correctamente")		

	elif data['opcionvar']==2:
		cursor.execute('DELETE FROM JULIO_ANTONIO_MELLA WHERE ESCUELA="%s"'%(nombre_borrar,))
		conex.commit()
		messagebox.showinfo("Borrar Base Datos", "Registro borrado de la base datos correctamente")		

	elif data['opcionvar']==3:
		cursor.execute('DELETE FROM CANDIDO_GONZALEZ WHERE ESCUELA="%s"'%(nombre_borrar,))
		conex.commit()
		messagebox.showinfo("Borrar Base Datos", "Registro borrado de la base datos correctamente")			

#Buscar en el registro
def buscar(*data):
	conex=sqlite3.connect("dbase/bdatos")
	cursor1=conex.cursor()
	
	if data[10].get()==0:
		cursor1.execute('SELECT * FROM JOAQUIN_AGUERO WHERE ESCUELA="%s"'%(data[0].get(),))
		busqueda1=cursor1.fetchall()
		for buscar1 in busqueda1:
			data[1].set(buscar1[2])
			data[2].set(buscar1[3])
			data[3].set(buscar1[4])
			data[4].set(buscar1[5])
			data[5].set(buscar1[6])
			data[6].set(buscar1[7])
			data[7].set(buscar1[8])
			data[8].set(buscar1[9])
			data[9].insert(1.0,buscar1[10])
		conex.commit()

	elif data[10].get()==1:
		cursor1.execute('SELECT * FROM IGNACIO_AGRAMONTE WHERE ESCUELA="%s"'%(data[0].get(),))
		busqueda1=cursor1.fetchall()
		for buscar1 in busqueda1:
			data[1].set(buscar1[2])
			data[2].set(buscar1[3])
			data[3].set(buscar1[4])
			data[4].set(buscar1[5])
			data[5].set(buscar1[6])
			data[6].set(buscar1[7])
			data[7].set(buscar1[8])
			data[8].set(buscar1[9])
			data[9].insert(1.0,buscar1[10])

		conex.commit()
	elif data[10].get()==2:
		cursor1.execute('SELECT * FROM JULIO_ANTONIO_MELLA WHERE ESCUELA="%s"'%(data[0].get(),))
		busqueda1=cursor1.fetchall()
		for buscar1 in busqueda1:
			data[1].set(buscar1[2])
			data[2].set(buscar1[3])
			data[3].set(buscar1[4])
			data[4].set(buscar1[5])
			data[5].set(buscar1[6])
			data[6].set(buscar1[7])
			data[7].set(buscar1[8])
			data[8].set(buscar1[9])
			data[9].insert(1.0,buscar1[10])
		conex.commit()

	elif data[10].get()==3:
		cursor1.execute('SELECT * FROM CANDIDO_GONZALEZ WHERE ESCUELA="%s"'%(data[0].get(),))
		busqueda1=cursor1.fetchall()
		for buscar1 in busqueda1:
			data[1].set(buscar1[2])
			data[2].set(buscar1[3])
			data[3].set(buscar1[4])
			data[4].set(buscar1[5])
			data[5].set(buscar1[6])
			data[6].set(buscar1[7])
			data[7].set(buscar1[8])
			data[8].set(buscar1[9])
			data[9].insert(1.0,buscar1[10])
		conex.commit()


#Limpiar
def clear(*data):
	data[0].set('')
	data[1].set('')
	data[2].set('')
	data[3].set('')
	data[4].set('')
	data[5].set('')
	data[6].set('')
	data[7].set('')
	data[8].set('')
	data[9].delete(1.0,END)
	data[10].focus()

#Limitadores de espacio
def limitador(eltelefono):
	if len(eltelefono.get())>0:
		eltelefono.set(eltelefono.get()[:8])

def limitador2(lamascred):
	if len(lamascred.get())>0:
		lamascred.set(lamascred.get()[:15])
			
def limitador1(elip):
	if len(elip.get())>0:
		elip.set(elip.get()[:15])

def limitador3(lapuertenlc):				
	if len(lapuertenlc.get())>0:
		lapuertenlc.set(lapuertenlc.get()[:15])

#Cerrar Programa
def salir(principal):
	confir = messagebox.askyesno('Advertencia', 'Estas seguro que desas salir')
	if confir:
		principal.destroy()

