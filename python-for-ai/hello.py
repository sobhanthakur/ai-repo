long_string = """My Name is Sobhan.
I live in Bangalore.
I am a software engineer.
"""
print(long_string)


first_name = "Sobhan"
last_name = "Thakur"
full_name = first_name + " " + last_name
print(full_name)
print('-' * 12)
print(len(full_name))

day = "saturday"
is_weekend = day == "saturday" or day == "sunday"
print(is_weekend)

has_license = True
age = 18
drunk = False
can_drive = has_license and age >= 18 and not drunk
print (can_drive)

name = "Sobhan"
print(f"Hi there! My name is {name}")
print(f"Hi there! My name is {name=}")
print(f"Hi there! My name is {name=}")

sentence = "hi my name is sobhan"
word="sobhan"
print(sentence.title())
print(word.title())