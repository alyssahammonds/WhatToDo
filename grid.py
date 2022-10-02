import tkinter as tk
from tkinter import *
from tkinter import ttk


root = tk.Tk()
list = []
root.title("grid() method")
root.geometry("390x844") 
#da frame on topa canvas
frame = tk.Frame(root, bg="white")
frame.place(relwidth=390,relheight=844)

#the text on buttons
Word =[['Adventurous', 'Creative', 'Artistic', "Curious", "Abstract"],
    ["Self-Disciplined", "Organized", "Plan-Driven", "Aware", "Detail Focused"],
    ["Energetic", "Center of Attention", "Assertive", "Impulsive", "Sociable"],
    ["Empathetic", "Trusting", "Honest", "Helping", "Put others first"],
    ["Stress Easy", "Moody", "Worrisome", "Emotionally Unstable", "Irritable"]]

def getchar(w,a,Word):
    list.append(Word[w][a])



buttonList = []

#making 1 button per element in Word     
for w in range(len(Word)):
    #print(w)
    for a in range(len(Word)):
        #print(a)
        button1 = tk.Button(root,height =4,width=5,bd=6,padx=18.50,pady=18.50)
        button1.grid(row=w,column=a)
        buttonList.append(button1)
        button1.config(text=Word[w][a], justify =LEFT) #trying to put the word on the button into list[]
root.mainloop()

for x in range(len(buttonList)):
    print(type(buttonList[x]))

