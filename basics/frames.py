# Frames
import tkinter

# Define Window
root = tkinter.Tk()
root.title('Frame Basics!')
img = tkinter.PhotoImage(file='icons/frames.png')
root.iconphoto(False, img)
root.geometry('512x512')

# Define frames
pack_frame = tkinter.Frame(root, bg='#f3f3f3')
grid_frame_1 = tkinter.Frame(root, bg='blue')
grid_frame_2 = tkinter.LabelFrame(root, text='Grid System rules!', borderwidth=5)

# Pack frames onto root
pack_frame.pack(fill=tkinter.BOTH, expand=True)
grid_frame_1.pack(fill='x', expand=True)
grid_frame_2.pack(fill=tkinter.BOTH, expand=True)

# Pack frame
tkinter.Label(pack_frame, text='text').pack()
tkinter.Label(pack_frame, text='text').pack()
tkinter.Label(pack_frame, text='text').pack()

# Grid 1 Layout
tkinter.Label(grid_frame_1, text='text').grid(row=0, column=0)
tkinter.Label(grid_frame_1, text='text').grid(row=1, column=1)
tkinter.Label(grid_frame_1, text='text').grid(row=2, column=2)
#tkinter.Label(grid_frame_1, text='aaaaaaaaaaaaaaaaaa').grid(row=3, column=0)

# Grid 2 Layout
tkinter.Label(grid_frame_2, text='aaaaaaaaaaaaaaaaaa').grid(row=0, column=0)

# Run root windows main loop
root.mainloop()