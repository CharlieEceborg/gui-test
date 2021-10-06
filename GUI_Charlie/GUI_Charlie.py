import os ## make pip3 install guizero in the cmd
from guizero import App, Text, TextBox, PushButton, Slider
import os

def say_my_name():
    welcome_message.value = my_name.value
    print(my_name)

def change_text_size(slider_value):
    welcome_message.size = slider_value

print('Start')
app = App(title="Hello world")
welcome_message = Text(app, text="Welcome to my app")
welcome_message = Text(app, text="Welcome to my app", size=40, font="Times New Roman", color="red")
my_name = TextBox(app, width = 40)
update_text = PushButton(app, command=say_my_name, text="Say my name")
text_size = Slider(app, command=change_text_size, start=10, end=80)
app.display()


print(my_name)
print ('End')


"""

"""
