# image-text_to_speech

*******************************************************************************
## README
*******************************************************************************

TODO:<br>
1.Add more languages both ways (image scan and audio output)<br>
<br><br>
This project was intended to scan text from given image and speak it into any
desirable language.<br>
Example: Scan any image with English text in it and output is English/Hindi
audio.
<br><br><br>
*******************************************************************************
## LIBRARIES REQUIRED & SETUP
*******************************************************************************
->cv2<br>
->os<br>
->pytesseract  
->tkinter<br>
->googletrans<br>

### For Windows
Download pytesseract from <a href="https://github.com/UB-Mannheim/tesseract/wiki">HERE</a>.<br>
Make changes in LINE 11: pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
Change USER to your Windows username.

### For Linux
Comment out LINE 11: pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

<br><br>
*******************************************************************************
