import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from tkinter import Tk
from tkinter import Frame
#Find closest
fenetre=Tk()
Largeur = 800
Hauteur = 500
Canevas = Canvas(fenetre, width=Largeur, height=Hauteur,bg="grey")
Canevas.pack()
switch_import = PhotoImage(file="switch.png")
pc_import = PhotoImage(file="pc.png")
routeur_import = PhotoImage(file="routeur.png")
Switch_depart=Canevas.create_image(100, 100, image=switch_import)
Canevas.update()
liste_element=[]
Element=Switch_depart
liste_element.append(Switch_depart)


def Close():
        fenetre.destroy()

def SwitchSpawn(event=None):
        Switch=Canevas.create_image(100, 100, image=switch_import)
        Canevas.update()
        liste_element.append(Switch)

def RouteurSpawn(event=None):
        Routeur=Canevas.create_image(100, 100, image=routeur_import)
        Canevas.update()
        liste_element.append(Routeur)

def OrdinateurSpawn(event=None):
        Ordinateur=Canevas.create_image(100, 100, image=pc_import)
        Canevas.update()
        liste_element.append(Ordinateur)

def Deplacement(event):
        global Element
        x=event.x
        y=event.y
        if x<=800 and y<=500 and x>=0 and y>=0:
                outils=Canevas.find_closest(x,y)
                Element=outils
                Canevas.coords(Element,x,y)

def Suppression(event):
        global Element
        x=event.x
        y=event.y
        suppression=Canevas.find_closest(x,y)
        Canevas.delete(fenetre,suppression)
        Element=liste_element[0]
        #GESTION DE LA LISTE A FAIRE

menu=Menu(fenetre)
fenetre.config(menu=menu)
SousMenu=Menu(menu)
menu.add_cascade(label="Outils", menu=SousMenu)
SousMenu.add_command(label="Switch",command=SwitchSpawn)
SousMenu.add_command(label="Routeur",command=RouteurSpawn)
SousMenu.add_command(label="Ordinateur",command=OrdinateurSpawn)
Quitter=Menu(menu)
menu.add_cascade(label="Quitter",menu=Quitter)
Quitter.add_command(label="Exit",command=Close)

Canevas.bind('<B1-Motion>',Deplacement)
Canevas.bind('<Double-Button-1>',Suppression)
fenetre.bind("<c>",OrdinateurSpawn)
fenetre.bind("<s>",SwitchSpawn)
fenetre.bind("<r>",RouteurSpawn)
fenetre.mainloop()