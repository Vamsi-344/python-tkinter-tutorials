#Labels and pack
import tkinter
from tkinter import BOTH

#Define window
root = tkinter.Tk()
root.title('Label Basics!')
img = tkinter.PhotoImage(file='icons/labels.png')
root.iconphoto(False, img)
root.geometry('512x512')
root.resizable(0,0)
root.config(bg='#f3f3f3')

#Create widgets
name_label_1 = tkinter.Label(root, text='Hello, my name is John Doe!')
name_label_1.pack()

name_label_2 = tkinter.Label(root, text='Hello, my name is Steve Smith!', font=('Arial', 18, 'bold'))
name_label_2.pack()

name_label_3 = tkinter.Label(root, text='Hello, my name is Sara!', font=('Cambria', 10), bg='#ff0000')
name_label_3.pack(padx=10, pady=50)
# name_label_3 = tkinter.Label(root)
# name_label_3.config(text='Hello my name is Sara!')
# name_label_3.config(font=('Cambria', 10))
# name_label_3.config(bg='#ff0000')
# name_label_3.pack()

name_label_4 = tkinter.Label(root, text='Hello, my name is Alex!', bg='black', fg='white')
name_label_4.pack(pady=(0, 10), ipadx=50, ipady=10, anchor='w')

name_label_5 = tkinter.Label(root, text='Hello, my name is Paul!', bg='blue', fg='white')
name_label_5.pack(fill=BOTH, expand='y', padx=10, pady=10)


#Run the root window's main loop
root.mainloop()