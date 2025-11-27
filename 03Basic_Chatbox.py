import nltk
import spacy
import random
import re

nlp = spacy.load("en_core_web_sm")

responses = {
    "greeting": ["Hello!", "Hi there!", "Greetings!", "How can I help you today?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!", "Have a nice day!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "how are you": ["good, what about you?","fine","better as always","doing great"],
    "fine":["glad to hear","great","amazing"],
    "default": ["I'm not sure I understand. Can you rephrase that?"]
}

def get_response(user_input):
   
    user_input = user_input.lower()
    
    if re.search(r'\bhello\b|\bhi\b|\bgreetings\b', user_input):
        return random.choice(responses["greeting"])
    
    elif re.search(r'\bbye\b|\bgoodbye\b|\bsee you\b', user_input):
        return random.choice(responses["goodbye"])
    
    elif re.search(r'\bthanks\b|\bthank you\b', user_input):
        return random.choice(responses["thanks"])
    
    elif re.search(r'\bhow are you\b|\bhow you doing\b|\bwhats up\b', user_input):
        return random.choice(responses["how are you"])
    
    elif re.search(r'\bfine\b|\bgood\bdoing great\b', user_input):
        return random.choice(responses["fine"])
    
    else:
        doc = nlp(user_input)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        
        if entities:
            entity_response = f"I see you mentioned: {', '.join([f'{text} ({label})' for text, label in entities])}."
            return entity_response + " " + random.choice(responses["default"])
        
        return random.choice(responses["default"])

def chat():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
