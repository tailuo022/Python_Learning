# test 2.3
name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")
#
#Hello Eric, would you like to learn some Python today?


# test 2.4
my_name = "li dong"
print(my_name.lower())
print(my_name.upper())
print(my_name.title())
#
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