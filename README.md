# ocrator: OCR-to-Speech

Scan an image with your phone and translate it into speech output of desired language.  


## TO DO
<ol>
  <li>Add camera input</li>
  <li>Add support for more output languages</li>
  <li>Real-time recognition</li>
</ol>


## Usage
Run main.py

## Troubleshoot
<code>pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'</code>  
**Windows:** Replace USER with your Windows username  
**Linux:** Comment out/delete it  

Why this happens?  
Not sure but pytesseract runtime is not recognized with default settings

## Additional tools
Download pytesseract from <a href="https://github.com/UB-Mannheim/tesseract/wiki">HERE</a>.<br>
