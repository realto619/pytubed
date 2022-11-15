from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
from tkinter import ttk
import os
from tkinter.filedialog import askopenfilename  
import tkinter as tk
from tkinter import messagebox
from cv2 import dft #pip install opencv-python
import webbrowser

screen = Tk()
title = screen.title('YouTube :: PyTube Video Download')
screen.curItem = 0
canvas = Canvas(screen, width=500, height=300)
canvas.pack()

#===== DATA LISTS =============
options = []
with open('data.txt') as inFile:
    options = [line for line in inFile]

#========= WIDGETS (START) ==============
def comboclick(event):
    link_field.delete(0, tk.END)
    link_field.insert(0, "https://www.youtube.com/watch?v="+myCombo.get())
#--------------------------------------------------

myCombo = ttk.Combobox(screen, value=options, font=("Lucida Sans Unicode", 11))
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()


#========= WIDGETS (START) ==============
label = Label(screen, text=options[screen.curItem], fg='maroon',  font=("Lucida Sans Unicode", 12))
counter = Label(screen, text="/?", fg='maroon', bg='white', font=('Roboto Bk', 12, 'normal'))
curnum = Label(screen, text="?", fg='red', bg='white', font=('Roboto Bk', 12, 'bold'))
Download_path = StringVar()


#======== FUNCTIONS (START) ==========
def openExtractYTIDs():
    filepath="E:/PYAPPS/pytubed/downloads/"
    getfile="extract-youtube-ids.html"
    filename=filepath+getfile
    print('filename', filename)

    webbrowser.open("file://"+filename)

def openFile(filename):
    os.chdir("E:\\PYAPPs\\pytubed\\browser\\") #change this path to your path where your f1.py and f2.py is located
    # print("current dir "+os.getcwd())
    os.system('python '+filename) #runnning the python command on cmd to execute both windows
    

def download_file():
    get_link = link_field.get()
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()

def open_file():  
    #file = askopenfilename()
    file = "data.txt"
    os.system('"%s"' % file)

def browse():
    # set directory
    download_dir = filedialog.askdirectory(initialdir="E:\\PYAPPs\\pytubed\\downloads\\")
    Download_path.set(download_dir)

def download_video():

    url = link_field.get()
    folder = Download_path.get()
    get_video = YouTube(url)
    get_stream = get_video.streams.get_highest_resolution()
    get_stream.download(folder)

def Close():
    screen.destroy()


size = os.path.getsize('data.txt')

if size > 0:
    print ("The file is not empty")
else:
    print ("The file is empty")

def refresh():
    with open('data.txt') as inFile:
        options = [line for line in inFile]

def nextArrItem(label=label):
    try:
        option = options[screen.curItem]
        print(option)
        label["text"] = option   # updates label on each call
        screen.curItem += 1          # increments index for option text
        curnum["text"] =  screen.curItem-1
        link_field.delete(0, tk.END)
        link_field.insert(0, "https://www.youtube.com/watch?v="+option)
    except IndexError:
       #print("End of Array Reached")
       label["text"] = "End of Array"
       file = "data.txt"
       os.system('"%s"' % file)

def dwnloadNextArrItem(label=label):
    try:
        #global download_success
        option = options[screen.curItem]
        print(option)
        label["text"] = option   # updates label on each call
        screen.curItem += 1          # increments index for option text
        curnum["text"] =  screen.curItem
        link_field.delete(0, tk.END)
        link_field.insert(0, "https://www.youtube.com/watch?v="+option)
        url = link_field.get()
        folder = Download_path.get()
        get_video = YouTube(url)
        get_stream = get_video.streams.get_highest_resolution()
        get_stream.download(folder)

        #messagebox.showinfo("Your video downloaded successfully")


    except IndexError:
       #print("End of Array Reached")
       label["text"] = "End of Array"
       file = "data.txt"
       os.system('"%s"' % file)

    else:
        nextArrItem()
        #download_file()
        download_video()

def open_pytubed():
    os.system('start E:/PYAPPs/pytubed/')

def buf_count_newlines_gen(fname):
    def _make_gen(reader):
        while True:
            b = reader(2 ** 16)
            if not b: break
            yield b

    with open(fname, "rb") as f:
        count = sum(buf.count(b"\n") for buf in _make_gen(f.raw.read))

    counter["text"] = "/  "+str(count)

    print(count)
    return count    

buf_count_newlines_gen("data.txt")    
#--------- FUNCTIONS (END) ---------
#openExtractYTIDs()    

