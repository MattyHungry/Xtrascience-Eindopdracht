#werkt alleen in trinket
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
    }

def get_product_fact():
  url = 'https://fakestoreapi.com/products/1'
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  
  single_products = result["title"]
  single_product = single_products[0]
  
  return single_products

def get_response(message): 
  if message in responses: 
      return "Bot: " + responses[message] 
  else: 
      return "I heard you. You said: " + message 
  
responses = {
  "Hallo": ["Hoi, hoe gaat het?", "Hallo!"],
  "hallo": ["Hoi, hoe gaat het?", "Hallo!"],
  "Het gaat goed": ["Goed om te horen!", "Geweldig!"],
  "het gaat goed": ["Goed om te horen!", "Geweldig!"],
  "product" : [get_product_fact()],
  "Hoe lang duurt het nog totdat mijn pakketje komt": ["Het duurt nog ongeveer 5 dagen."],
  "hoe lang duurt het nog totdat mijn pakketje komt": ["Het duurt nog ongeveer 5 dagen."],
  "Wat zijn de kosten om mijn pakketje terug te sturen": ["Dat kost ongeveer €1.", "Dat kost ongeveer €2.", "Dat kost ongeveer €3.", "Dat kost ongeveer €4."],
  "wat zijn de kosten om mijn pakketje terug te sturen": ["Dat kost tussen de €5-10."],
  "Hoe komt het dat mijn pakketje vertraagt is": ["Dat komt omdat we het op dit moment druk hebben met veel bestellingen.", "Sorry, we hebben het op dit moment heel druk."],
  "hoe komt het dat mijn pakketje vertraagt is": ["Dat komt omdat we het op dit moment druk hebben met veel bestellingen.", "Sorry, we hebben het op dit moment heel druk."],
  "Is er een mogelijkheid dat ik mijn pakketje kan volgen": ["Met onze app kan je je pakketje volgen met de unieke code die je hebt ontvangen in je mail".],
  "is er een mogelijkheid dat ik mijn pakketje kan volgen": ["Met onze app kan je je pakketje volgen met de unieke code die je hebt ontvangen in je mail".],

,}

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