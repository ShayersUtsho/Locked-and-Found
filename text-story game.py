input('Hi')
input('I\'m sure you\'re wondering...')
input('What kind of game is this?')
input('What have I wondered into?')
input('Well,')
input('You\'re locked in a room.')
input('You don\'t remember what happened to you')
input('But you\'re finally awake!')
input('Look around you - ')
input('There\'s a door')
option = input('Pull it? (y/n)')
if option == 'y' or option == 'Y':
    input('you pull the doorknob,')
    input('but nothing happened.')
    input('It\'s locked from the outside.')
    input('Now what?')
input('There\'s a window')
input('You try to get up')
input('You try to look through it,')
input('But it\'s too high...')
item = list()
while True:
    input('You look around the room')
    input('There are a few things you could use')
    option = input('1. A saw\n2. Some boxes\n3. Some rope\n4. A lighter\n5. A Teddy bear\n')
    if option == '1':
        item.append('saw')
        input('You pick up the saw')
        input('But it can\'t help you look out the window')
        continue
    if option == '2':
        item.append('boxes')
        input('You pile the boxes in front of the window')
        input('Then you climb up the boxes')
        break
    if option == '3':
        item.append('rope')
        input('You tie the rope to the window bars')
        input('Then you climb up the rope')
        break
    if option == '4':
        item.append('lighter')
        break
    if option == '5':
        input('The teddy bear reminds you of your daughter')
        input('She plays with teddy bears a lot')
        input('You need to get out of here')
        input('but a teddy bear is useless for that')
        continue

if 'lighter' in item:
    # Sadat
    input('You light up the lighter')
    input('The dark room lights up')
    input('Including the corridor outside of the door')
    input('You hear some footsteps')
    input('"Hey!! Check on the captive!"')
    input('You look around -')
elif 'saw' in item:
    # Shayer S. Utsho
    input('You cut down the window bars.')
    if 'rope' in item:
        input('But the bar with the rope tied to it breaks, too')
        input('And you fall off with the rope, making some noise')
        input('You hear footsteps outside the door')
        input('You hurriedly put together the boxes')
    input('And you climb out the window.')
    if 'boxes' in item:
        item.remove('boxes')
    input('A man from what seems to be the entrance to the place sees you')
    input('And you start running')
else:
    # Apon
    input('You look outside')
    input('You see an empty street')
    input('You begin to feel despair,')
    input('But then,')
    input('You hear some footsteps')
    input('Coming towards your direction')
    input('You see an old lady walking')
    option = input('Call her for help? (y/n) ')
    if option == 'y' or option == 'Y':
        #Apon
        pass
    else:
        #Tamim
        pass























