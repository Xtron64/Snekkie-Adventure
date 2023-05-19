# We need these imports to import every race.
from humans import human
from demons import demon
from elfs import elf
from goblins import goblin
from orks import ork

no = "no"
yes = "yes"
yes_no = ("yes" or "no")
available_classes = "Available classes: rogue, wizard, knight."


races = \
    (
        human, demon, elf, goblin, ork
    )
races_names = \
    (
            "human" or "demon" or "elf" or "goblin" or "ork"
    )


def main():
    pass


if __name__ == '__main__':
    main()
