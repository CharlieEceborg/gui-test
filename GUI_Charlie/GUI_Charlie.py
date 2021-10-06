import os ## make pip3 install guizero in the cmd
from guizero import App, Text, TextBox, PushButton, Slider, Picture, Combo 
import os


kp = 2

def affiche() :
    global kp
    welcome_message = Text(app, text=str(round(kp,3)) , grid=[0,1,4,1])
    print( round(kp,3))

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





print('Start')
app = App(layout="grid")#, layout="grid"

#film_choice = Combo(app, options=["Star Wars", "Frozen", "Lion King"],grid=[100,100],align ="left")
#update_text = PushButton(app, grid=[10,0] ,text="Say my name")



buttonPDix    = PushButton(app,command = buttonPDix  , text="PDix"  , grid=[0,0])
buttonPUni    = PushButton(app,command = buttonPUni  , text="PUni"  , grid=[1,0])
buttonPdix    = PushButton(app,command = buttonPdix  , text="Pdix"  , grid=[2,0])
buttonPcent   = PushButton(app,command = buttonPcent , text="Pcent" , grid=[3,0])
buttonPmille  = PushButton(app,command = buttonPmille, text="Pmille", grid=[4,0])

buttonMDix    = PushButton(app,command = buttonMDix  , text="MDix"  , grid=[0,2])
buttonMUni    = PushButton(app,command = buttonMUni  , text="MUni"  , grid=[1,2])
buttonMdix    = PushButton(app,command = buttonMdix  , text="Mdix"  , grid=[2,2])
buttonMcent   = PushButton(app,command = buttonMcent , text="Mcent" , grid=[3,2])
buttonMmille  = PushButton(app,command = buttonMmille, text="Mmille", grid=[4,2])


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
