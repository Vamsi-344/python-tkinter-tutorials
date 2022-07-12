# Radio buttons
import tkinter

# Define root window
root = tkinter.Tk()
root.title('Radio Button Basics!')
img = tkinter.PhotoImage(file='icons/radio.png')
root.iconphoto(False, img)
root.geometry('512x512')
root.resizable(0,0)

# Define Functions
def make_label():
    '''Print to the screen'''
    global number
    if number.get() == 1:
        num_label = tkinter.Label(output_frame, text="1 one 1")
    elif number.get()==2:
        num_label = tkinter.Label(output_frame, text="2 two 2")
    num_label.pack()

# Define Frames
input_frame = tkinter.LabelFrame(root, text='This is for radio buttons', width=512, height=125)
output_frame = tkinter.Frame(root, width=512, height=375)
input_frame.pack(padx=10, pady=10)
output_frame.pack(padx=10, pady=(0,10))

# Define Variable
number = tkinter.IntVar()

# Define Widgets
radio_1 = tkinter.Radiobutton(input_frame, text='Print the number one', variable=number, value=1)
radio_2 = tkinter.Radiobutton(input_frame, text='Print the number two', variable=number, value=2)
print_button = tkinter.Button(input_frame, text='Print the number', command=make_label)

# Define Radio Buttons
radio_1.grid(row=0, column=0, padx=10, pady=10)
radio_2.grid(row=0, column=1, padx=10, pady=10)
print_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


# Run the root window's main loop
root.mainloop()