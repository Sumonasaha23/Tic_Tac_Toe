import tkinter as tk

def BoxSet(row,column):
      global default_player
      #for stopping if the winner is declared
      if(game_over): 
            return
      # stop overwritting
      if board[row][column]["text"]!="": 
            return 

      board[row][column]["text"]=default_player
      if default_player==playerX:
            default_player=playerO
      else:
            default_player=playerX
      
      lable["text"]= default_player+"'s turn"
      winner()

def winner():
      global turns, game_over
      turns+=1
      #checking winner horizontally
      for row in range(3):
           if (board[row][0]["text"]==board[row][1]["text"]==board[row][2]["text"] and board[row][0]["text"]!=""):
                  lable.config(text=board[row][0]["text"]+" is Winner!", foreground=color_yellow)
                  for column in range (3):
                          board[row][column].config(foreground= color_yellow, background=color_lightgray)
                  game_over = True
                  return  
      #checking winner vertically
      for column in range(3):
            if(board[0][column]["text"]==board[1][column]["text"]==board[2][column]["text"] and board[0][column]["text"]!=""):
                  lable.config(text=board[0][column]["text"]+" is Winner!",foreground=color_yellow)
                  for row in range(3): 
                         board[row][column].config(foreground= color_yellow, background=color_lightgray)
                  game_over = True
                  return 
      #chceking winner diagonally
      if(board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"]and board[0][0]["text"]!=""):
            lable.config(text=board[0][0]["text"]+" is Winner!",foreground=color_yellow)
            for i in range(3): 
                         board[i][i].config(foreground= color_yellow, background=color_lightgray)
            game_over = True
            return 
      if(board[0][2]["text"]==board[1][1]["text"]==board[2][0]["text"]and board[0][2]["text"]!=""):
            lable.config(text=board[0][2]["text"]+" is Winner!",foreground=color_yellow)
            board[0][2].config(foreground= color_yellow, background=color_lightgray)
            board[1][1].config(foreground= color_yellow, background=color_lightgray)
            board[2][0].config(foreground= color_yellow, background=color_lightgray)
            game_over = True
            return 
      #Tie
      if(turns==9):
            game_over=True
            lable.config(text="Its a Tie!",foreground="red")


def reset():
      global turns,game_over
      turns=0
      game_over=False
      lable.config(text=default_player+"'s turn",foreground="black")
      for row in range(3):
            for column in range(3):
                  board[row][column].config(text="",foreground=color_blue,background=color_gray)


playerX="X"
playerO="O"
default_player=playerX
board=[[0,0,0],[0,0,0],[0,0,0]]

color_blue="#4584b6"
color_yellow="#ffde57"
color_gray="#343434"
color_lightgray="#646464"

turns=0
game_over=False

box=tk.Tk()
box.title("Tik Tac Toe-Using Python")
box.resizable(False,False)

frame=tk.Frame(box)
lable=tk.Label(frame, text=default_player+"'s turn",font=("Consolas",20), foreground="black")
lable.grid(row=0,column=0,columnspan=3)
frame.pack()

for row in range(3):
      for column in range(3):
           board[row][column]=tk.Button(frame,text="",font=("Consolas",50,"bold"),background=color_gray,foreground=color_blue,width=4,height=1, 
                                         command=lambda row=row,column=column:BoxSet(row,column))
           board[row][column].grid(row=row+1,column=column)

button=tk.Button(frame, text="Restart",font=("Consolas",20), background=color_gray,foreground=color_lightgray,command=reset )
button.grid(row=4,column=0,columnspan=3)

#box popup in center always
box.update()
box_width=box.winfo_width()
box_height=box.winfo_height()
sc_width=box.winfo_screenwidth()
sc_height=box.winfo_screenheight()
box_x= int((sc_width/2)-(box_width/2))
box_y= int((sc_height/2)-(box_height/2))
box.geometry(f"{box_width}x{box_height}+{box_x}+{box_y}")

box.mainloop()