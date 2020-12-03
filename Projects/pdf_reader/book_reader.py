import pyttsx3
import PyPDF2
book = open("pythonforeverybody.pdf","rb")
pdf = PyPDF2.PdfFileReader(book)
pages=pdf.numPages
print("Total number of pager in your book is",pages)
speaker = pyttsx3.init()
page = pdf.getPage(int(input("enter the number of the page you want to read:")))
text = page.extractText()
# print(text)

speaker.say(text)
speaker.runAndWait()

