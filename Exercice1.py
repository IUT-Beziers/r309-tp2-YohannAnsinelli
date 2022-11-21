import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from tkinter import Tk
from tkinter import Frame
from tkinter.filedialog import *
from tkinter import filedialog
from PIL import Image, ImageTk



#Find closest
fenetre=Tk()
fenetre.title("Réseaux")
Largeur = 800
Hauteur = 500
Canevas = Canvas(fenetre, width=Largeur, height=Hauteur,bg="grey")
Canevas.pack()
switch_import = PhotoImage(file="switch.png")
pc_import = PhotoImage(file="pc.png")
routeur_import = PhotoImage(file="routeur.png")
liste_element=[]
liste_label=[]
element_cable=[]
Element1=0
x=0
y=0
x1=0
y1=0
x2=0
y2=0

def Close():
        fenetre.destroy()

def SwitchSpawn(event=None):
        Switch=Canevas.create_image(100, 100, image=switch_import)
        Canevas.update()
        liste_element.append(Switch)
        texte=Canevas.create_text(100,125,text="Switch")
        liste_label.append(texte)

def CableSpawn(event):
        global x,y,x1,y1,x2,y2,Element1
        x=event.x
        y=event.y
        Element=Canevas.find_closest(x,y)
        if x1==0 and y1==0 and x1!=100 and y1!=100:
                x1=int(Canevas.coords(Element)[0])
                y1=int(Canevas.coords(Element)[1])
                Element1=Element
        elif x2==0 and y2==0 and x1>0 and y1>0:
                x2=int(Canevas.coords(Element)[0])
                y2=int(Canevas.coords(Element)[1])
                Cable=Canevas.create_line(x1,y1,x2,y2,fill='black',width=2)
                element_cable.append([Cable,Element1,Element])
                Canevas.update()
                x1=0
                y1=0
                x2=0
                y2=0

                

def RouteurSpawn(event=None):
        Routeur=Canevas.create_image(100, 100, image=routeur_import)
        Canevas.update()
        liste_element.append(Routeur)
        texte=Canevas.create_text(100,125,text="Routeur")
        liste_label.append(texte)

def OrdinateurSpawn(event=None):
        Ordinateur=Canevas.create_image(100, 100, image=pc_import)
        Canevas.update()
        liste_element.append(Ordinateur)
        texte=Canevas.create_text(95,125,text="PC")
        liste_label.append(texte)

def Deplacement(event):
        global x,y
        x=event.x
        y=event.y
        if x<=800 and y<=500 and x>=0 and y>=0:
                outils=Canevas.find_closest(x,y)
                Element=outils
                try:
                        texte=outils[0]+1
                except IndexError:
                        texte=None
                
                try:
                        Canevas.coords(Element,x,y)
                        Canevas.coords(texte,x,y+25)
                except:
                        None
                for v in range(len(element_cable)):
                        for valeur in element_cable[v]:
                                if valeur==outils:
                                        try:
                                                x1=Canevas.coords(element_cable[v][1])[0]
                                                y1=Canevas.coords(element_cable[v][1])[1]
                                                x2=Canevas.coords(element_cable[v][2])[0]
                                                y2=Canevas.coords(element_cable[v][2])[1]
                                                Canevas.coords(element_cable[v][0],x1,y1,x2,y2)
                                        except IndexError:
                                                None

def MenuCliqueDroit(event):
        global x,y
        x=event.x
        y=event.y
        droit.tk_popup(event.x_root,event.y_root)

def EditNom():
        pop=Tk()
        pop.title("Edit Nom")
        #objetproche=Canevas.find_closest(x,y)
        texte=Label(pop,text="Nouveau Nom :")
        texte.pack(side=LEFT)
        entree=Entry(pop,bd=5)
        entree.pack()
        btn=Button(pop,text="Valider",command=lambda: EditNom2(entree))
        btn.pack(side=RIGHT)
        pop.mainloop()

def EditNom2(entree):
        objetproche=Canevas.find_closest(x,y)
        modif=entree.get()
        Canevas.itemconfigure(objetproche[0]+1, text=modif)

def UploadFile():
        image=Canevas.find_closest(x,y)
        path=askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
        img=Image.open(path)
        photo=ImageTk.PhotoImage(img)
        Canevas.itemconfigure(image, image=photo)
        Canevas.img=photo
        
        
def Suppression(event):
        global x,y
        x=event.x
        y=event.y
        suppression=Canevas.find_closest(x,y)
        for v in range(len(element_cable)):
                for cable in element_cable[v]:
                        if cable==suppression:
                                Canevas.delete(fenetre,element_cable[v][0])
        for valeurs in liste_element:
                if valeurs==suppression[0]:
                        suppr_txt=valeurs+1
                        Canevas.delete(fenetre,suppr_txt)
        Canevas.delete(fenetre,suppression)
                

menu=Menu(fenetre,tearoff = 0)
fenetre.config(menu=menu)
SousMenu=Menu(menu,tearoff = 0)
menu.add_cascade(label="Outils", menu=SousMenu)
SousMenu.add_command(label="Switch",command=SwitchSpawn)
SousMenu.add_command(label="Routeur",command=RouteurSpawn)
SousMenu.add_command(label="Ordinateur",command=OrdinateurSpawn)
Quitter=Menu(menu,tearoff = 0)
menu.add_cascade(label="Quitter",menu=Quitter)
Quitter.add_command(label="Exit",command=Close)

droit=Menu(fenetre,tearoff = 0)
droit.add_command(label="Modifier Nom",command=EditNom)
droit.add_command(label="Modifier Icône",command=UploadFile)

Canevas.bind('<B1-Motion>',Deplacement)
Canevas.bind("<Button-2>",CableSpawn) #Clique molette
Canevas.bind('<Double-Button-1>',Suppression)
Canevas.bind("<Button-3>",MenuCliqueDroit)
fenetre.bind("<c>",OrdinateurSpawn)
fenetre.bind("<s>",SwitchSpawn)
fenetre.bind("<r>",RouteurSpawn)
fenetre.mainloop()