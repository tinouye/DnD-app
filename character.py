import json

all_skills = {
        "acrobatics": "dex",
        "animal handling": "wis",
        "arcana": "int",
        "athletics": "str",
        "deception": "cha",
        "history": "int",
        "insight": "wis",
        "initimidation": "cha",
        "investigation": "int",
        "medicine": "wis",
        "nature": "int",
        "perception": "wis",
        "performance": "cha",
        "persuasion": "cha",
        "religion": "int",
        "sleight of hand": "dex",
        "stealth": "dex",
        "survival": "wis"
    }

class Character:

    stats = {
        "str": None,
        "dex": None,
        "con": None,
        "int": None,
        "wis": None,
        "cha": None
    }

    skills = []

    def __init__(self, name, player_class, level, background, race,
    stats, inspiration, prof_bonus, saving_throws, skills, ac, speed, hp, temp_hp, hit_dice, death_saves, money,
    spell_slots, spells
    ):
        self.name = name
        self.player_class = player_class
        self.level = level
        self.background = background
        self.race = race
        self.inspiration = inspiration
        self.prof_bonus = prof_bonus
        self.ac = ac
        self.speed = speed
        self.hp = hp
        self.temp_hp = temp_hp
        self.hit_dice = hit_dice
        self.death_saves = death_saves
        self.money = money
        self.skills = skills
        self.saving_throws = saving_throws
        self.spell_slots = spell_slots
        self.spells = spells
        
        for stat in stats:
            self.stats[stat] = stats[stat]


    def save_character(self):
        char_data_json = json.dumps(self.__dict__)
        save_file = open(f"{self.name}.json", "w")
        save_file.write(char_data_json)
        save_file.close()
