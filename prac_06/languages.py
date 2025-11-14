"""
CP1404 Practical - languages
Start time: 2:45am
Expected Finish time: 3:00am
Finish time: 3:07am
"""

from prac_06.programming_language import ProgrammingLanguage
def main():
    """ Program dynamic checker """
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    program_languages = [python, ruby, visual_basic] # create list of added languages
    print("The dynamically typed languages are: ")
    for language in program_languages: # Iterate through each language and check if they are dynamic
        if language.is_dynamic():
            print(language.name) # print dynamic languages

main()




