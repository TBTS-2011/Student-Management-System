
import PyPDF2
import pyttsx3

# path of the PDF file
path = open('file.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(path)

from_page = pdfReader.getPage(24)

# extracting the text from the PDF
text = from_page.extractText()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
