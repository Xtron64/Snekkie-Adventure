no = "no"
yes = "yes"
yes_no = ("yes" or "no")
available_classes = "Available classes: rogue, wizard, knight."


class knight:
    name = "Knight"
    knight_lore = \
        (
            "Noble warriors."
        )


class rogue:
    name = "Rogue"
    rogue_lore = \
        (
            "A thief."
        )


class wizard:
    name = "Wizard"
    wizard_lore = \
        (
            "A magic user. Wizards have bad relations with the church."
        )


classes = \
    (
        rogue, wizard, knight
    )
class_names = \
    (
            "rogue" or "wizard" or "knight"
    )


def main():
    import json
    open(character.json)


if __name__ == '__main__':
    main()

if char_class.lower() == wizard.lower() and char_sex.lower():
    pass
