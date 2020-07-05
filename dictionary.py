zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements['earth'])
print(zodiac_elements['fire'])


zodiac_elements['energy']='Not a Zodiac element'

print(zodiac_elements['energy'])

print(zodiac_elements)


# estructura del try except en phyton. Ojo debe ser KeyError:
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

key_check='matcha'

try:
  print(caffeine_level[key_check])
except KeyError:
  print('Unknown Caffeine Level')


# el dictionary tiene una función get. Se puede definir que valor entregar cuando no existe
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id=user_ids.get('teraCoder',100000)
print(tc_id)

stack_id=user_ids.get('superStackSmash','No value')
print(stack_id)

# pop es para eliminar keys de los dictionaries. Se puede definir que sale si el key no existe
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}

health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)


# list y keys son los métodos para ver todos los keys de un dictionary
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users=user_ids.keys()

lessons=num_exercises.keys()

print(users)
print(lessons)
list(users)


# maneras de ver y utilizar los keys y los values del dictionary
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises=0

for exercise in num_exercises.values():
  print(exercise)
  total_exercises+=exercise

print (total_exercises)

print(list(num_exercises.values()))
print(list(num_exercises.keys()))


#iterar en el key y el value del dictionary
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

#occupation es el key / percentaje es el value
for occupation, percentage in pct_women_in_occupation.items():
  print("Women make up " + str(percentage) + " percent of " + occupation + "s.") 

# Ejemplo para agregar, eliminar e iterar en un dictionary

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread={}

spread['past']='Death'
tarot.pop(13)

spread['present']='The Fool'
tarot.pop(22)

spread['future']='Wheel of Fortune'
tarot.pop(10)

for time,card in spread.items():
  print('Your '+str(time)+' is the '+str(card)+ ' card.')









