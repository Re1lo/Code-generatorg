import random
import string

import pyperclip3
from customtkinter import *



def random_numbers():
    length = random.randint(1,15)
    numbers = ['1','2','3','4','5','6','7','8','9','0']

    for x in string.ascii_lowercase:
        numbers.append(x)


    code = ''.join(random.choice(numbers) for x in range(length))
    label.configure(text=code)

def copy():
    copy_Text = label.cget("text")
    pyperclip3.copy(copy_Text)
root = CTk()
root.geometry("400x400")
root.resizable(False,False)

frame = CTkFrame(root,width=300, height=350, corner_radius=4)
frame.pack()

label = CTkLabel(frame, width=100, height=60, font=("Comic Sans MC", 15, 'bold'), text="No code over there")
label.place(relx=0.5, rely=0.2, anchor=CENTER)

button = CTkButton(frame, width=110, height=40, text="Generate!", command=lambda : random_numbers())
button.place(relx=0.5, rely=0.5, anchor=CENTER)

copybutton = CTkButton(frame, width=70, height=30, text="copy", command=lambda : copy(), fg_color='transparent')
copybutton.place(relx=0.5, rely=0.3, anchor=CENTER)

root.mainloop()
