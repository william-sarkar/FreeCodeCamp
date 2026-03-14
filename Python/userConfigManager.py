def add_setting(settings: dict, pair: tuple):
    key, value = pair
    key_lower = str(key).lower()
    value_lower = str(value).lower()
    if key_lower in settings:
        return f"Setting '{key_lower}' already exists! Cannot add a new setting with this name."
    
    settings[key_lower] = value_lower
    return f"Setting '{key_lower}' added with value '{value_lower}' successfully!"

def update_setting(settings: dict, pair: tuple):
    key, value = pair
    key_lower = str(key).lower()
    value_lower = str(value).lower()

    if key_lower in settings:
        settings[key_lower] = value_lower
        return f"Setting '{key_lower}' updated to '{value_lower}' successfully!"
    
    return f"Setting '{key_lower}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings: dict, key):
    key_lower = str(key).lower()

    if key_lower in settings:
        del settings[key_lower]
        return f"Setting '{key_lower}' deleted successfully!"
    
    return "Setting not found!"

def view_settings(settings: dict):
    if not settings:
        return "No settings available."
    
    lines = [f"{str(key).capitalize()}: {value}" for key, value in settings.items()]

    return "Current User Settings:\n" + "\n".join(lines) + "\n"

test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}

