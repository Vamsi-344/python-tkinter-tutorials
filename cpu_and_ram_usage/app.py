import time
import psutil
import tkinter
from PIL import ImageTk, Image

root = tkinter.Tk()
root.title('CPU & RAM Usage Monitor')
img = ImageTk.PhotoImage(Image.open('icons/cpu_hardware.png'))
root.iconphoto(False, img)
root.geometry('512x74')
root.resizable(0,0)

quitter = False
def quitting():
    global quitter #Tkinter works better as a class so this is a workaround
    quitter = True
    # add any code needed to exit the application here
    if quitter == True:
        exit(0)

root.protocol("WM_DELETE_WINDOW", quitting)

def display_usage(cpu_usage, mem_usage, bars=50):
    global cpu_cl
    global ram_cl
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = "█"*int(cpu_percent*bars)+'-'*(bars-int(cpu_percent*bars))

    mem_percent = (mem_usage / 100.0)
    mem_bar = "█"*int(mem_percent*bars)+'-'*(bars-int(mem_percent*bars))

    cpu_cl = tkinter.Label(root, text=f"\rCPU Usage: |{cpu_bar}| {cpu_usage: .2f}%  ")
    ram_cl = tkinter.Label(root, text=f"MEM Usage: |{mem_bar}| {mem_usage: .2f}%  \r")

    cpu_cl.pack(anchor="w")
    ram_cl.pack(anchor="w")

def update_cpu_usage(cpu_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = "█"*int(cpu_percent*bars)+'-'*(bars-int(cpu_percent*bars))
    return f"\rCPU Usage: |{cpu_bar}| {cpu_usage: .2f}%  "

def update_ram_usage(mem_usage, bars=50):
    mem_percent = (mem_usage / 100.0)
    mem_bar = "█"*int(mem_percent*bars)+'-'*(bars-int(mem_percent*bars))
    return f"MEM Usage: |{mem_bar}| {mem_usage: .2f}%  \r"

display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)

while True:
    if not quitter:
        root.update()
        root.update_idletasks()
        cpu_cl.configure(text=update_cpu_usage(psutil.cpu_percent(), 30))
        ram_cl.configure(text=update_ram_usage(psutil.virtual_memory().percent, 30))
        time.sleep(0.5)
    else:
        quitting()