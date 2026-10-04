import random

# List of silly words
silly_words = ['Banana', 'Noodle', 'Bloop', 'Soggy Waffle']
silly = random.choice(silly_words)

print('Welcome to Mad Libs')
user_choice = input('Select a template [1-3]: ')
print(f'You chose {user_choice}')

if user_choice == '1':
  number = input('Type a Number: ')
  time = input('Type a Measure of time: ')
  transport = input('Type a Mode of transportation:')
  adjective = input('Type an adjective: ')
  adjective2 = input('Type another adjective: ')
  noun = input('Type a noun: ')
  color = input('Type a color: ')
  part_body = input('Type a part of body: ')
  verb = input('Type a verb: ')
  number_2 = input('Type another number: ')
  noun2 = input('Type another noun: ')
  noun3 = input('Type another noun: ')
  part_body_2 = input('Type another part of body: ')
  noun_4 = input('Type another noun: ')
  adjective_3 = input('Type another adjective: ')

  # 1st story
  story = (
    f"""
    It was about {number} {time} ago when I arrived at the hospital in a {transport}.
    The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here.There are nurses here who have {color} {part_body}.
    If someone wants to come into my room I told them that they have to {verb} first.I've decorated my room with {number_2} {noun2}.
    Today I talked to a doctor and they were wearing a {noun3} on their {part_body_2}. I heard that all doctors {verb} {noun_4} every day for breakfast.
    The most {adjective_3} thing about being in the hospital is the {silly} {noun}!""")
  
  print(f'Here is your story:\n{story}')


elif user_choice == '2':

  name = input('Type a person\'s name: ')
  noun = input('Type a noun: ')
  adjective = input('Type an adjective(feeling): ')
  verb = input('Type a verb: ')
  adjective_2 = input('Type another adjective(feeling): ')
  animal = input('Type an animal: ')
  verb_2 = input('Type another verb: ')
  color = input('Type a color: ')
  adverb = input('Type an adverb (anding in ly): ')
  number = input('Type a number: ')
  time = input('Type a measure of time: ')
  noun2 = input('Type anpther noun: ')

  # 2nd story
  story = f"""
  This weekend I am going camping with {name.title()}. I packed my lantern,sleeping bag,
  and {noun}. I am so {adjective} to {verb} in a tent. I am {adjective_2} we might see a/an {animal}.
  I hear they're kind of dangerous. While we're camping, we are going to hike, fish, and {verb_2}.
  I have heard that the {color} lake is great for {verb}ing. Then we will {adverb} hike through the forest for {number} {time}.
  If I see a {color} {animal} while hiking, I am going to bring it home as a pet!
  At night we will tell {number} {silly} stories and roast {noun2} around the campfire!!"""
  print(f'Here is your story:\n{story}')

else:
 
  name = input('Type a person name: ')
  adjective = input('Type an adjective: ')
  color = input('Type a color: ')
  animal = input('Type an animal: ')
  place = input('Type a place: ')
  adjective2 = input('Type another adjective: ')
  magical_creature = input('Type a Magical creature (plural): ')
  adjective3 = input('Type another adjective: ')
  magical_creature2 = input('Type another Magical creature (plural): ')
  room = input('Type a room in a house: ')
  noun = input('Type a noun: ')
  noun2 = input('Type another noun: ')
  noun3 = input('Type another noun (plural): ')
  adjective4 = input('Type another adjective: ')
  noun4 = input('Type another noun (plural): ')
  number = input('Type a number: ')
  time = input('Type a measure of time: ')
  verb = input('Type a verb: ')
  adjective5 = input('Type another adjective: ')
  noun5 = input('Type another noun: ')
   
  #  3rd story
  story = f"""
  Dear {name.title()}, I am writing to you from a {adjective} castle in an enchanted forest.
  I found myself here one day after going for a ride on a {color} {animal} in {place.title()}
  There are {adjective2} {magical_creature.title()} and {adjective3} {magical_creature2.title()} here!
  In the {room} there is a pool full of {noun}. I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}.
  It feels as though I have lived here for {number} {time}.
  I hope one day you can visit,although the only way to get here now is {verb}ing on a {adjective5} {noun5}!!"""
  print(f'Here is you story:\n{story}')

