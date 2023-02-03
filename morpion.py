
from tkinter import *
import random

def next_turn(row,column):
    global player
    
    if boutons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            boutons[row][column]['text'] = player
            
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))
                
            elif check_winner() is True:
                label.config(text=(players[0]+" gagné"))
            
            elif check_winner() == "égalité":
                label.config(text=("égalité"))
        
        else:
            boutons[row][column]['text'] = player
            
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))
                
            elif check_winner() is True:
                label.config(text=(players[1]+" gagné"))
            
            elif check_winner() == "égalité":
                label.config(text=("égalité"))
        

def check_winner():
    
   for row in range (3):
       if boutons[row][0]['text'] == boutons[row][1]['text'] == boutons[row][2]['text'] != "":
          return True
      
   for column in range (3):
        if boutons[0][column]['text'] == boutons[1][column]['text'] == boutons[2][column]['text'] != "":
            return True
        
   if boutons[0][0]['text'] == boutons[1][1]['text'] == boutons[2][2]['text'] != "":
        return True
    
   elif boutons[0][2]['text'] == boutons[1][1]['text'] == boutons[2][0]['text'] != "":
        return True
    
   elif empty_spaces() is False:
        return "égalité"
    
   else:
        return False

def empty_spaces():
    
    espaces = 9
    
    for row in range(3):
        for column in range(3):
            if boutons[row][column]['text'] != "":
                espaces -=1
            
    if espaces == 0 :
        return False
    else :
        return True 
    
    

def new_game():
    global player
    
    player = random.choice(players)
    
    label.config(text=player+" turn")
    
    for row in range(3):
        for column in range(3):
             boutons[row][column].config(text="")
    
    

fenetre =Tk()
fenetre.title("Morpions")
players=["x","o"]
player = random.choice(players)
boutons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text= player + " turn",font=('consolas',40))
label.pack(side="top")

bouton_reset= Button(text="C'est parti mon kiki", font=('consolas',20),command=new_game)
bouton_reset.pack(side="top")

cadre = Frame(fenetre)
cadre.pack() 

for row in range(3):
    for column in range(3):
        boutons[row][column] = Button(cadre, text="",font=('consolas',40), width=5, height=2,command= lambda row=row,column=column: next_turn(row,column))
        boutons[row][column].grid(row=row,column=column) 

fenetre.mainloop()
