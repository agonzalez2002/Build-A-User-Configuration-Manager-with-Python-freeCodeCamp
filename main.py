def add_setting(setting_dict, setting_tup):
    key, value = setting_tup
    key = key.lower()
    value = value.lower()

    if key in setting_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    setting_dict[key] = value

    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(setting_dict, setting_tup):
    key, value = setting_tup
    key = key.lower()
    value = value.lower()

    if key in setting_dict:
        setting_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(setting_dict, key):
    key = key.lower()

    if key in setting_dict:
        del setting_dict[key]
        return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."

    lines = ["Current User Settings:"]
    for key, value in settings.items():
        lines.append(f"{key.capitalize()}: {value}")
    return "\n".join(lines) + "\n"

if __name__ == "__main__":
    test_settings = {
        'Theme': 'Dark',
        'Notifications': 'enabled',
        'Volume': 'high'
    }


print(view_settings(test_settings))
