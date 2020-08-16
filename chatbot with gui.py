#Description : This is a python program GUI for a chatbot

#library
from tkinter import *
import csv
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import simpledialog

#Define the bot's name and create an object
bot = ChatBot('bot')

#Creating a tkinter object(this represent parent window)
root = Tk()

#give the window a title
root.title('chat bot')

#give the window some dimension
root.geometry('400x500')

#create a menu bar
menu = Menu(root)

#add a scroll bar
scrollbar = Scrollbar(root)
scrollbar.place(x=375, y=5, height = 385)

#create a chat window
chatWindow = Text(root, bd=1, width = 50, height = 8,yscrollcommand = scrollbar.set)
chatWindow.place(x = 6, y = 6, height = 385, width = 370)


#create the message window
messageWindow = Text(root, bd = 1, width = 30, height = 4)
messageWindow.place(x = 128, y = 400, height = 88, width = 260)

scrollbar.config(command = chatWindow.yview)

def onclick():
    message=messageWindow.get('1.0', 'end')
    messageWindow.delete('1.0', 'end')
    if(message=='Bye\n' or message=='bye\n'):
        you = 'you : ' + str(message)
        chatWindow.insert(INSERT, you)
        reply=str(bot.name) + ' : ' + str(bot.get_response(message)) + '\n'
        chatWindow.insert(INSERT, reply)
        #root.after(3000)
        #root.destroy()
    else:
        you = 'you : ' + str(message)
        chatWindow.insert(INSERT, you)
        reply=str(bot.name) + ' : ' + str(bot.get_response(message)) + '\n'
        chatWindow.insert(INSERT, reply)

#create the button to send the message
Button = Button(root, text = 'Enter', activebackground = 'yellow', width = 12, height = 5, command = onclick)
Button.place(x =6, y =400, height = 88, width =120)

#defining all the functions

#defining save function which will save the all the chats in a file
def save():
    text = chatWindow.get('1.0', 'end')
    name = simpledialog.askstring('file name','enter the file name')
    file = open(name, 'w')
    file.write(text)
    file.close()

#defining open function which will open the previously stored chats
def open_file():
    name = simpledialog.askstring('file name','enter the file name')
    file = open(name, 'r')
    text = file.read()
    chatWindow.delete('1.0','end')
    chatWindow.insert(INSERT, text)
    file.close()
    
#defining a function to change the bot name
def change_botname():
    name = simpledialog.askstring('Bot Name','enter the new bot name')
    bot.name = name
    
#defining function to change to dark theme
def dark():
    chatWindow.config(bg = 'black', fg = 'lightgreen', insertbackground = 'lightgreen')
    messageWindow.config(bg = 'black', fg = 'lightgreen',insertbackground = 'lightgreen')
    Button.config(bg = 'black',fg = 'lightgreen')
    
#defining function to change to light theme
def light():
    chatWindow.config(bg = 'white', fg = 'black',insertbackground = 'black')
    messageWindow.config(bg = 'white', fg = 'black',insertbackground = 'black')
    Button.config(bg = 'white',fg = 'black')
    
#defining function to change the font to Times
def change_font(name):
    chatWindow.config(font = (name,13))
    messageWindow.config(font = (name,13))
    Button.config(font = (name,13))
    
#definingi function to clear chat
def clear_chat():
    chatWindow.delete('1.0','end')
    

#creating file menu
file_menu = Menu(menu)
menu.add_cascade(label = 'file', menu = file_menu)
file_menu.add_command(label = 'save', command = save)
file_menu.add_separator()
file_menu.add_command(label = 'open', command = open_file)
file_menu.add_separator()
file_menu.add_command(label = 'quit' , command = root.destroy)

#creating option menu
edit_menu = Menu(menu)
menu.add_cascade(label = 'option', menu = edit_menu)

edit_menu.add_command(label = 'clear chat', command = clear_chat)

#creating theme menu
theme_menu = Menu(edit_menu)
edit_menu.add_cascade(label = 'theme', menu = theme_menu)

theme_menu.add_command(label = 'dark', command = dark)
theme_menu.add_separator()
theme_menu.add_command(label = 'light', command = light)


edit_menu.add_separator()

#creating theme menu
font_menu = Menu(edit_menu)
edit_menu.add_cascade(label = 'font', menu = font_menu)

font_menu.add_command(label = 'Times', command = lambda : change_font('Times'))
font_menu.add_separator()
font_menu.add_command(label = 'Courier', command = lambda : change_font('Courier'))
font_menu.add_separator()
font_menu.add_command(label = 'Helvetica', command = lambda : change_font('Helvetica'))
font_menu.add_separator()
font_menu.add_command(label = 'normal', command = lambda : change_font('corbel'))

edit_menu.add_separator()

edit_menu.add_command(label = 'bot name', command = change_botname)

root.config(menu = menu)


#Define the trainer (set)
bot.set_trainer(ChatterBotCorpusTrainer)
#Import data
#Train the algorithm on this data
#Data: chatterbot/corpus/english
#.yml files for training
bot.train('chatterbot.corpus.english')
#Code for interaction with ChatBot

root.mainloop()

