from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
  if request.method == "POST":
    text = request.files['text']
    response = chatbot.converse(text.lower())
  respond = session['response']
  return render_template('main.html', response=respond)
  
