from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

class AlumnoTk:
    
    def __init__(self,app):
        self.app = app
        self.app.title('Alumnos')
        self.app.geometry('640x480')
        
        frame = LabelFrame(self.app, text='Registrar nuevo alumno')
        frame.grid(row=0, column=0, columnspan=2, pady=10,padx=50)
        
        lb_dni = Label(frame, text='DNI')
        lb_dni.grid(row=1, column=0)
        self.txt_dni = Entry(frame)
        self.txt_dni.grid(row=1, column=1)
        
        lb_nombre = Label(frame, text='Nombre')
        lb_nombre.grid(row=2, column=0)
        self.txt_nombre = Entry(frame)
        self.txt_nombre.grid(row=2, column=1)
        
        btn_insertar = Button(frame, text='Insertar',command=self.insertar)
        btn_insertar.grid(row=3, columnspan=2, sticky=W+E)
        
        #grilla de alumnos
        self.tree = Treeview(self.app, columns=('DNI','Nombre'))
        self.tree.grid(row=4, column=0, columnspan=2,padx=10,pady=10)
        self.tree.heading('#0', text='id')
        self.tree.heading('DNI', text='DNI')
        self.tree.heading('Nombre', text='Nombre')
        
    def insertar(self):
        pass
        
app = Tk()
app_alumno = AlumnoTk(app)
app.mainloop()