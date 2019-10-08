# More strings and text

x = "There are %d types of people" % 10
# defined there are 10 types of people in this world
binary = "binary"
# defined it makes binary mean binary
doNot = "don't"
# defined it turns doNot into don't i guess for eas purposes
y = "Those who know %s and those who %s" % (binary, doNot)
# Defined it makes the sentence whole
print(x)
# defined it is a variable that will say the sentence as a whole
print(y)
# defined is is the variable that makes the sentence with out without having it again
print("I said %r.:" % x)
# defined it is repeating the part of the joke considered to be funny
print("I also said: '%s'." % y)
# defined The other part of the joke which comes together
hilarious = True
jokeEvaluation = "Isn't that joke so funny?! %r"
# defined this is a code that asks if it was funny
print(jokeEvaluation % hilarious)
# defined this line says what the previous defined lines adds up t0
w = "This is the left side of..."
# defined part 1 of we
e = "a string with a right side."
# defined part 2 of we
print(w+e)
# defined "we"
# More printing fum
print("Mary had a little lamb.")
# defined part 1 of mary had a little lamb
print("Its fleece was white as %s." % 'snow')
# defined part 2 of mary had a little lamb
print("And everywhere that Mary went.")
# defined part 3 of mary had a little lamb
print("." * 10)
# defined repeated dot 10 times
end1 = "c"
# defined c in cheeseburger
end2 = "h"
# defined h in cheeseburger
end3 = "e"
# defined e in cheeseburger
end4 = "e"
# defined e in cheeseburger
end5 = "s"
# defined s in cheeseburger
end6 = "e"
# defined e in cheeseburger
end7 = "b"
# defined b in cheeseburger
end8 = "u"
# defined u in cheeseburger
end9 = "r"
# defined r in cheeseburger
end10 = "g"
# defined g in cheeseburger
end11 = "e"
# defined e in cheeseburger
end12 = "r"
# defined r in cheeseburger

print(end1 + end2 + end3 + end4 + end5 + end6)

print(end7 + end8 + end9 + end10 + end11 + end12)
# But wait there is more
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, True, False))
print(formatter % (formatter, formatter, formatter, formatter))

# why do i use %r instead of %s in the above example

# which should I use on a regular basis?

# why does %r sometimes give me single quotes around things?

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJuly\nAug"

print("here are the days: ", days)
print("here are the months:", months)

print("""There's a cool thing
 you can do and 
with enough double quotes which 
is 3 you can type what ever you 
want even if it is three four or 
even five lines long """)
print("here are the months: %r" % months)
print("here are the months: %s" % months)

















