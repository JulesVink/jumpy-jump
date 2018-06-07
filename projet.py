from tkinter import*                                                                ###############################################
from tkinter.messagebox import*                                                     #Programme créé par Baptiste Vié et Jules Vink#   
from random import*                                                                 #              Année 2017/2018                #
from time import*                                                                   ###############################################
fen=Tk()
fen.geometry('1000x550+110+335')
fen.title('Jumpy jump by Jules Vink and Baptiste Vié')
menu=Tk()                                               
menu.geometry('500x300+355+0')
menu.title('Jumpy jump-Menu')
canv=Canvas(fen,width=999,height=399,bg='blue') 
canv.grid()
def question_menu(str):
    showinfo('Question piège','IL EST PAS BIEN NOTRE JEU ?')
    fen.destroy()
    menu.destroy()
def commandes(str):
    showinfo('Commandes','Vous incarnez le dernier Pacman survivant sur Pluton combattant les démoniaques formes rouges. Appuyez sur la flèche du haut pour sauver votre vie en utilisant votre jetpack')	
def game_over(str):
    global phrase
    global score
    global question
    if score<2:
        phrase='Vous avez perdu ! Vous avez survécu à ',score,' vague des démoniaques formes rouges. Voulez-vous recommencer ?'
    else:   
        phrase='Vous avez perdu ! Vous avez survécu à ',score,' vagues des démoniaques formes rouges. Voulez-vous recommencer ?'
    question=askyesno("Game over",phrase)
    if question==True:
        recommencer()
    else:
        fen.destroy()
    return
def recommencer():
    global n,objet,obstacle2,obstacle1,y1pacman,y2pacman,boucle,score,vitesse
    while not y2pacman==380:
        canv.move('Pacman',0,1)
        canv.move('Oeuil',0,1)
        canv.update()
        y2pacman+=1
    if objet==1:
        while not obstacle2>=1000:
            canv.move('obstacle1',1,0)
            canv.update()
            obstacle2+=1
    elif objet==2:
        while not obstacle2>=1000:
            canv.move('obstacle2',1,0)
            canv.update()
            obstacle2+=1
    else:
        while not obstacle2>=1000:
            canv.move('obstacle3',1,0)
            canv.update()
            obstacle2+=1
    objet=randrange(1,4)
    if objet==1:
        obstacle1=900
    elif objet==2:
        obstacle1=980
    else:
        obstacle1=940
    n=1120
    y1pacman=230
    score=0
    vitesse=1.5
    boucle_principale('!')
    return
def boucle_principale(event):
    while boucle==True:
        avancer()
        sleep(0.001)
        depart()
    return
def verifier():
    global objet
    global y1pacman
    global y2pacman
    global obstacle1
    global obstacle2
    if objet<2:
        if obstacle1<151:
            if obstacle2>19:
                if y2pacman>280:
                    game_over('!')
    elif objet==2:
        if obstacle1<151:
            if obstacle2>19:
                if y2pacman>220:
                    game_over('!')
    else:
        if obstacle1<151:
            if obstacle2>19:
                if y1pacman<220:
                    game_over('!')
    return
def sauter(event):
    global y2pacman
    global y1pacman
    global i
    if y2pacman==380:  
        for i in range(90):
            canv.move('Pacman',0,-2)
            canv.move('Oeuil',0,-2)
            canv.update()
            y2pacman-=2
            y1pacman-=2
            avancer()
            sleep(0.001)
            depart()
        for i in range(95):
            avancer()
            sleep(0.001)
            depart()
        for i in range(180):
            canv.move('Pacman',0,1)
            canv.move('Oeuil',0,1)
            canv.update()
            avancer()
            sleep(0.001)
            depart()
            y2pacman+=1
            y1pacman+=1
    return
def danger(event):
    menu.destroy()
    global obstacle1
    global obstacle2
    global objet
    objet=randrange(1,4)
    if objet==1:
        obstacle1=900
    elif objet==2:
        obstacle1=980
    else:
        obstacle1=940
    boucle_principale('!')
    return
def depart():
    global obstacle2
    global objet
    global obstacle1
    global score
    global vitesse
    if obstacle2<2:
        if objet==1:
            canv.move('obstacle1',1000,0)
        elif objet==2:
            canv.move('obstacle2',1000,0)
        else:
            canv.move('obstacle3',1000,0)
        objet=randrange(1,4)
        obstacle2=1000
        if objet==1:
            obstacle1=900
        elif objet==2:
            obstacle1=980
        else:
            obstacle1=940
        score+=1
        vitesse+=0.2
        canv.itemconfigure('marqueur_score', text=score)
        return
def avancer():
    global objet
    global obstacle1
    global obstacle2
    global vitesse
    if objet==1:
        canv.move('obstacle1',-vitesse,0)
        canv.update()
        obstacle1-=vitesse
        obstacle2-=vitesse
    elif objet==2:
        canv.move('obstacle2',-vitesse,0)
        canv.update()
        obstacle1-=vitesse
        obstacle2-=vitesse
    else:
        canv.move('obstacle3',-vitesse,0)   
        canv.update()
        obstacle1-=vitesse
        obstacle2-=vitesse
    verifier()
    return
#Variable
i=0
n=1120
objet=0
obstacle2=1000
obstacle1=0
y1pacman=230
y2pacman=380
boucle=True
score=0
phrase='resultat'
vitesse=1.5
question='question'
#Objets
f1=canv.create_arc((20,230,170,380),fill='yellow',extent=270,start=45,tag='Pacman')
f2=canv.create_oval((100,250,110,260),fill='black',tag='Oeuil')
f3=canv.create_line((1,381,1000,383),fill='black',tag='sol')
f4=canv.create_rectangle((900,280,1000,380),fill='red',tag='obstacle1')
f5=canv.create_rectangle((980,220,1000,380),fill='red',tag='obstacle2')
f6=canv.create_oval((940,160,1000,220),fill='red',tag='obstacle3')
f7=canv.create_rectangle((900,1,1000,400),fill='red',tag='bande_rouge')
f8=canv.create_text(800,20,text='Score : ',anchor='e',font=('Times', '25'),fill='white')
f9=canv.create_text(800,20,text=score,anchor='w',font=('Times', '25'),fill='white',tag='marqueur_score')
titre=Label(menu,text='Jumpy Jump',fg='red',height=2,font=('Times','25')).pack()
sous_titre=Label(menu,text='Jeu développé par Jules Vink et Baptiste Vié en ICN, 2017-2018',height=2,fg='black',font=('Times','10')).pack()
#Boutons
bouton=Button(fen, text='Fini de jouer ?', command=lambda:question_menu('!'))
bouton.grid()
bouton2=Button(fen, bitmap='info', command=lambda:commandes('!'))
bouton2.grid()
start=Button(menu, text='Commencer à jouer ?',activebackground='blue',activeforeground='white',relief='groove',height=2, command=lambda:danger('!'))
start.pack()
info=Button(menu, text='Commandes',activebackground='blue',activeforeground='white',relief='groove',height=2, command=lambda:commandes('!'))
info.pack()
sortir=Button(menu, text='Quitter',activebackground='blue',activeforeground='white',relief='groove',height=2, command=lambda:question_menu('!'))
sortir.pack()
fen.bind(sequence="<KeyPress>",func=sauter)
#Main program
fen.mainloop()
menu.mainloop()
