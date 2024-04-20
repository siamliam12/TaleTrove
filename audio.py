import PyPDF2
import pyttsx3

open_book = PyPDF2.PdfReader(open('./books/the-complete-sherlock-holmes.pdf','rb'))
speaker = pyttsx3.init()

start_page = 13

# Get list of available voices
voices = speaker.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")

for pagenumber in range(start_page-1,len(open_book.pages)):
    text = open_book.pages[pagenumber].extract_text()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()