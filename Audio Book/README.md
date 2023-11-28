# Audio Book Using Python🔥

An audiobook is a recording or voiceover of a book or other work read aloud. You can listen to audiobooks on any smartphone, tablet, computer, home speaker system, or in-car entertainment system. So, let's learn how to create an audiobook with Python.

## 📌Let’s Create an Audiobook with Python
- Python has a large collection of libraries due to the very active community which serves various purposes. Here we need to use two libraries **pyttsx3** and **PyPDF2** to create an audiobook with Python.

- Both the above libraries can be easily installed by using the pip command.
  
      pip install PyPDF2
      pip install pyttsx3
      
## 📌Reading the PDF File
PyPDF2 allows manipulation of pdf in memory. This python library is capable of tasks such as:
- extract information about the document, such as title, author, etc.
- document division by page
- merge documents per page
- cropping pages
- merge multiple pages into one page
- encrypt and decrypt PDF files
- and more.

I will use this library to split the pdf file page by page, then read the text on each page, then send the text to the next step in the process to create an audiobook with Python.

    import PyPDF2
    pdfReader = PyPDF2.PdfFileReader(open('file.pdf', 'rb'))

The pyttsx3 library is capable of converting text to speech offline. The text that we read from a pdf is then fed as an input to the text-to-speech engine:

    import pyttsx3
    speaker = pyttsx3.init()
    
Now the next step in the process is to loop the process for each page of the pdf file and stop the pyttsx3 speaker engine last:

    for page_num in range(pdfReader.numPages):
        text =  pdfReader.getPage(page_num).extractText()
        speaker.say(text)
        speaker.runAndWait()
    speaker.stop()
    
This is how we can build an audiobook with Python in a few lines of code.
