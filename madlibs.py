# py projects guiding
# string concatenation
# suppose we want a string that says 'subscribe to ____'

youtuber = 'Claire' # some string variable
# a few ways to do this
print('subscribe to '+ youtuber)
print('subscribe to {}'.format(youtuber))
print(f'subscribe to {youtuber}')

adj = input('Adjective: ')
verb1 = input('Verb: ')
verb2 = input('Verb: ')
famous_person = input('Famous_person')

madlib = f'Computer programming is so {adj}! It makes me so excited all the time because \n I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!'
print(madlib)
