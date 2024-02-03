
# string slicing
text = 'Remarkable bird, the Norwegian Blue'
print(text[11:14])
print(text[-7:-1])
print(text[:14])
print(text[-7:])

reputation = """But I got smarter, I got harder in the nick of time
Honey, I rose up from the dead, I do it all the time
I've got a list of names and yours is in red, underlined
I check it once, then I check it twice, oh!"""
print(reputation.find('I do it all'))
print(f"Taylor: {reputation[19:32]} {reputation[84:104]} {reputation[-10:]}")
print(f"Taylor {reputation[0:100:10]}")

text = "Now that's what i call a dead parrot"
print(text[5:15:2])


name = 'Katy'
print(name[::-1].upper())
# string.format / f strings

# split and join
line = 'root::0:0:superuser:/root:/bin/sh'
elems = line.split(':')

elems[0] = 'avatar'
elems[4] = 'The super-user (zero)'
line = ':'.join(elems)
print(line)

sentence = """It begins, as most things begin, with a song. 
In the beginning, after all, were the words, and they came with a tune. That was how the world was made, how the void was divided, how the lands and the stars and the dreams and the little gods and the animals, how all of them came into the world.
They were sung."""

word_count = sentence.split()
print(word_count)
print(len(word_count))
print(word_count[0:9])

# literal string interpolation
# list
names = ['Tom', 'Harry', 'Jane', 'Mary']
suffix = ['st', 'nd', 'rd', 'th']
n = 1
s = f"{str(n+1) + suffix[n]} of {len(names)} is {names[n]}"
print(s)

food = ['Pizza', 'Doughnuts', 'Salad', 'Fruit']
description = ['tasty', 'delicious', 'horrible', 'full']

print(f"I chose {food[0].lower()} out of {len(food)} choices because it was {description[1]}. It left me {description[3].upper()}.")

# join first part is deliminator and the next one is the iterable
print(' great\n'.join(food))

sentence = ', '.join(food)
print(f"I ate {sentence}")

# string formatting

albums = { 'Debut': 2006,
                 'Fearless': 2008,
                 'Speak now': 2010,
                 'Red': 2012,
                 '1989': 2014,
                 'Reputation': 2017,
                 'Lover':2019
}

for index, key in enumerate(albums.keys(),1):
    print(f"{index:5d} {key.upper():>12s} {albums[key]:5d}")