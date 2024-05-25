import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import requests
import nltk
from nltk.chat.util import Chat, reflections
import re
from flask import Flask,request,render_template, jsonify
def predict(year_num):
  response = requests.get('https://github.com/ColinJ69/Co2Awareness/raw/main/Book%202%20(1).xlsx')
  data = pd.read_excel(response.content, usecols=[0,1], engine='openpyxl')
  x = np.array(data['Year'])
  y = np.array(data['Tonnes'])
  X = x.reshape(-1,1)
  reg = LinearRegression().fit(X,y)
  year_arr =  np.array(year_num)
  return int(f'{reg.predict(year_arr.reshape(1,-1))} tonnes in {year_num}')


patterns = [#questions for chatbot to answer(ngl I probably could've added more but u get the point)
    [r'hi|hello|hey', ['Hi there, is there any question I can assist with?']],
    [r'what are the effects of raised co2 levels|why is this bad|what are the effects of this|what are the impacts of this|why does this matter', ["Carbon dioxide is a greenhouse gas which traps heat inside the atmosphere,more of these gasses would raise the Earth's temperature, raising sea levels, increasing chances of wildfires, and changing the climate of ecosystems."]],
    [r'how does this impact me', ["This is affects you because the rising carbon dioxide brings along lower air quality, unpredictable weather, and burdens many economies."]],
    [r'what can i do to reduce this|how can i help|what can i do|how can i reduce my footprint|what should i do about this', ['Try to reduce meat and dairy, eat local, reduce energy consumption, and use public transport if viable.']],
    [r'what caused this', ['This rise was mainly sparked after the industrial revolution. The burning of fossil fuels, rise in industry, and deforestation are all big reasons that led to this.']],
    [r'what happened in 2020|why did it dip in 2020|why did it dip|why did it get lower in 2020', ["Covid was the reason it dipped in 2020. People were stuck inside and not travelling around."]],
]
chatbot = Chat(patterns, reflections)
def converse(text):
  if re.search(r'\d', text) != None:
    h = [str(s) for s in text.split() if s.isdigit()]
    e = [s for s in h if len(s) == 10]
    if 0 < (int(''.join(h)) - 2022) <= 100: 
      #User can ask about the amount of co2 in a specific year and that would trigger the predict function
      return predict(int(''.join(h)))
    else:
      return "We can't predict that far"
  else:
    return chatbot.respond(text)


app = Flask(__name__, template_folder='C:\\Users\\johns\\OneDrive\\Desktop\\templates')
@app.route('/', methods=['GET', 'POST'])
def main():
  if request.method == 'POST':
    text = request.form['input']
    return jsonify({'output': converse(text)})
  
  return render_template('co2.html')
  

  
if __name__ == '__main__':
  app.run(debug=True)
