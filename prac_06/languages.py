from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python)
print(ruby)
print(visual_basic)

languages_list = [python, ruby, visual_basic]

# Loop through and print the names of all the languages with dynamic typing
dynamic_languages = [lang.name for lang in languages_list if lang.is_dynamic()]

print("\nThe dynamically typed languages are:")
for lang in dynamic_languages:
    print(lang)
