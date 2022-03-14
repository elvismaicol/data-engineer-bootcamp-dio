import webbrowser
from tkinter import *

# Tk( ) => o espaço dentro no parentese é para representar a tel
root = Tk( )

root.title('Abrir Browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')


Button(root, text='Abrir o Google', command=google).pack(pady=20)

root.mainloop()
