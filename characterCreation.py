# We need yes, and no to know if the user agrees to something or not.
from main import yes, no, available_classes
# We need to import json to parse and write in 'character.json'
import json


def charCreation():
    while True:
        print("What do you want your character's first name to be?"),
        char_first_name = (input("You: ")),
        first_name_confirmation = input("Are you sure: ")
        if first_name_confirmation.lower() != yes.lower():
            continue
        else:
            break
    while True:
        print("What do you want your character's surname to be?"),
        char_surname = (input("You: ")),
        surname_confirmation = input("Are you sure: ")
        if surname_confirmation.lower() != yes.lower():
            continue
        else:
            break
    while True:
        print("How old do you want your character to be, in years?")
        char_age = int(input("You: "))
    while True:
        print("Do you want your character to be male or female?")
        char_sex = input("You:")
        if char_sex.lower() != "male".lower() or "man".lower() or "female".lower() or "woman".lower() or "boy".lower() or "girl".lower():
            continue
        else:
            pass
        gender_confirmation = input("Are you sure: ")
        if gender_confirmation.lower() != yes.lower():
            continue
        else:
            break
    while True:
        print("""What class do you want your character to have? If you would like to see a list of classes, enter "see 
        all""")
        class_input = input("You: ")
        if class_input.lower() == "see all".lower():
            print(available_classes),
            continue
        elif class_input != class_names:
            continue
        else:
            char_class = class_input,
            break
    char_name = (char_first_name, char_surname)

    # python object(dictionary) to be dumped
    charDict = {
        "character": {
            "name": char_name,
            "class": char_class,
            "age": char_age,
            "gender": char_sex
        },
    }

    # the json file where the output must be stored
    out_file = open("character.json", "w")

    json.dump(charDict, out_file, indent=6)

    out_file.close()
