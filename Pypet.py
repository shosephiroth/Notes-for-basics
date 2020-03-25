print('Welcome to Pypet!')

#Created a dictionary which hosts the variables between curly brackets { }. These are the pets

kitty = {
    'name': 'Sparky',
    'age': 1,
    'weight': 4,
    'hungry': True,
    'happiness': 3
    'photo': '(=^o.o^=)__',
}

#basic print function, let's see what they look like

print('Hello ' + kitty['name'])
print(kitty['photo'])

#Another pet, let's give them a friend

mouse = {
    'name': 'Mouse',
    'age': 6,
    'weight': 1.5,
    'hungry': False,
    'photo': '<:3~~~~',
}

#Let's create a list for the pets, that way we can call them all at once if needed

pets = [kitty, mouse]

#Let's add a feed function


def feed(pet):
    if pet['hungry'] == True:
        pet['hungry'] = False
        pet['weight'] = pet['weight'] + 1
    else:
        print('Kitty is not hungry')
        print('Mouse is not hungry')

#Still working on this function below

def play(pet):
  if pet['happiness'] <= 4:
      pet['happiness'] = pet[happiness] + 1

print(happiness)


#so far I can only feed one pet at a time unless I type the function out for each

print(pets)
feed(kitty)
feed(mouse)
print(pets)

print(NameError)

#Thanks to Thinkful for this tutorial, I plan on building upon it so you may notice some differences from the original lesson

# https://www.thinkful.com/learn/intro-to-python-tutorial/#Introduction
