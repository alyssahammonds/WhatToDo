import tkinter as tk


root = tk.Tk()
apps = []
root.title("grid() method")
root.geometry("390x844")
#da frame on topa canvas
frame = tk.Frame(root, bg="white")
frame.place(relwidth=390,relheight=844)
Word =[['Adventurous', 'Creative', 'Artistic', "Curious", "Abstract"],
    ["Self-Disciplined", "Organized", "Plan-Driven", "Aware", "Detail Focused"],
    ["Energetic", "Center of Attention", "Assertive", "Impulsive", "Sociable"],
    ["Empathetic", "Trusting", "Honest", "Helping", "Put others first"],
    ["Stress Easy", "Moody", "Worrisome", "Emotionally Unstable", "Irritable"]]

for w in range(len(Word)):
    for a in range(len(Word)):
        button1 = tk.Button(root, text=Word[w][a],height =5,width=5,bd=6,padx=18.50,pady=18.50)
        button1.grid(row=w,column=a)



root.mainloop()

