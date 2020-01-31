from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import cv2
import pytesseract
from gtts import gTTS
import os
import sys
from googletrans import Translator
translator = Translator()
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\kawad\AppData\Local\Tesseract-OCR\tesseract.exe'


class main(Tk):
    x=1
    file_name = ""
    def __init__(self):
        super(main, self).__init__()
        self.title("Image Text to Speech")
        self.minsize(640, 400)
        self.labelFrame = ttk.LabelFrame(self, text = "Convert image text(English) into speech of below mentioned languages")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
        self.buttons()


    def buttons(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)
        self.button2 = ttk.Button(self.labelFrame, text="Exit", command = self.close_window)
        self.button2.grid(column = 2, row = 1)
        self.button3 = ttk.Button(self.labelFrame, text="English", command = lambda :self.setx(1))
        self.button3.grid(column = 1, row = 2)
        self.button4 = ttk.Button(self.labelFrame, text="Hindi", command = lambda :self.setx(2))
        self.button4.grid(column = 2, row = 2)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =(("png files","*.png"),("jpeg files","*.jpg"),("all files","*.*")) )
        self.img_speech(self.filename)
        global file_name
        file_name = self.filename
        
        
    def setx(self, a):
        global x
        x = a
        try:
            self.img_speech(file_name)
           
          
    def img_speech(self, address):
        img = cv2.imread(address)
        text = pytesseract.image_to_string(img)
        if x==1:
            text = translator.translate(text, dest="en")        
        elif x==2:
            text = translator.translate(text, dest="hi")
        
        text = text.text
        tts = gTTS(text)
        tts.save("audio.mp3")
        os.system("start audio.mp3")


    def close_window(self):
        exec.destroy()
        

exec = main()
exec.mainloop()