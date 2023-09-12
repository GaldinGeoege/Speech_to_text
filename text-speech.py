
from flask_cors import cross_origin
from flask import Flask, render_template, request
import pyttsx3


def text_to_speech(text, gender):
  
    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]

    engine = pyttsx3.init()


    engine.setProperty('rate', 133)

    engine.setProperty('volume', 0.8)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)

    engine.say(text)
    engine.runAndWait()

app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
@cross_origin()
def homepage():
    if request.method == 'POST':
        text = request.form['speech']
        gender = request.form['voices']
        text_to_speech(text, gender)
        return render_template('home.html')
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)