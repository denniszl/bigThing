def makeBig(thingToMakeBig):
    if thingToMakeBig:
        bigThing = 'e' + thingToMakeBig.capitalize()
        bigString = 'The next big thing is {}.'.format(bigThing)
    else:
        bigString = 'Give me something to start with, man.'
    return bigString
