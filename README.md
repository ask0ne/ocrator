# ocrator: OCR-to-Speech

Scan an image with your phone and translate it into speech output of desired language.  

--

## TO DO
<ol>
  <li>Add camera input</li>
  <li>Add support for more output languages</li>
  <li>Real-time recognition</li>
</ol>

--
## Usage
Run main.py

--

## Additional tools  
Windows  
Download pytesseract from <a href="https://github.com/UB-Mannheim/tesseract/wiki">HERE</a>.<br>
Make changes in LINE 11: pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
Change USER to your Windows username.  
Linux
Comment out LINE 11: pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
