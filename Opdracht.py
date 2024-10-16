import re 
import random

# Dictionary voor patronen.
patterns = { 
   "Weet je nog (.*)":"Natuurlijk weet nog {}", 
   "Ik voel (.*)":"Waarom voel jij je {}?" 

}

# Dictionary voor veelvoorkomende berichten.
responses = {
  "Hallo": ["Hoi, hoe gaat het?", "Hallo!"],
  "Het gaat goed": ["Goed om te horen!", "Geweldig!"]

}

def get_response(message):
  for pattern in patterns: 
     match = re.search(pattern,message) 
     if match:
        print("Match found!") 
        print("USER: " + match.group(0))

  if message in responses: 
    return random.choice(responses[message]) 
  else:
    return "Ik begrijp je niet."

while True:
  message = input("YOU: ")
  response = get_response(message)
  print("Bot: " + response)