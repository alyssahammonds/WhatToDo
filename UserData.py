import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

root_tk = customtkinter.CTk()
root_tk.geometry(f"{390}x{844}")
root_tk.title("main plain")
frame = customtkinter.CTkFrame(master=root_tk,width=390,height=844,corner_radius=10)
frame.pack(padx=20,pady=20)

Nick_Name = customtkinter.CTkEntry(master=root_tk,width=200,placeholder_text="Enter you're Name\\Nick Name",height=25,border_width=2,corner_radius=10)
Nick_Name.place(relx=.5, rely=.2, anchor = tkinter.CENTER)

Age = customtkinter.CTkEntry(master=root_tk,width=200,placeholder_text="Enter you're Age", justify = tkinter.CENTER,height=25,border_width=2,corner_radius=10)
Age.place(relx=.5, rely=.25, anchor = tkinter.CENTER)


def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox_var = customtkinter.StringVar(value="select gender")
combobox = customtkinter.CTkComboBox(master=root_tk,values=["Female","Male","Nonbinary","Decline to Answer"], command=combobox_callback, variable=combobox_var)
combobox.place(relx=.5, rely=.30,anchor = tkinter.CENTER)

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox_var = customtkinter.StringVar(value="Dietary restrictions?")
combobox = customtkinter.CTkComboBox(master=root_tk,values=["vegan","vegetarian","paleo","lactose intolerant"], width= 150 ,command=combobox_callback, variable=combobox_var)
combobox.place(relx=.5, rely=.35,anchor = tkinter.CENTER)




root_tk.mainloop()






