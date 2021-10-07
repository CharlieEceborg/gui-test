 ## make pip3 install guizero in the cmd
from guizero import App, Text, TextBox, PushButton, Slider, Picture, Combo 
import os


kp = 2

def buttonPDix   ():
    global kp
    kp += 10
    affiche()
def buttonPUni   ():
    global kp
    kp += 1
    affiche()
def buttonPdix   ():
    global kp
    kp += 0.1
    affiche()
def buttonPcent  ():
    global kp
    kp += 0.01
    affiche()
def buttonPmille ():
    global kp
    kp += 0.001
    affiche()

def buttonMDix   ():
    global kp
    kp -= 10
    affiche()
def buttonMUni   ():
    global kp
    kp -= 1
    affiche()
def buttonMdix   ():
    global kp
    kp -= 0.1
    affiche()
def buttonMcent  ():
    global kp
    kp -= 0.01
    affiche()
def buttonMmille ():
    global kp
    kp -= 0.001
    affiche()



def affiche() :
    global kp

    dixaine  = int(kp/10)   % 10
    unite    = int(kp/1)    % 10
    dixieme  = int(kp*10)   % 10
    centieme = int(kp*100)  % 10
    milieme  = int(kp*1000) % 10
 
    KPT       = Text(app,text = "Kp distance = ", grid = [0,1] ,size=40, font="Times New Roman", color="blue")
    dixaineT  = Text(app,text =  str(dixaine)   , grid = [1,1] ,size=40, font="Times New Roman", color="blue")
    uniteT    = Text(app,text =  str(unite)     , grid = [2,1] ,size=40, font="Times New Roman", color="blue")
    virgule   = Text(app,text = "."             , grid = [3,1] ,size=40, font="Times New Roman", color="blue")
    dixiemeT  = Text(app,text =  str(dixieme)   , grid = [4,1] ,size=40, font="Times New Roman", color="blue")
    centiemeT = Text(app,text =  str(centieme)  , grid = [5,1] ,size=40, font="Times New Roman", color="blue")
    miliemeT  = Text(app,text =  str(milieme)   , grid = [6,1] ,size=40, font="Times New Roman", color="blue")

#    welcome_message = Text(app, text=str(round(kp,3)) , grid=[0,1,4,1])
    print( round(kp,3))





print('Start')
app = App(layout="grid", width = 1000, height = 500)#, layout="grid"

#film_choice = Combo(app, options=["Star Wars", "Frozen", "Lion King"],grid=[100,100],align ="left")
#update_text = PushButton(app, grid=[10,0] ,text="Say my name")

affiche()

espace        = Text(app,text = " " , grid = [0,0])
buttonPDix    = PushButton(app,command = buttonPDix  ,image = "FlecheHaut.png"  , grid=[1,0])
buttonPUni    = PushButton(app,command = buttonPUni  ,image = "FlecheHaut.png"  , grid=[2,0])
espace        = Text(app,text = " " , grid = [3,0])
buttonPdix    = PushButton(app,command = buttonPdix  ,image = "FlecheHaut.png"  , grid=[4,0])
buttonPcent   = PushButton(app,command = buttonPcent ,image = "FlecheHaut.png"  , grid=[5,0])
buttonPmille  = PushButton(app,command = buttonPmille,image = "FlecheHaut.png"  , grid=[6,0])


espace        = Text(app,text = " " , grid = [0,2])
buttonMDix    = PushButton(app,command = buttonMDix  , image = "FlecheBas.png" , grid=[1,2])
buttonMUni    = PushButton(app,command = buttonMUni  , image = "FlecheBas.png" , grid=[2,2])
espace        = Text(app,text = " " , grid = [3,2])
buttonMdix    = PushButton(app,command = buttonMdix  , image = "FlecheBas.png" , grid=[4,2])
buttonMcent   = PushButton(app,command = buttonMcent , image = "FlecheBas.png" , grid=[5,2])
buttonMmille  = PushButton(app,command = buttonMmille, image = "FlecheBas.png" , grid=[6,2])




app.display()
print ('End')


"""

def buttonPUni 
def buttonPdix  
def buttonPcent   
def buttonPmille  


def buttonPDix 
def buttonPUni 
def buttonPdix  
def buttonPcent  
def buttonPmille  

def say_my_name():
    welcome_message.value = my_name.value
    print(my_name)

def change_text_size(slider_value):
    welcome_message.size = slider_value

app = App(title="Hello world")
welcome_message = Text(app, text="Welcome to my app")
welcome_message = Text(app, text="Welcome to my app", size=40, font="Times New Roman", color="red")
my_name = TextBox(app, width = 40)
update_text = PushButton(app, command=say_my_name, text="Say my name")
text_size = Slider(app, command=change_text_size, start=10, end=80)
my_cat = Picture(app, image="CharlieTete.png")
app.display()

print(my_name)
"""
