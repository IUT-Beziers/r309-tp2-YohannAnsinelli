import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from tkinter import Tk
from tkinter import Frame
from tkinter.filedialog import *
from tkinter import filedialog
from PIL import Image, ImageTk



fenetre=Tk()
fenetre.title("Réseaux")
Largeur = 800
Hauteur = 500
Canevas = Canvas(fenetre, width=Largeur, height=Hauteur,bg="grey")
Canevas.pack()
switch_import = PhotoImage(file="switch.png") #IMPORT IMAGE
pc_import = PhotoImage(file="pc.png")
routeur_import = PhotoImage(file="routeur.png")
liste_element=[] #Stockage des objets
liste_label=[] #Stockage des textes
element_cable=[] #Stockage objets + cable + Menu + Index Menu
liste_temporaire=[] #Pour les traits droit
liste_menucable=[] #Stockage Menu
Element1=0
Menu_item1=0
valeurinf1=0
tour=0
x=0
y=0
x1=0
y1=0
x2=0
y2=0

def Close():
        fenetre.destroy()

def SwitchSpawn(event=None): #Fenetre pour demander le nombre de port
        pop=Tk()
        pop.title("Port Switch")
        texte=Label(pop,text="Nombre de Port(s) (1 à 4) :")
        texte.pack(side=LEFT)
        entree=Entry(pop,bd=5)
        entree.pack()
        btn=Button(pop,text="Valider",command=lambda: SwitchSpawn2(entree,pop))
        btn.pack(side=RIGHT)
        pop.mainloop()

def SwitchSpawn2(entree,pop): #Faire apparaître un switch + lui associé un Menu en fonction du choix de la fonction SwitchSpawn
        valeur=entree.get()
        valeur=int(valeur)
        if valeur==1 or valeur==2 or valeur==3 or valeur==4:
                Switch=Canevas.create_image(100, 100, image=switch_import)
                Canevas.update()
                liste_element.append(Switch)
                texte=Canevas.create_text(100,125,text="Switch")
                liste_label.append(texte)
                Switch=str(Switch)
                Menu_Switch=str(Switch+'Menu')
                Menu_Switch=Menu(fenetre,tearoff=0)
                if valeur==1:
                        Menu_Switch.add_command(label="FastEthernet 1/0",command=lambda: StatuInf(val=1))
                elif valeur==2:
                        Menu_Switch.add_command(label="FastEthernet 1/0",command=lambda: StatuInf(val=1))
                        Menu_Switch.add_command(label="FastEthernet 2/0",command=lambda: StatuInf(val=2))
                elif valeur==3:
                        Menu_Switch.add_command(label="FastEthernet 1/0",command=lambda: StatuInf(val=1))
                        Menu_Switch.add_command(label="FastEthernet 2/0",command=lambda: StatuInf(val=2))
                        Menu_Switch.add_command(label="FastEthernet 3/0",command=lambda: StatuInf(val=3))
                elif valeur==4:
                        Menu_Switch.add_command(label="FastEthernet 1/0",command=lambda: StatuInf(val=1))
                        Menu_Switch.add_command(label="FastEthernet 2/0",command=lambda: StatuInf(val=2))
                        Menu_Switch.add_command(label="FastEthernet 3/0",command=lambda: StatuInf(val=3))
                        Menu_Switch.add_command(label="FastEthernet 4/0",command=lambda: StatuInf(val=4)) 
                liste_menucable.append([int(Switch),Menu_Switch])
        else:
                tkinter.messagebox.showerror(title=None, message="Choisir une valeur entre 1 et 4")
        pop.destroy()

def StatuInf(val): #Fonction pour changer le statut d'un port en Disabled quand on clique sur un port
        outils=Canevas.find_closest(x,y)
        Menu_item=outils[0]
        Menu_item=str(Menu_item)
        Menu_item=str(Menu_item+'Menu')
        for v in range(len(liste_menucable)):
                        for valeur in liste_menucable[v]:
                                if valeur==outils[0] and val==1:
                                        liste_menucable[v][1].entryconfig(0,state=DISABLED)
                                        CableSpawn(liste_menucable[v][1],valeurinf=0)
                                elif valeur==outils[0] and val==2:
                                        liste_menucable[v][1].entryconfig(1,state=DISABLED)
                                        CableSpawn(liste_menucable[v][1],valeurinf=1)
                                elif valeur==outils[0] and val==3:
                                        liste_menucable[v][1].entryconfig(2,state=DISABLED)
                                        CableSpawn(liste_menucable[v][1],valeurinf=2)
                                elif valeur==outils[0] and val==4:
                                        liste_menucable[v][1].entryconfig(3,state=DISABLED)
                                        CableSpawn(liste_menucable[v][1],valeurinf=3)
        
        

