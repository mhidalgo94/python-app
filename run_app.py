from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import os
import sys

from ui import funciones
from dbase.dbase import conexdb

class App_General():


	def __init__(self, principal, funciones):
		self.func = funciones
		self.principal = principal
		self.principal.title("Primera App")
		self.principal.geometry("619x595+500+250")
		self.principal.resizable(False, False)

		
		self.bmenu = Menu(self.principal)
		self.principal.config(menu=self.bmenu, width=400, height=400)

		self.archivomenu=Menu(self.bmenu,tearoff=0)
		self.archivomenu.add_command(label="Conectar Base Datos",command=conexdb)

		self.archivomenu.add_separator()
		self.archivomenu.add_command(label="Salir", command=self.salir)
		self.edicionmenu=Menu(self.bmenu,tearoff=0)
		self.edicionmenu.add_command(label="Crear",command=self.crear)
		self.edicionmenu.add_command(label="Buscar",command=self.buscar)
		self.edicionmenu.add_command(label="Limpiar",command=self.limpiar)
		self.edicionmenu.add_command(label="Actualizar",command=self.actualizar)

		self.edicionmenu.add_command(label="Borrar Base Datos", command=self.borrar_base)

		self.ayudamenu=Menu(self.bmenu,tearoff=0)
		self.ayudamenu.add_command(label="Requisitos")
		self.ayudamenu.add_command(label="Acerca de..")

		self.bmenu.add_cascade(label="Archivo", menu=self.archivomenu)
		self.bmenu.add_cascade(label="Edicion", menu=self.edicionmenu)
		self.bmenu.add_cascade(label="Ayuda", menu=self.ayudamenu)


		self.fram1=Frame(self.principal)
		self.fram1.pack()

		self.laescuela=StringVar()
		self.eltipomodem=StringVar()
		self.lacantusu=StringVar()
		self.elrespconect=StringVar()
		self.elrespsi=StringVar()
		self.eltelefono=StringVar()
		self.elip=StringVar()
		self.lamascred=StringVar()
		self.lapuertenlc=StringVar()
		self.opcionvar=IntVar()
		

		#Limitadores
		self.eltelefono.trace("w", lambda *args: self.func.limitador(self.eltelefono))
		self.elip.trace("w", lambda *args: self.func.limitador1(self.elip))
		self.lamascred.trace("w", lambda *args: self.func.limitador2(self.lamascred))
		self.lapuertenlc.trace("w", lambda *args: self.func.limitador3(self.lapuertenlc))


		self.txtid=ttk.LabelFrame(self.fram1,text="Inserte los datos requeridos")
		self.txtid.grid(row=0, column=0, sticky="e", padx=10, pady=10)

		self.LabelFrame1=ttk.LabelFrame(self.txtid,text="Seleccione el distrito")
		self.LabelFrame1.grid(row=1,column=2,sticky=W,rowspan=6)

		ttk.Radiobutton(self.LabelFrame1,text="Joaquín Aguero",variable=self.opcionvar,value=0).grid(row=1,column=2,sticky="w",pady=10)

		ttk.Radiobutton(self.LabelFrame1, text="I. Agramonte",variable=self.opcionvar,value=1).grid(row=2,column=2,sticky="w",pady=10)

		ttk.Radiobutton(self.LabelFrame1, text="Julio A. Mella",variable=self.opcionvar,value=2).grid(row=3,column=2,sticky="w",pady=10)

		ttk.Radiobutton(self.LabelFrame1, text="Cándido González",variable=self.opcionvar,value=3).grid(row=4,column=2,sticky="w",pady=10)

		self.cuadroescuela=ttk.Entry(self.txtid, textvariable=self.laescuela,font=("Perpetua",12,"normal"))
		self.cuadroescuela.focus()
		self.cuadroescuela.grid(row=2, column=1, sticky="w")

		self.cuadrotipomodem=ttk.Entry(self.txtid, textvariable=self.eltipomodem,font=("Perpetua",12,"normal"))
		self.cuadrotipomodem.grid(row=3, column=1, sticky="w")

		self.cuadrocantusu=ttk.Entry(self.txtid, textvariable=self.lacantusu,font=("Perpetua",12,"normal"))
		self.cuadrocantusu.grid(row=4, column=1, sticky="w")

		self.cuadrorespconect=ttk.Entry(self.txtid, textvariable=self.elrespconect,font=("Perpetua",12,"normal"))
		self.cuadrorespconect.grid(row=5, column=1, sticky="w")

		self.cuadrorespsi=ttk.Entry(self.txtid, textvariable=self.elrespsi,font=("Perpetua",12,"normal"))
		self.cuadrorespsi.grid(row=6, column=1, sticky="w")

		self.cuadrotelefono=ttk.Entry(self.txtid, textvariable=self.eltelefono,font=("Perpetua",12,"normal"))
		self.cuadrotelefono.grid(row=7, column=1, columnspan=2,sticky="w")

		self.txtipcentros=ttk.LabelFrame(self.txtid,text="Ip Centro Conectado")
		self.txtipcentros.grid(row=8, column=0, padx=10, pady=10,columnspan=3)
		#txtipcentros.config(bg="dark turquoise", fg="Blue")



		self.cuadroip=ttk.Entry(self.txtipcentros, textvariable=self.elip,font=("Console",11,"normal"),justify="right")
		self.cuadroip.grid(row=1, column=0,sticky="w",padx=10,pady=10)

		self.cuadromasc=ttk.Entry(self.txtipcentros, textvariable=self.lamascred,font=("Console",11,"normal"),justify="right")
		self.cuadromasc.grid(row=1, column=1, padx=10,pady=10,sticky="w")

		self.cuadropenlc=ttk.Entry(self.txtipcentros, textvariable=self.lapuertenlc,font=("Console",11,"normal"),justify="right")
		self.cuadropenlc.grid(row=1, column=2,sticky="w",padx=10)

		self.textocomentario=Text(self.txtid, width=36, height=5,font=("Perpetua",15,"normal"))
		self.textocomentario.grid(row=11,column=1, padx=10,pady=10, columnspan=2)

		self.scrollcoment=Scrollbar(self.txtid, command=self.textocomentario.yview)
		self.scrollcoment.grid(row=11, column=3, sticky="nsw")

		self.textocomentario.config(yscrollcommand=self.scrollcoment.set)

		#-----------------------------Labels---------------------------#

		self.txtescuela=ttk.Label(self.txtid,text="Escuelas: ",font=("Perpetua",12,"normal"))
		self.txtescuela.grid(row=2, column=0, sticky="e", padx=10, pady=10)

		self.txttipmodems=ttk.Label(self.txtid,text="Tipo Modems: ",font=("Perpetua",12,"normal"))
		self.txttipmodems.grid(row=3, column=0, sticky="e", padx=10, pady=10)

		self.txtcanusu=ttk.Label(self.txtid,text="Cantidad Usuarios: ",font=("Perpetua",12,"normal"))
		self.txtcanusu.grid(row=4, column=0, sticky="e", padx=10, pady=10)

		self.txtrconect=ttk.Label(self.txtid,text="Responsable Conectividad: ",font=("Perpetua",12,"normal"))
		self.txtrconect.grid(row=5, column=0, sticky="e", padx=10, pady=10)

		self.txtrseginf=ttk.Label(self.txtid,text="Responsable Seguridad Informática: ",font=("Perpetua",12,"normal"))
		self.txtrseginf.grid(row=6, column=0, sticky="e", padx=10, pady=10)

		self.txttelefono=ttk.Label(self.txtid,text="Teléfono: ",font=("Perpetua",12,"normal"))
		self.txttelefono.grid(row=7, column=0, sticky="e", padx=10, pady=10)


		self.txtip=ttk.Label(self.txtipcentros,text="Ip",font=("Perpetua",13,"normal"))
		self.txtip.grid(row=0, column=0, padx=10,sticky=N+S)

		self.txtmasc=ttk.Label(self.txtipcentros,text="Mascara Subred",font=("Perpetua",13,"normal"))
		self.txtmasc.grid(row=0, column=1, sticky=N+S, padx=10)

		self.txtpuertenl=ttk.Label(self.txtipcentros,text="Pruerta Enlace",font=("Perpetua",13,"normal"))
		self.txtpuertenl.grid(row=0, column=2, sticky=N+S, padx=10)


		self.txtcoment=ttk.Label(self.txtid,text="Comentario: ",font=("Perpetua",13,"normal"))
		self.txtcoment.grid(row=11, column=0, sticky="ne", padx=10, pady=10)
		

		#----------------------------------Botones de accion-----------------------------#
		self.fram2=Frame(self.principal)
		self.fram2.pack()


		self.botonsave=ttk.Button(self.fram2, text="Buscar", command=self.buscar)
		self.botonsave.grid(row=1, column=0, padx=20, pady=10, sticky=W+E)

		self.botonleer=ttk.Button(self.fram2, text="Limpiar",command=self.limpiar)
		self.botonleer.grid(row=1, column=1, padx=20, pady=10, sticky=W+E)

		self.botonclear=ttk.Button(self.fram2, text="Crear",command=self.crear)
		self.botonclear.grid(row=1, column=2, padx=20, pady=10, sticky=W+E)

		self.botonupdate=ttk.Button(self.fram2, text="Actualizar",command=self.actualizar)
		self.botonupdate.grid(row=1, column=3, padx=20, pady=10, sticky=W+E)

		self.botondel=ttk.Button(self.fram2, text="Borrar Base", command=self.borrar_base)
		self.botondel.grid(row=1, column=4, padx=20, pady=10, sticky=W+E)

		self.boton_datos = ttk.Button(self.LabelFrame1,text='Datos Generales', command=self.ventana_btn_datos).grid(row=5,column=2,sticky=W+E,pady=10)


	# Funciones de todos los botones
	def ventana_btn_datos(self):
		self.btn_datos= Toplevel(self.principal)
		self.abrir_btn_datos = ventana_btn_dat(self.btn_datos)

	def limpiar(self):
		
		data = (self.laescuela, self.eltipomodem, self.lacantusu, self.elrespconect, self.elrespsi, self.eltelefono, self.elip, self.lamascred, self.lapuertenlc, self.textocomentario, self.cuadroescuela)
		self.func.clear(*data)

	def crear(self):
		#data = (self.laescuela.get(),self.eltipomodem.get(),self.lacantusu.get(), self.elrespconect.get(), self.elrespsi.get(),self.eltelefono.get(),self.elip.get(),self.lamascred.get(),self.lapuertenlc.get(), self.textocomentario.get("1.0",END))
		if len(self.laescuela.get())>0 and self.laescuela.get()!=int:
			data = {'escuela': self.laescuela.get(),'moden': self.eltipomodem.get(),'usuario': self.lacantusu.get(),'respcon': self.elrespconect.get(),'respsi': self.elrespsi.get(),'telefono': self.eltelefono.get(),'ip': self.elip.get(),'mascara': self.lamascred.get(),'puerta': self.lapuertenlc.get(),'text': self.textocomentario.get("1.0",END), 'opcionvar': self.opcionvar.get()}
			self.func.crear(**data)
		else:
			messagebox.showwarning("Base datos","Debe llenar los campos por favor")

	def actualizar(self):
		data = {'escuela': self.laescuela.get(),'moden': self.eltipomodem.get(),'usuario': self.lacantusu.get(),'respcon': self.elrespconect.get(),'respsi': self.elrespsi.get(),'telefono': self.eltelefono.get(),'ip': self.elip.get(),'mascara': self.lamascred.get(),'puerta': self.lapuertenlc.get(),'text': self.textocomentario.get("1.0",END), 'opcionvar': self.opcionvar.get()}
		self.func.actualizar(**data)
	
	def borrar_base(self):
		data = {'escuela':self.laescuela.get(), 'opcionvar': self.opcionvar.get()}
		self.limpiar()
		self.cuadroescuela.focus()
		self.func.borrar_base(**data)

	def buscar(self):
		data = (self.laescuela, self.eltipomodem, self.lacantusu, self.elrespconect, self.elrespsi, self.eltelefono, self.elip, self.lamascred, self.lapuertenlc, self.textocomentario,self.opcionvar)
		self.func.buscar(*data)

	def salir(self):
		self.func.salir(self.principal)


	

