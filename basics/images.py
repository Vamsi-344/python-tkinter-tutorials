#Images
import tkinter
# from PIL import ImageTk, Image //--->For jpeg files use ImageTk.PhotoImage(Image.open('jpg-file))

# Define Window
root = tkinter.Tk()
root.title('Image Basics!')
img = tkinter.PhotoImage(file='icons/images.png')
root.iconphoto(False, img)
root.geometry('512x512')
root.resizable(0,0)

# Define Functions

# Basics...works for png
my_img = tkinter.PhotoImage(file='icons/python64.png')
my_label = tkinter.Label(root, image=my_img)
my_label.pack()

my_button = tkinter.Button(root, image=my_img)
my_button.pack()

# Define Frames



# Run root window's main loop
root.mainloop()