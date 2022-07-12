# Window basics
import tkinter

# Define Window
root = tkinter.Tk()
root.title('Window Basics!')
img = tkinter.PhotoImage(file='icons/windows.png')
root.iconphoto(False, img)
root.geometry('512x256')
root.resizable(0,0)
root.config(bg="#ccc")
# root.tk.call('wm', 'iconphoto', root._w, img)
# root.iconphoto('python.ico')

#Second Window
top = tkinter.Toplevel()
top.title('Second window')
top.iconphoto(False, img)
top.config(bg="#f3f3f3")
top.geometry('256x256+500+50')

# Run root window's mainloop
root.mainloop()