#esta es la ventana de vista general
class ventana_btn_dat:
	def __init__(self, toplevel):
		self.toplevel = toplevel
		self.toplevel.title("Registro Datos")
		self.toplevel.geometry("1225x600")
		self.toplevel.resizable(False,True)

		self.notebook = ttk.Notebook(self.toplevel)
		#notebook['show'] = 'headings'
		self.notebook.pack(expand=True,fill="y")

		self.pestana1 = ttk.Frame(self.notebook)
		self.pestana1.pack(expand=True, fill="y")

		self.pestana2 = ttk.Frame(self.notebook)
		self.pestana2.pack(expand=True, fill="y")

		self.pestana3 = ttk.Frame(self.notebook)
		self.pestana3.pack(expand=True, fill="y")

		self.pestana4 = ttk.Frame(self.notebook)
		self.pestana4.pack(expand=True, fill="y")


		self.notebook.add(self.pestana1, text='Joaquin Aguero')
		self.notebook.add(self.pestana2, text='I. Agramonte')
		self.notebook.add(self.pestana3, text='Julio A Mella')
		self.notebook.add(self.pestana4, text='Cándido González')

		self.tree_pestana1 = ttk.Treeview(self.pestana1,height=10 , columns= ('escuela','usuario', 'telefono', 'ip', 'masksubred', 'puertenlace'))
		self.tree_pestana1.pack(side="left",expand=True, fill="y")
		#tree_pestana1.columnconfigure(0,weight=1)
		#tree_pestana1.rowconfigure(0,weight=1)

		self.tree_pestana1['show'] = 'headings'	
		self.tree_pestana1.heading('#1',text ="Escuela", anchor=CENTER)
		self.tree_pestana1.heading('#2',text ="Cant Usuarios", anchor=CENTER)
		self.tree_pestana1.heading('#3',text ="Teléfono", anchor=CENTER)
		self.tree_pestana1.heading('#4',text ="IP", anchor=CENTER)
		self.tree_pestana1.heading('#5',text ="Mask Subred", anchor=CENTER)
		self.tree_pestana1.heading('#6',text ="Puerta Enlace", anchor=CENTER)


		self.tree_pestana2 = ttk.Treeview(self.pestana2,height=10 , columns= ('escuela','usuario', 'telefono', 'ip', 'masksubred', 'puertenlace'))
		self.tree_pestana2.pack(side="left",expand=True, fill="y")

		self.tree_pestana2['show'] = 'headings'
		self.tree_pestana2.heading('#1',text ="Escuela", anchor=CENTER)
		self.tree_pestana2.heading('#2',text ="Cant Usuarios", anchor=CENTER)
		self.tree_pestana2.heading('#3',text ="Teléfono", anchor=CENTER)
		self.tree_pestana2.heading('#4',text ="IP", anchor=CENTER)
		self.tree_pestana2.heading('#5',text ="Mask Subred", anchor=CENTER)
		self.tree_pestana2.heading('#6',text ="Puerta Enlace", anchor=CENTER)

		self.tree_pestana3 = ttk.Treeview(self.pestana3,height=10 , columns= ('escuela','usuario', 'telefono', 'ip', 'masksubred', 'puertenlace'))
		self.tree_pestana3.pack(side="left",expand=True, fill="y")

		self.tree_pestana3['show'] = 'headings'
		self.tree_pestana3.heading('#1',text ="Escuela", anchor=CENTER)
		self.tree_pestana3.heading('#2',text ="Cant Usuarios", anchor=CENTER)
		self.tree_pestana3.heading('#3',text ="Teléfono", anchor=CENTER)
		self.tree_pestana3.heading('#4',text ="IP", anchor=CENTER)
		self.tree_pestana3.heading('#5',text ="Mask Subred", anchor=CENTER)
		self.tree_pestana3.heading('#6',text ="Puerta Enlace", anchor=CENTER)

		self.tree_pestana4 = ttk.Treeview(self.pestana4,height=10 , columns= ('escuela','usuario', 'telefono', 'ip', 'masksubred', 'puertenlace'))
		self.tree_pestana4.pack(side="left",expand=True, fill="y")

		self.tree_pestana4['show'] = 'headings'
		self.tree_pestana4.heading('#1',text ="Escuela", anchor=CENTER)
		self.tree_pestana4.heading('#2',text ="Cant Usuarios", anchor=CENTER)
		self.tree_pestana4.heading('#3',text ="Teléfono", anchor=CENTER)
		self.tree_pestana4.heading('#4',text ="IP", anchor=CENTER)
		self.tree_pestana4.heading('#5',text ="Mask Subred", anchor=CENTER)
		self.tree_pestana4.heading('#6',text ="Puerta Enlace", anchor=CENTER)
		
		self.scrolltree = ttk.Scrollbar(self.pestana1, command=self.tree_pestana1.yview)
		self.scrolltree.pack(side="right", fill="y")
		self.tree_pestana1.config(yscrollcommand=self.scrolltree.set)
		
		self.scrolltree2 = ttk.Scrollbar(self.pestana2, command=self.tree_pestana2.yview)
		self.scrolltree2.pack(side="right", fill="y")
		self.tree_pestana2.config(yscrollcommand=self.scrolltree2.set)

		self.scrolltree3 = ttk.Scrollbar(self.pestana3, command=self.tree_pestana3.yview)
		self.scrolltree3.pack(side="right", fill="y")
		self.tree_pestana3.config(yscrollcommand=self.scrolltree3.set)

		self.scrolltree4 = ttk.Scrollbar(self.pestana4, command=self.tree_pestana4.yview)
		self.scrolltree4.pack(side="right", fill="y")
		self.tree_pestana4.config(yscrollcommand=self.scrolltree4.set)

		self.tomar_datos_tree()

	def tomar_datos_tree(self):
		conex=sqlite3.connect("dbase/bdatos")
		cursor=conex.cursor()
		#Consultar tabla
		query1 = "SELECT ESCUELA, CANTIDAD_USUARIOS, TELEFONO, IP, MASC_SUBRED, P_ENLACE FROM JOAQUIN_AGUERO"
		cursor.execute(query1)
		db_rows1 = cursor.fetchall() 
		#tree_pestana1.get_children()

		for row in db_rows1:
			
			self.tree_pestana1.insert("",END, text="" , values = row)

		query2 = "SELECT ESCUELA, CANTIDAD_USUARIOS, TELEFONO, IP, MASC_SUBRED, P_ENLACE FROM IGNACIO_AGRAMONTE"
		cursor.execute(query2)
		db_rows2 = cursor.fetchall() 
		#tree_pestana1.get_children()

		for row in db_rows2:
		
			self.tree_pestana2.insert("",END, text="" , values = row)

		query3 = "SELECT ESCUELA, CANTIDAD_USUARIOS, TELEFONO, IP, MASC_SUBRED, P_ENLACE FROM JULIO_ANTONIO_MELLA"
		cursor.execute(query3)
		db_rows3 = cursor.fetchall() 
		#tree_pestana1.get_children()

		for row in db_rows3:
		
			self.tree_pestana3.insert("",END, text="" , values = row)

		query4 = "SELECT ESCUELA, CANTIDAD_USUARIOS, TELEFONO, IP, MASC_SUBRED, P_ENLACE FROM CANDIDO_GONZALEZ"
		cursor.execute(query4)
		db_rows4 = cursor.fetchall() 
		#tree_pestana1.get_children()

		for row in db_rows4:
		
			self.tree_pestana4.insert("",END, text="" , values = row)

		
 
if __name__=="__main__":
	principal= Tk()
	aplicacion = App_General(principal, funciones)
	principal.mainloop()













