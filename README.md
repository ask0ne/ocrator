# ocrator

Scan a image with your phone and translate it into desired language speech output.
<hr>
## TO DO
<hr>
<ol>
  <li>Add camera input</li>
  <li>Add support for more output languages</li>
</ol>
<br><br>
<br><br><br>
<hr>
## LIBRARIES REQUIRED & SETUP
<hr>

<ul>
  <li>opencv</li>
  <li>os</li>
  <li>pytesseract</li>
  <li>tkinter</li>
  <li>googletrans</li>
</ul>

### For Windows
Download pytesseract from <a href="https://github.com/UB-Mannheim/tesseract/wiki">HERE</a>.<br>
Make changes in LINE 11: pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
Change USER to your Windows username.

### For Linux
Comment out LINE 11: pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
