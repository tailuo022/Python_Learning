# test 2.1
message = "This is a simple message."
print(message)
#This is a simple message.


# test 2.2
message = "Hello World!"
print(message)
message = "Hello World! Hello World!"
print(message)
# Hello World!
# Hello World! Hello World!


# test 2.3
name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")
#Hello Eric, would you like to learn some Python today?


# test 2.4
my_name = "li dong"
print(my_name.lower())
print(my_name.upper())
print(my_name.title())
# li dong
# LI DONG
# Li Dong


# test 2.5
favorite_person = "Albert Einstein"
favorite_quote = "A person who never made a mistake never tried anything new."
print(f"{favorite_person} once said, \"{favorite_quote}\"")
# Albert Einstein once said, "A person who never made a mistake never tried anything new."


# test 2.6
# 同上


# test 2.7
famous_person = "   famous  \nname\tAlbert Einstein    "
print("'" + famous_person + "'")
print("'" + famous_person.lstrip() + "'")
print("'" + famous_person.rstrip() + "'")
print("'" + famous_person.strip() + "'")
# '   famous  
# name    Albert Einstein    '
# 'famous  
# name    Albert Einstein    '
# '   famous  
# name    Albert Einstein'
# 'famous  
# name    Albert Einstein'


# test 2.8
filename = 'python_notes.txt'
print(filename.removeprefix('python_'))
print(filename.removesuffix('.txt'))
# notes.txt
# python_notes


# test 2.9
print(2 + 6)
print(10 - 2)
print(2 * 4)
print(16 // 2)
# 8
# 8
# 8
# 8


# test 2.10
favorite_number = 7
print(f"My favorite number is {favorite_number}.")
print("my favorite number is " +str(favorite_number) + ".")
# My favorite number is 7.
# My favorite number is 7.


# test 2.11
# skip


# test 2.12
import this
# he Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!