def CableSpawn(Menu_item,valeurinf): #Tracer des traits d'un point A à un point B
        global x,y,x1,y1,x2,y2,Element1,Menu_item1,valeurinf1
        Element=Canevas.find_closest(x,y)
        if x1==0 and y1==0 and x1!=100 and y1!=100: #Stockage en mémoire du premier objet sélectionné (ces coordonnées)
                x1=int(Canevas.coords(Element)[0])
                y1=int(Canevas.coords(Element)[1])
                Element1=Element
                Menu_item1=Menu_item
                valeurinf1=valeurinf
        elif x2==0 and y2==0 and x1>0 and y1>0:
                x2=int(Canevas.coords(Element)[0])
                y2=int(Canevas.coords(Element)[1])
                Cable=Canevas.create_line(x1,y1,x2,y2,fill='black',width=2)
                element_cable.append([Cable,Element1,Element,Menu_item,valeurinf,Menu_item1,valeurinf1])
                Canevas.update()
                x1=0
                y1=0
                x2=0
                y2=0

def RouteurSpawn(event=None):  #Fenetre pour demander le nombre de port
        pop=Tk()
        pop.title("Port Routeur")
        texte=Label(pop,text="Nombre de Port(s) (1 à 4) :")
        texte.pack(side=LEFT)
        entree=Entry(pop,bd=5)
        entree.pack()
        btn=Button(pop,text="Valider",command=lambda: RouteurSpawn2(entree,pop))
        btn.pack(side=RIGHT)
        pop.mainloop()                

def RouteurSpawn2(entree,pop): #Faire apparaître un routeur + lui associé un Menu en fonction du choix de la fonction RouteurSpawn
        valeur=entree.get()
        valeur=int(valeur)
        if valeur==1 or valeur==2 or valeur==3 or valeur==4:
                Routeur=Canevas.create_image(100, 100, image=routeur_import)
                Canevas.update()
                liste_element.append(Routeur)
                texte=Canevas.create_text(100,125,text="Routeur")
                liste_label.append(texte)
                Routeur=str(Routeur)
                Menu_Routeur=str(Routeur+'Menu')
                Menu_Routeur=Menu(fenetre,tearoff=0)
                if valeur==1:
                        Menu_Routeur.add_command(label="FastEthernet 1/0",command=lambda: StatuInf(val=1))
                elif valeur==2:
                        Menu_Routeur.add_command(label="FastEthernet 1/0",command=lambda: StatuInf(val=1))
                        Menu_Routeur.add_command(label="FastEthernet 2/0",command=lambda: StatuInf(val=2))
                elif valeur==3:
                        Menu_Routeur.add_command(label="FastEthernet 1/0",command=lambda: StatuInf(val=1))
                        Menu_Routeur.add_command(label="FastEthernet 2/0",command=lambda: StatuInf(val=2))
                        Menu_Routeur.add_command(label="FastEthernet 3/0",command=lambda: StatuInf(val=3))
                elif valeur==4:
                        Menu_Routeur.add_command(label="FastEthernet 1/0",command=lambda: StatuInf(val=1))
                        Menu_Routeur.add_command(label="FastEthernet 2/0",command=lambda: StatuInf(val=2))
                        Menu_Routeur.add_command(label="FastEthernet 3/0",command=lambda: StatuInf(val=3))
                        Menu_Routeur.add_command(label="FastEthernet 4/0",command=lambda: StatuInf(val=4)) 
                liste_menucable.append([int(Routeur),Menu_Routeur])
        else:
                tkinter.messagebox.showerror(title=None, message="Choisir une valeur entre 1 et 4")
        pop.destroy()

def OrdinateurSpawn(event=None): #Faire apparaître un ordinateur
        Ordinateur=Canevas.create_image(100, 100, image=pc_import)
        Canevas.update()
        liste_element.append(Ordinateur)
        texte=Canevas.create_text(95,125,text="PC")
        liste_label.append(texte)
        Ordinateur=str(Ordinateur)
        Menu_PC=str(Ordinateur+'Menu')
        Menu_PC=Menu(fenetre,tearoff=0)
        Menu_PC.add_command(label="FastEthernet 1/0",command=lambda: StatuInf(val=1))
        liste_menucable.append([int(Ordinateur),Menu_PC])
        

def Deplacement(event): #Déplacement d'objet
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
                        Canevas.coords(Element,x,y) #Je déplace l'objet
                        Canevas.coords(texte,x,y+25) #Je déplace le texte
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
                                                Canevas.coords(element_cable[v][0],x1,y1,x2,y2) #Faire des traits dynamique qui suivent l'objet quand on le déplace
                                        except IndexError:
                                                None


def MenuCliqueDroit(event): #Fonction Menu Clique Droit
        global x,y
        x=event.x
        y=event.y
        droit.tk_popup(event.x_root,event.y_root)

def MenuCable(event):
        global x,y
        x=event.x
        y=event.y
        outils=Canevas.find_closest(x,y)
        Menu_item=outils[0]
        Menu_item=str(Menu_item)
        Menu_item=str(Menu_item+'Menu')
        for v in range(len(liste_menucable)): 
                        for valeur in liste_menucable[v]: #On va rechercher le Menu associé à l'objet qu'on a cliqué dans le stockage
                                if valeur==outils[0]:
                                        liste_menucable[v][1].tk_popup(event.x_root,event.y_root)



