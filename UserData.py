from distutils.cmd import Command
from email.mime import image
import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

def userData():

    root_tk = customtkinter.CTk()
    root_tk.geometry(f"{390}x{844}")
    root_tk.title("main plain")
    frame = customtkinter.CTkFrame(master=root_tk,width=390,height=844,corner_radius=10)
    frame.pack(padx=20,pady=20)

    lis=[]
    def printValue():
        pname = Nick_Name.get()
        age = Age.get()
        lis.append(pname)
        lis.append(age)
        root_tk.destroy()

        
    Nick_Name = customtkinter.CTkEntry(master=root_tk,width=200,placeholder_text="Enter your Name\\Nick Name",height=25,border_width=2,corner_radius=10)
    Nick_Name.place(relx=.5, rely=.2, anchor = tkinter.CENTER)

    Age = customtkinter.CTkEntry(master=root_tk,width=200,placeholder_text="Enter your Age", justify = tkinter.CENTER,height=25,border_width=2,corner_radius=10)
    Age.place(relx=.5, rely=.25, anchor = tkinter.CENTER)


    def combobox_callback(choice):
        print("combobox dropdown clicked:", choice)
        lis.append(choice)

    combobox_var = customtkinter.StringVar(value="select gender")
    combobox = customtkinter.CTkComboBox(master=root_tk,values=["Female","Male","Nonbinary","Decline to Answer"], command=combobox_callback, variable=combobox_var)
    combobox.place(relx=.5, rely=.30,anchor = tkinter.CENTER)

    def combobox_callback(choice):
        print("combobox dropdown clicked:", choice)
        lis.append(choice)

    combobox_var = customtkinter.StringVar(value="Dietary restrictions?")
    combobox = customtkinter.CTkComboBox(master=root_tk,values=["vegan","vegetarian","paleo","lactose intolerant"], width= 150 ,command=combobox_callback, variable=combobox_var)
    combobox.place(relx=.5, rely=.35,anchor = tkinter.CENTER)

    label = customtkinter.CTkLabel(master=root_tk, text="Hobbies?",corner_radius=10)
    label.place(relx=0.25, rely=0.4, anchor=tkinter.CENTER)


    photo = tkinter.PhotoImage(file = "C:\\Users\\vidar\\OneDrive\\Desktop\\HackUTA\hiking.gif")
    def button_event():
        b1= "Hiking"
        lis.append(b1)
    button = customtkinter.CTkButton(master=root_tk,width=0,height=0,border_width=1,corner_radius=8,command=(button_event),image = photo,text="")
    button.place(relx=0.25, rely=0.53, anchor=tkinter.CENTER)

    photo = tkinter.PhotoImage(file = "C:\\Users\\vidar\\OneDrive\\Desktop\\HackUTA\\music.gif")
    def button_event():
        b2= "Music"
        lis.append(b2)
    button2 = customtkinter.CTkButton(master=root_tk,width=0,height=0,border_width=0,corner_radius=8,command=(button_event),image = photo,text="")
    button2.place(relx=0.75, rely=0.53, anchor=tkinter.CENTER)

    photo = tkinter.PhotoImage(file = "C:\\Users\\vidar\\OneDrive\\Desktop\\HackUTA\\movie.gif")
    def button_event():
        b3= "Movies"
        lis.append(b3)
    button3 = customtkinter.CTkButton(master=root_tk,width=0,height=0,border_width=0,corner_radius=8,command=(button_event),image = photo,text="")
    button3.place(relx=0.55, rely=0.75, anchor=tkinter.CENTER)

    submitButton = customtkinter.CTkButton(master=root_tk,width=5,height=10,border_width=0,corner_radius=8,command=printValue,text="submit")
    submitButton.place(relx=0.55, rely=0.85, anchor=tkinter.CENTER)
    root_tk.mainloop()

    return lis


print(userData())
