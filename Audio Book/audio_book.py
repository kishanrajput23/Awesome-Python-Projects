import PyPDF2
import pyttsx3

pdfReader = PyPDF2.PdfFileReader(open("C:\\Users\\KISHAN\\Downloads\\New folder\\An Introductiom To AI.pdf", 'rb'))

speaker = pyttsx3.init()

for num_page in range(pdfReader.numPages):
    text = pdfReader.getPage(num_page).extractText()
    speaker.say(text)
    speaker.runAndWait()

speaker.stop()
