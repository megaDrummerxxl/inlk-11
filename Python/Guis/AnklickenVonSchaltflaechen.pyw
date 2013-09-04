from tkinter import *

# Ereignisbehandlung
def buttonWeiterClick():
    stand = int(labelZahl.cget('text'))
    stand = stand + 1
    labelZahl.config(text=str(stand))
    buttonZurueck.config(state = 'normal')

def buttonZurueckClick():
    stand = int(labelZahl.cget('text'))
    stand = stand - 1
    labelZahl.config(text=str(stand))
    if(stand == 0) :
        buttonZurueck.config(state = 'disabled')

def buttonNullClick():
    labelZahl.config(text="0")
    buttonZurueck.config(state = 'disabled')

# GUI-Objekte
# Fenster
tkFenster = Tk()
tkFenster.title('Zähler')
tkFenster.geometry('170x125')
# Label
labelZahl = Label(master=tkFenster, text='0', bg='gray', font=('Arial', 36))
labelZahl.place(x=5, y=5, width=160, height=80)
# Button
buttonWeiter = Button(master=tkFenster, text='weiter', bg='#D5E88F', command=buttonWeiterClick)
buttonWeiter.place(x=115, y=90, width=50, height=30)
buttonZurueck = Button(master=tkFenster, text='zurück', bg='#FFCFC9', state='disabled', command=buttonZurueckClick)
buttonZurueck.place(x=5, y=90, width=50, height=30)
buttonNull = Button(master=tkFenster, text='Null', bg='#FBD975', command=buttonNullClick)
buttonNull.place(x=60, y=90, width=50, height=30)
# Aktivierung des Fensters
tkFenster.mainloop()