#========= WIDGETS (START) ==============
youTube_You_Label = Label(screen, text=" Py ", bg='red', fg='white', font=('Roboto Bk', 22, 'normal'))
youTube_Tube_Label = Label(screen, text=" Tube ", fg='red', bg='white', font=('Roboto Bk', 20, 'normal'))
nextButton = Button(screen, text="Next Item", command=nextArrItem, bg='red', fg='white', font=("Lucida Sans Unicode", 10, 'normal'))
dlNextButton = Button(screen, text="Download Next Item", command=dwnloadNextArrItem, bg='red', fg='white', font=("Lucida Sans Unicode", 10, 'normal'))

dataBtn = Button(screen, text ='Open data.txt',  command = open_file, bg='maroon', fg='white', font=("Lucida Sans Unicode", 10))
#ytIdExtract = Button(screen, text="Extract", command = openExtractYTIDs, bg='#1b3162', fg='white', font=("Lucida Sans Unicode", 10, 'bold'))
ytIdExtract2 = Button(screen,text="Extract", command=lambda: openFile("browser.py"), bg='#1b3162', fg='white', font=("Lucida Sans Unicode", 10, 'bold'))
pytBtn = Button(screen, text ='Open PyTuber folder',  command = open_pytubed, bg='#315ba1', fg='white', font=("Lucida Sans Unicode", 10))
close_button = Button(screen, text="Close", command=Close, bg='#1b3162', fg='white', font=("Lucida Sans Unicode", 10, 'bold'))

link_field = Entry(screen, width=40, fg='maroon', font=("Lucida Sans Unicode", 12))
link_label = Label(screen, text="Enter download link: ", font=('Lucida Sans Unicode', 12))
download_btn = Button(screen, text="Download", command=download_video, bg='red', fg='white', font=("Lucida Sans Unicode", 10, 'normal'))
# 3 new widgets for "Download_path" 
destination_label = Label(screen, text ='Save To: ', bg="#d1d2ca", fg="#315ba1")


destination_field = Entry(screen, width=40 , textvariable=Download_path)
destination_field.insert(0, "E:/PYAPPs/pytubed/downloads")
browse_but = Button(screen, text="Browse", command=browse, width=10, fg="#ffffff", bg="#315ba1")
#--------- WIDGETS (END) ---------

#======== ADD TO CANVAS (START) =========
canvas.create_window(250, 25, window=youTube_You_Label)
canvas.create_window(250, 60, window=youTube_Tube_Label)

canvas.create_window(100, 95, window=destination_label)
canvas.create_window(260, 95, window=destination_field)
canvas.create_window(390, 95, window=browse_but)
#previous widgets moved down for row inserted above
canvas.create_window(250, 125, window=link_label)
canvas.create_window(250, 155, window=link_field)
canvas.create_window(150, 190, window=myCombo)
canvas.create_window(120, 230, window=label)

canvas.create_window(200, 220, window=curnum)
canvas.create_window(225, 220, window=counter)

canvas.create_window(300, 190, window=nextButton)
canvas.create_window(390, 190, window=download_btn)

canvas.create_window(340, 225, window=dlNextButton)

canvas.create_window(100, 270, window=dataBtn)
#canvas.create_window(190, 270, window=ytIdExtract)
canvas.create_window(190, 270, window=ytIdExtract2)
canvas.create_window(300, 270, window=pytBtn)
canvas.create_window(400, 270, window=close_button)

#-------- ADD TO CANVAS (END) ------------


#=== CALL GUI ==============
screen.mainloop()


###########################################################
###---------------TO-DO LIST------------------------------
###=======================================================
###  DONE 1) Button that opens the video download location
###  DONE 2) Figure out a way to change the default download location
###  DONE 3) DONE Fix the current errors 
###  ===> Exception ignored in: <function Image.__del__ at 0x000001BEB9260160>
###  ===> Traceback (most recent call last):
###  ===>   File "C:\Python\python3.10\lib\tkinter\__init__.py", line 4047, in __del__
###  ===> TypeError: catching classes that do not inherit from BaseException is not allowed
###  DONE 4) Fix the duplicate opener issue
###  DONE 5) Create a Next button that selects the next Combobox option
###  DONE 6) Ideally, trigger that button when the Download button returns to its normal state
###  7) Trigger the Download button after you change the Combobox selection
###  8) After saving an updated "data.txt" file, reload the option array
###  KINDA 9) Create a button that clears the Combobox options after all the videos have downloaded
###  KINDA 10) Make the first Combobox item that is selected by default blank  
###  KINDA 11) Figure out how to monitor when a button is depressed and when it changes
###########################################################