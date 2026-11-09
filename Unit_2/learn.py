message = "Hello World!"
rename_message = "Rename Hello World!"
print(message, rename_message)
print(message)  
print(rename_message)
print()
print("rename_message \n message")

# result
# Hello World! Rename Hello World!
# Hello World!
# Rename Hello World!
#
# rename_messag1e 
#  message
# \n 不能在变量里面使用 如 
# print(message \n rename_message)

print()
#练习
first_name = "dong"
last_name = "li"
full_name = last_name + " " + first_name
print(full_name)
other_name = "li" + " " + "dong"
print(other_name)
another_name = f"{last_name} {first_name}"
print(another_name)
# li dong
# li dong
# li dong

print()
# 练习
Full_Name = full_name.title()
print(Full_Name)
print(full_name.title())
print(f"hello {full_name.title()}!")
print(full_name.upper())
print(Full_Name.lower())
message_name = f"hello {full_name}"
print(message_name)
# Li Dong
# Li Dong
# hello Li Dong!
# LI DONG
# li dong
# hello li dong

print()
# 练习
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")  
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# Python
#         Python
# Languages:
# Python
# C
# JavaScript
# Languages:
#         Python
#         C
#         JavaScript

print()
# 练习
favorite_language = ' python '
favorite_language = favorite_language.rstrip()
print("'" + favorite_language + "'")
favorite_language = ' python '
favorite_language = favorite_language.lstrip()
print("'" + favorite_language + "'")
favorite_language = ' python '
favorite_language = favorite_language.strip()
print("'" + favorite_language + "'")
# ' python'
# 'python '
# 'python'

print()
# 练习
nostarch_url = 'https://nostarch.com'
nostarch_url = nostarch_url.replace('https://', '')
print(nostarch_url)
nostarch_url = 'https://nostarch.com'
nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)
# nostarch.com
# nostarch.com