def Traitverthorz(event): # Fonction pour tracer des traits droit (La fonction marche à moitié)
        global x,y,x1,y1,x2,y2,Element1,liste_temporaire,tour
        x=event.x
        y=event.y
        Element=Canevas.find_closest(x,y)
        liste_temporaire.append(Element)
        for v in range(len(element_cable)):
                        for valeur in element_cable[v]:
                                if valeur==Element:
                                        try:
                                                x1=Canevas.coords(element_cable[v][1])[0]
                                                y1=Canevas.coords(element_cable[v][1])[1]
                                                x2=Canevas.coords(element_cable[v][2])[0]
                                                y2=Canevas.coords(element_cable[v][2])[1]
                                                ortho=int(x1)-int(y1)
                                                if Element==element_cable[v][1] and ortho<0:
                                                        Canevas.coords(element_cable[v][2],x2,y1)
                                                        Canevas.coords(element_cable[v][0],x1,y1,x2,y1)
                                                        x1=0
                                                        y1=0
                                                        x2=0
                                                        y2=0
                                                elif Element==element_cable[v][1] and ortho>0:
                                                        Canevas.coords(element_cable[v][2],x1,y2)
                                                        Canevas.coords(element_cable[v][0],x1,y1,x1,y2)
                                                        x1=0
                                                        y1=0
                                                        x2=0
                                                        y2=0
                                                elif Element==element_cable[v][2]:
                                                        Canevas.coords(element_cable[v][1],x1,y2)
                                                        Canevas.coords(element_cable[v][0],x1,y2,x2,y2)
                                                        x1=0
                                                        y1=0
                                                        x2=0
                                                        y2=0

                                        except IndexError:
                                                None
                                        
                                        if tour==2:
                                                liste_temporaire=[]
                                                tour=0
                                                        
                                                       


def EditNom(): #Fênetre pour pouvoir rentrer un nom
        pop=Tk()
        pop.title("Edit Nom")
        #objetproche=Canevas.find_closest(x,y)
        texte=Label(pop,text="Nouveau Nom :")
        texte.pack(side=LEFT)
        entree=Entry(pop,bd=5)
        entree.pack()
        btn=Button(pop,text="Valider",command=lambda: EditNom2(entree,pop))
        btn.pack(side=RIGHT)
        pop.mainloop()

def EditNom2(entree,pop): 
        objetproche=Canevas.find_closest(x,y)
        modif=entree.get()
        if modif!="":
                Canevas.itemconfigure(objetproche[0]+1, text=modif)  #Modification du texte de l'objet cliqué
        pop.destroy()
        

def UploadFile(): #Fonction pour modifier l'image d'un objet
        image=Canevas.find_closest(x,y)
        path=askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
        img=Image.open(path)
        photo=ImageTk.PhotoImage(img)
        Canevas.itemconfigure(image, image=photo)
        Canevas.img=photo
        
        
def Suppression(event): #Suppression des objets ainsi que la réactivation des ports quand ils ne sont plus branchés
        global x,y
        x=event.x
        y=event.y
        suppression=Canevas.find_closest(x,y)
        for v in range(len(element_cable)):
                for cable in element_cable[v]:
                        if cable==suppression:
                                Canevas.delete(fenetre,element_cable[v][0])
                                element_cable[v][3].entryconfig(element_cable[v][4],state=NORMAL)
                                element_cable[v][5].entryconfig(element_cable[v][6],state=NORMAL)
                        elif cable==suppression[0]:
                                Canevas.delete(fenetre,element_cable[v][0])
                                element_cable[v][3].entryconfig(element_cable[v][4],state=NORMAL)
                                element_cable[v][5].entryconfig(element_cable[v][6],state=NORMAL)
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
Canevas.bind('<Double-Button-1>',Suppression)
Canevas.bind("<Button-3>",MenuCliqueDroit)
Canevas.bind("<Button-2>",MenuCable)
fenetre.bind("<c>",OrdinateurSpawn)
fenetre.bind("<s>",SwitchSpawn)
fenetre.bind("<r>",RouteurSpawn)
fenetre.bind("<KeyPress-Control_L>",Traitverthorz)

var=StringVar()
var1=StringVar()
label=Label(fenetre,textvariable=var,font="Times",fg="red")
var.set("Touches :")
label.pack() 
label1=Label(fenetre,textvariable=var1,font="Times",fg="red")
var1.set("Clique Gauche maintenu sur un objet permet de le déplacer\nDouble Clique Gauche permet de supprimer l'objet le plus proche\nClique Droit permet l'ouverture d'un menu édit de l'objet le plus proche\nClique Molette ouvre le Menu des ports de l'objet le plus proche\nLa touche Contrôle permet de dessiner des traits droits\nLa touche C fait apparaître un Ordinateur\nLa touche S fait apparaître un Switch\nLa touche R fait apparaître un Routeur")      
label1.pack() 

fenetre.mainloop()