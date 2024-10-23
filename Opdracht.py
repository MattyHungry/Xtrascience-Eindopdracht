import re 
import random
import json
import urllib.request

patterns = { 
   "Weet je nog (.*)":"Natuurlijk weet ik nog {}.",
   "weet je nog (.*)":"Natuurlijk weet ik nog {}.",    
   "Ik voel me (.*)":"Waarom voel jij je {}?",
   "ik voel me (.*)":"Waarom voel jij je {}?",
   "Ik wil graag (.*)": "Ik snap dat jij graag wilt{}.",
   "ik wil graag (.*)": "Ik snap dat jij graag wilt{}.",
   "Hoe lang duurt het nog totdat mijn pakketje komt (.*)": "Het duur nog ongeveer 5 dagen{}.",
   "hoe lang duurt het nog totdat mijn pakketje komt (.*)": "Ik snap dat jij graag wilt{}."

}

def get_product_fact():
  url = 'https://fakestoreapi.com/products/1'
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  
  single_products = result["data"]
  single_product = single_products[0]
  
  return single_products

def get_response(message): 
  if message in responses: 
      return "Bot: " + responses[message] 
  else: 
      return "I heard you. You said: " + message 
  
responses = {
  "Hallo": ["Hoi, hoe gaat het?", "Hallo!"],
  "Het gaat goed": ["Goed om te horen!", "Geweldig!"],
  "product" : get_product_fact()

}

def get_response(message):


  for pattern in patterns: 
    match = re.search(pattern, message) 
    if match:
      return patterns[pattern].format(match.group(1))

  if message in responses: 
    return random.choice(responses[message]) 
  else:
    return "Ik begrijp je niet."

while True:
  message = input("YOU: ")
  response = get_response(message)
  print("Bot: " + response)