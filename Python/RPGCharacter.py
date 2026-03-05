full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == '' or name is None:
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    
    stats = [strength, intelligence, charisma]

    if not all(isinstance(val, int) for val in stats):
        return "All stats should be integers"
    if any(val < 1 for val in stats):
        return "All stats should be no less than 1"
    if any(val > 4 for val in stats):
        return "All stats should be no more than 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"

    return getValue(name, strength, intelligence, charisma)

def getValue(name, strength, intelligence, charisma):
    STR = f'STR {strength * full_dot}{(10 - strength) * empty_dot}'
    INT = f'INT {intelligence * full_dot}{(10 - intelligence) * empty_dot}'
    CHA = f'CHA {charisma * full_dot}{(10 - charisma) * empty_dot}'
    return f'{name}\n{STR}\n{INT}\n{CHA}'
