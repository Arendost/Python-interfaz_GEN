##ventanas emergentes

from tkinter import *
from tkinter import messagebox
root=Tk()

############################## Funciones ##########################

def infoadicional():
    messagebox.showinfo("Procesador","Procesador de texto")
def avisolicencia():
    messagebox.showwarning("licencia","producto bajo licencia GNU")  
def saliraplicacion():
    #valor=messagebox.askquestion("salr","deseas salir de la aplicacion") 
    valor=messagebox.askokcancel("salr","deseas salir de la aplicacion") 
    
    if valor==TRUE:    #yes
        root.destroy()
def cerrardocumento():
    valor=messagebox.askretrycancel("reintentar","deseas salir de la aplicacion") 
    if valor==FALSE:
        root.destroy()
    
##############################   Root  ##################################

barraMenu=Menu(root)

root.config(bg="#00AB9A",menu=barraMenu,width=300,height=300)
root.title("TITULO")
root.resizable(0,0)
root.geometry("1200x550")
Label(root,text="TITULO",fg="white",font=("Comid Sans MS", 20),bg="#00AB9A" ).place(x=450,y=25)


frame=Frame(root)
frame.config(bg="white",width=1200,height=450)
frame.pack(side="bottom",anchor="s")







################################ Menu Superior ###############################
AArchivo=Menu(barraMenu,tearoff=0)
AArchivo.add_command(label="nuevo")
AArchivo.add_separator()
AArchivo.add_command(label="guardar")
AArchivo.add_command(label="guardar como")
AArchivo.add_command(label="reinicio",command=cerrardocumento)
AArchivo.add_command(label="salir",command=saliraplicacion)

AEdicion=Menu(barraMenu)
AHerramientas=Menu(barraMenu)

AAyuda=Menu(barraMenu)
AAyuda=Menu(barraMenu,tearoff=0)
AAyuda.add_command(label="Licencia",command=avisolicencia)
AAyuda.add_command(label="acerca de",command=infoadicional)

barraMenu.add_cascade(label="archivo",menu=AArchivo)
barraMenu.add_cascade(label="edicion",menu=AEdicion)
barraMenu.add_cascade(label="herramientas",menu=AHerramientas)
barraMenu.add_cascade(label="ayuda",menu=AAyuda)



#############################################################
root.mainloop()
