# test 3.1
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(names[0], names[1], names[2], names[3], names[4])
# Alice Bob Charlie David Eve


# test 3.2
print(f"Your name is {names[0]}.")
print("Your name is " + names[1] + ".")
# Your name is Alice.
# Your name is Bob.


# test 3.3
ways = ["walk", "bike", "drive", "bus", "train"]
print(f"I like to {ways[0]} to work.")
print(f"I like to {ways[1]} to work.")
print(f"I like to {ways[2]} to work.")
print(f"I like to {ways[3]} to work.")
print(f"I like to {ways[4]} to work.")
# I like to walk to work.
# I like to bike to work.
# I like to drive to work.
# I like to bus to work.
# I like to train to work.


# test 3.4
print("I will go to the party with " + names[0] + ", " + names[1] + ", and " + names[2] + ".")
# I will go to the party with Alice, Bob, and Charlie.


# test 3.5
out_name = names.pop( 0 )
names.insert( 0, "Alex" )
print("I will go to the party with " + names[0] + ", " + names[1] + ", and " + names[2] + ".")
print(f"Because {out_name} can't come, I will go to the party with {names[1]} and {names[2]}.")
# I will go to the party with Alex, Bob, and Charlie.
# Because Alice can't come, I will go to the party with Bob and Charlie.


# test 3.6
names.insert ( 0, "Pop" )
names.insert ( 3, "Top" )
names.append( "Stop" )
print("I will go to the party with " + names[0] + ", " + names[1] + ", and " + names[2] + ".")
print("I will go to the party with " + names[3] + ", " + names[4] + ", and " + names[5] + ".")
print("I will go to the party with " + names[6] + ", " + names[7] + ".")
# I will go to the party with Pop, Alex, and Bob.
# I will go to the party with Top, Charlie, and David.
# I will go to the party with Eve, Stop.


# test 3.7
print("I can only invite two people to the party.")
no_1 = names.pop()
print("Sorry, " + no_1 + ", I can't invite you to the party.")
no_2 = names.pop()
print("Sorry, " + no_2 + ", I can't invite you to the party.")
no_3 = names.pop()
print("Sorry, " + no_3 + ", I can't invite you to the party.")
no_4 = names.pop()
print("Sorry, " + no_4 + ", I can't invite you to the party.")
no_5 = names.pop()
print("Sorry, " + no_5 + ", I can't invite you to the party.")
no_6 = names.pop()
print("Sorry, " + no_6 + ", I can't invite you to the party.")
print(F"I will invite {names[0]} and {names[1]} to the party.")
del names[0]
del names[0]
print(names)
# I can only invite two people to the party.
# Sorry, Stop, I can't invite you to the party.
# Sorry, Eve, I can't invite you to the party.
# Sorry, David, I can't invite you to the party.
# Sorry, Charlie, I can't invite you to the party.
# Sorry, Top, I can't invite you to the party.
# Sorry, Bob, I can't invite you to the party.
# I will invite Pop and Alex to the party.
# []


# test 3.8
places = ["shangqiu", "zhanjiang", "zhenzhou", "hefei", "chengdu"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort( reverse=True)
print(places)
# ['shangqiu', 'zhanjiang', 'zhenzhou', 'hefei', 'chengdu']
# ['chengdu', 'hefei', 'shangqiu', 'zhanjiang', 'zhenzhou']
# ['shangqiu', 'zhanjiang', 'zhenzhou', 'hefei', 'chengdu']
# ['zhenzhou', 'zhanjiang', 'shangqiu', 'hefei', 'chengdu']
# ['shangqiu', 'zhanjiang', 'zhenzhou', 'hefei', 'chengdu']
# ['chengdu', 'hefei', 'zhenzhou', 'zhanjiang', 'shangqiu']
# ['shangqiu', 'zhanjiang', 'zhenzhou', 'hefei', 'chengdu']
# ['chengdu', 'hefei', 'shangqiu', 'zhanjiang', 'zhenzhou']
# ['zhenzhou', 'zhanjiang', 'shangqiu', 'hefei', 'chengdu']


# test 3.9
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names.insert ( 0, "Pop" )
names.insert ( 3, "Top" )
names.append( "Stop" )
length_names = len(names)
print(f"Here are {length_names} people who will go to my party")
# Here are 8 people who will go to my party


# test 3.10
# 如上


# test 3.11
print(names[10])
# IndexError: list index out of range