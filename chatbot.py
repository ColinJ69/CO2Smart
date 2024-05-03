import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')
nltk.download('wordnet')
import re
patterns = [
    [r'hi|hello|hey', ['Hi there, is there any question I can assist with?']],
    [r'what are the effects of raised co2 levels|why is this bad|what are the effects of this|what are the impacts of this|why does this matter', ["Carbon dioxide is a greenhouse gas which traps heat inside the atmosphere,more of these gasses would raise the Earth's temperature, raising sea levels, increasing chances of wildfires, and changing the climate of ecosystems."]],
    [r'how does this impact me', ["This is affects you because the rising carbon dioxide brings along lower air quality, unpredictable weather, and burdens many economies."]],
    [r'what can i do to reduce this|how can i help|what can i do|how can i reduce my footprint|what should i do about this', ['Try to reduce meat and dairy, eat local, reduce energy consumption, and use public transport if viable.']],
    [r'what caused this', ['This rise was mainly sparked after the industrial revolution. The burning of fossil fuels, rise in industry, and deforestation are all big reasons that led to this.']],
    [r'what happened in 2020|why did it dip in 2020|why did it dip|why did it get lower in 2020', ["Covid was the reason it dipped in 2020. People were stuck inside and not travelling around."]],
]
chatbot = Chat(patterns, reflections)
def converse():
  text = input('You: ')

  if re.search(r'\d', text) != -1:
    h = [str(s) for s in text.split() if s.isdigit()]
    e = [s for s in h if len(s) == 10]
    if 0 < (int(''.join(h)) - 2022) <= 100:
      print(main.predict(int(''.join(h))))
    else:
      print("We can't fufill that request")
  else:
    response = chatbot.respond(shut)
    print(f'Bot: {response}')
  
