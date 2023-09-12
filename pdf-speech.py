from flask_cors import cross_origin
from flask import Flask, render_template, request
import pyttsx3
import PyPDF2 

def text_to_speech(book, gender):  
    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.8)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)

    pdf_reader = PyPDF2.PdfReader(book)
    pages = len(pdf_reader.pages)

    pdf_text = ""

    for num in range(0, pages):
        page = pdf_reader.pages[num]
        pdf_text += page.extract_text()  
        
    engine.say(pdf_text)
    engine.runAndWait()

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def homepage():
    if request.method == 'POST':
        book = request.form['pdf']
        gender = request.form['voices']
        text_to_speech(book, gender) 
        return render_template('pdf-speech.html')
    else:
        return render_template('pdf-speech.html')

if __name__ == "__main__":
    app.run(debug=True)
